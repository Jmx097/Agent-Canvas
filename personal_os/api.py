from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from agents.job_scout import JobScoutAgent
from agents.thread_spotter import ThreadSpotterAgent
from agents.orchestrator import OrchestratorAgent
from core.pruner import prune_items
from config.settings import settings

app = FastAPI()

# Allow CORS for dev (Vite runs on 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/plan")
def get_plan():
    plan_path = settings.BASE_DIR / "data" / "daily_plan.md"
    if not plan_path.exists():
        return {"content": "No plan generated yet."}
    return {"content": plan_path.read_text(encoding="utf-8")}

@app.get("/api/jobs")
def get_jobs():
    from db.database import SessionLocal
    from db.models import ScoredItem
    db = SessionLocal()
    try:
        top_jobs = db.query(ScoredItem).filter_by(
            type="JOB", 
            status="NEW"
        ).order_by(ScoredItem.score.desc()).limit(10).all()
        
        jobs_data = [{
            "id": job.id,
            "title": job.title,
            "score": job.score,
            "score_details": job.score_details,
            "content_summary": job.content_summary,
            "created_at": job.created_at.isoformat()
        } for job in top_jobs]
        
        return {"jobs": jobs_data}
    finally:
        db.close()

@app.post("/api/run/{agent_name}")
def run_agent(agent_name: str):
    try:
        if agent_name == "job-scout":
            JobScoutAgent().execute()
            return {"status": "success", "message": "Job Scout finished processing CSV."}
        elif agent_name == "thread-spotter":
            ThreadSpotterAgent().execute()
        elif agent_name == "orchestrator":
            OrchestratorAgent().execute()
        else:
            raise HTTPException(status_code=404, detail="Agent not found")
        return {"status": "success", "message": f"{agent_name} executed."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/prune")
def run_prune():
    try:
        prune_items()
        return {"status": "success", "message": "Pruning complete."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serve Static Files (Dashboard)
# Must be after API routes
dashboard_path = settings.BASE_DIR / "dashboard" / "dist"
if dashboard_path.exists():
    app.mount("/", StaticFiles(directory=str(dashboard_path), html=True), name="dashboard")


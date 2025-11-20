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
            "url": job.url,
            "created_at": job.created_at.isoformat()
        } for job in top_jobs]
        
        return {"jobs": jobs_data}
    finally:
        db.close()

@app.get("/api/trends")
def get_trends():
    from db.database import SessionLocal
    from db.models import ScoredItem
    db = SessionLocal()
    try:
        top_threads = db.query(ScoredItem).filter_by(
            type="THREAD", 
            status="NEW"
        ).order_by(ScoredItem.score.desc()).limit(10).all()
        
        threads_data = [{
            "id": thread.id,
            "title": thread.title,
            "score": thread.score,
            "score_details": thread.score_details,
            "content_summary": thread.content_summary,
            "source_id": thread.source_id,
            "url": thread.url,
            "created_at": thread.created_at.isoformat()
        } for thread in top_threads]
        
        return {"threads": threads_data}
    finally:
        db.close()

@app.post("/api/run/{agent_name}")
def run_agent(agent_name: str):
    try:
        if agent_name == "job-scout":
            JobScoutAgent().execute()
            return {"status": "success", "message": "Job Scout finished processing."}
        elif agent_name == "thread-spotter":
            ThreadSpotterAgent().execute()
            return {"status": "success", "message": "Thread Spotter finished processing."}
        elif agent_name == "orchestrator":
            OrchestratorAgent().execute()
            return {"status": "success", "message": "Orchestrator finished generating plan."}
        else:
            raise HTTPException(status_code=404, detail="Agent not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/prune")
def run_prune():
    try:
        prune_items()
        return {"status": "success", "message": "Pruning complete."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ... existing code ...

@app.post("/api/chat")
async def chat_endpoint(request: dict):
    from core.llm import call_llm
    user_message = request.get("message", "")
    if not user_message:
        raise HTTPException(status_code=400, detail="Message required")
    
    response = call_llm(user_message)
    return {"response": response.content}

@app.get("/api/tasks")
def get_tasks():
    from db.database import SessionLocal
    from db.models import Task
    db = SessionLocal()
    try:
        tasks = db.query(Task).filter(Task.status != "DONE").all()
        return {"tasks": [{"id": t.id, "title": t.title, "status": t.status, "due": t.due_date} for t in tasks]}
    finally:
        db.close()

@app.post("/api/tasks")
def create_task(task: dict):
    from db.database import SessionLocal
    from db.models import Task
    db = SessionLocal()
    try:
        new_task = Task(title=task.get("title"), status="TODO")
        db.add(new_task)
        db.commit()
        return {"status": "success", "task_id": new_task.id}
    finally:
        db.close()

@app.get("/api/calendar")
def get_calendar():
    # Placeholder for Google Calendar integration
    # In a real implementation, this would call the Google API
    return {"events": [
        {"id": "1", "title": "Deep Work Session", "start": "2025-11-21T09:00:00", "end": "2025-11-21T11:00:00"},
        {"id": "2", "title": "Team Sync", "start": "2025-11-21T14:00:00", "end": "2025-11-21T15:00:00"}
    ]}

# Serve Static Files (Dashboard)
# Must be after API routes
dashboard_path = settings.BASE_DIR / "dashboard" / "dist"
if dashboard_path.exists():
    app.mount("/", StaticFiles(directory=str(dashboard_path), html=True), name="dashboard")


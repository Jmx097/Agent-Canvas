import typer
from agents.job_scout import JobScoutAgent
from agents.thread_spotter import ThreadSpotterAgent
from agents.orchestrator import OrchestratorAgent
from db.database import init_db
from config.logging_config import logger

app = typer.Typer()

@app.command()
def init():
    """Initialize the database."""
    init_db()
    logger.info("Database initialized.")

@app.command()
def job_scout():
    """Run the Job Scout Agent."""
    JobScoutAgent().execute()

@app.command()
def thread_spotter():
    """Run the Thread Spotter Agent."""
    ThreadSpotterAgent().execute()

@app.command()
def orchestrator():
    """Run the Orchestrator Agent."""
    OrchestratorAgent().execute()

@app.command()
def run_all():
    """Run all agents in sequence."""
    logger.info("Running all agents...")
    JobScoutAgent().execute()
    ThreadSpotterAgent().execute()
    OrchestratorAgent().execute()
    logger.info("All agents finished.")

@app.command()
def prune(days: int = 14, rejected_days: int = 3):
    """Prune old items from the database."""
    from core.pruner import prune_items
    prune_items(days, rejected_days)

@app.command()
def serve(port: int = 8000):
    """Start the Personal OS API server."""
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=port, reload=True, app_dir="personal_os")

if __name__ == "__main__":
    app()

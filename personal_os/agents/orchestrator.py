from datetime import datetime
from core.base_agent import BaseAgent
from db.models import ScoredItem
from config.logging_config import logger

class OrchestratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("Orchestrator")

    def run(self):
        # 1. Get NEW items
        new_jobs = self.db.query(ScoredItem).filter_by(type="JOB", status="NEW").all()
        new_threads = self.db.query(ScoredItem).filter_by(type="THREAD", status="NEW").all()

        logger.info(f"Orchestrator found {len(new_jobs)} new jobs and {len(new_threads)} new threads.")

        # 2. Generate Plan via LLM
        from core.llm import call_llm
        
        context = f"Found {len(new_jobs)} new jobs and {len(new_threads)} new threads.\n"
        if new_jobs:
            context += "Top Job: " + new_jobs[0].title + "\n"
        
        prompt = f"""
        You are the Orchestrator for a Personal OS.
        Context: {context}
        
        Generate a daily plan in Markdown format.
        Include 3 blocks: Deep Work, Content/Community, and Admin.
        """
        
        response = call_llm(prompt)
        plan = response.content if hasattr(response, 'content') else str(response)

        # 3. Save Plan
        with open("data/daily_plan.md", "w") as f:
            f.write(plan)
        
        logger.info("Daily plan generated at data/daily_plan.md")

if __name__ == "__main__":
    OrchestratorAgent().execute()

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

        # 2. Generate Plan
        plan = f"# Daily Workbench Plan - {datetime.now().strftime('%Y-%m-%d')}\n\n"

        # Block 1: Job Search
        plan += "## Block 1: Job Search Deep Work (90 mins)\n"
        if new_jobs:
            for job in new_jobs:
                plan += f"- [ ] Review: {job.title} (Score: {job.score})\n"
        else:
            plan += "- No new high-scoring jobs today.\n"
        plan += "\n"

        # Block 2: Content & Community
        plan += "## Block 2: Content & Community (60 mins)\n"
        if new_threads:
            for thread in new_threads:
                plan += f"- [ ] Reply to: {thread.title} (Score: {thread.score})\n"
        else:
            plan += "- No new threads to engage with.\n"
        plan += "\n"

        # Block 3: Admin
        plan += "## Block 3: Admin & Learning (45 mins)\n"
        plan += "- [ ] Clear inbox\n"
        plan += "- [ ] Update run-logs\n"

        # 3. Save Plan
        with open("data/daily_plan.md", "w") as f:
            f.write(plan)
        
        logger.info("Daily plan generated at data/daily_plan.md")

if __name__ == "__main__":
    OrchestratorAgent().execute()

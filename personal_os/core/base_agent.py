from abc import ABC, abstractmethod
from datetime import datetime
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import AgentRun
from config.logging_config import logger
import traceback

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.db: Session = SessionLocal()

    @abstractmethod
    def run(self):
        """Core logic of the agent."""
        pass

    def execute(self):
        """Wrapper to handle logging, DB recording, and error handling."""
        logger.info(f"Starting agent: {self.name}")
        run_record = AgentRun(agent_name=self.name, status="RUNNING")
        self.db.add(run_record)
        self.db.commit()
        self.db.refresh(run_record)

        try:
            self.run()
            run_record.status = "SUCCESS"
            run_record.end_time = datetime.now()
            logger.info(f"Agent {self.name} completed successfully.")
        except Exception as e:
            run_record.status = "FAILED"
            run_record.end_time = datetime.now()
            run_record.log_summary = str(e) + "\n" + traceback.format_exc()
            logger.error(f"Agent {self.name} failed: {e}")
        finally:
            self.db.commit()
            self.db.close()

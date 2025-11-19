from db.database import init_db
from core.base_agent import BaseAgent
from config.logging_config import logger
import sys

# Initialize DB
init_db()

class TestAgent(BaseAgent):
    def run(self):
        logger.info("Test Agent is running logic...")
        # Simulate work
        import time
        time.sleep(1)
        logger.info("Test Agent logic done.")

def main():
    logger.info("Verifying Personal OS Foundation...")
    agent = TestAgent("TestAgent")
    agent.execute()
    logger.info("Verification complete. Check personal_os.db and personal_os.log")

if __name__ == "__main__":
    main()

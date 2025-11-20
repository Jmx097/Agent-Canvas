from sqlalchemy import Column, Integer, String, DateTime, Text, JSON, Float
from sqlalchemy.sql import func
from db.database import Base

class AgentRun(Base):
    __tablename__ = "agent_runs"

    id = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String, index=True)
    start_time = Column(DateTime(timezone=True), server_default=func.now())
    end_time = Column(DateTime(timezone=True), nullable=True)
    status = Column(String)  # SUCCESS, FAILED, RUNNING
    items_processed = Column(Integer, default=0)
    log_summary = Column(Text, nullable=True)

class ScoredItem(Base):
    __tablename__ = "scored_items"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(String, unique=True, index=True) # URL or unique ID
    type = Column(String) # JOB, THREAD
    url = Column(String, nullable=True) # URL to the item
    title = Column(String)
    content_summary = Column(Text)
    score = Column(Float)
    score_details = Column(JSON) # Breakdown of score
    status = Column(String, default="NEW") # NEW, APPLIED, REJECTED, ARCHIVED
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(String, default="TODO") # TODO, IN_PROGRESS, DONE
    due_date = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

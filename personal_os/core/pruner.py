from datetime import datetime, timedelta
from db.database import SessionLocal
from db.models import ScoredItem
from config.logging_config import logger

def prune_items(days_to_keep: int = 14, rejected_days: int = 3):
    """
    Deletes items older than `days_to_keep`.
    Deletes REJECTED items older than `rejected_days`.
    """
    db = SessionLocal()
    try:
        now = datetime.now()
        
        # Prune old items (general)
        cutoff_general = now - timedelta(days=days_to_keep)
        deleted_general = db.query(ScoredItem).filter(
            ScoredItem.created_at < cutoff_general
        ).delete()

        # Prune rejected items (aggressive)
        cutoff_rejected = now - timedelta(days=rejected_days)
        deleted_rejected = db.query(ScoredItem).filter(
            ScoredItem.status == "REJECTED",
            ScoredItem.created_at < cutoff_rejected
        ).delete()

        db.commit()
        logger.info(f"Pruning complete. Deleted {deleted_general} old items and {deleted_rejected} rejected items.")
    except Exception as e:
        logger.error(f"Pruning failed: {e}")
        db.rollback()
    finally:
        db.close()

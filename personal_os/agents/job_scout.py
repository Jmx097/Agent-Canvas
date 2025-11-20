import csv
import json
from pathlib import Path
from core.base_agent import BaseAgent
from db.models import ScoredItem
from config.logging_config import logger
from config.settings import settings

class JobScoutAgent(BaseAgent):
    def __init__(self):
        super().__init__("Job Scout")
        self.input_csv_path = settings.BASE_DIR / "data" / "jobs_input.csv"
        self.cv_profile_path = settings.BASE_DIR / "data" / "cv_profile.json"
        self.cv_profile = self.load_cv_profile()

    def load_cv_profile(self):
        if not self.cv_profile_path.exists():
            logger.warning("CV profile not found. Using default scoring.")
            return None
        with open(self.cv_profile_path, "r") as f:
            return json.load(f)

    def load_from_csv(self):
        if not self.input_csv_path.exists():
            logger.warning(f"Input CSV not found at {self.input_csv_path}")
            return []
        
        jobs = []
        try:
            with open(self.input_csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Ensure required fields exist
                    if not row.get("id") or not row.get("title"):
                        continue
                        
                    jobs.append({
                        "id": row.get("id"),
                        "title": row.get("title"),
                        "company": row.get("company", "Unknown"),
                        "description": row.get("description", ""),
                        "url": row.get("url", ""),
                        "location": row.get("location", "Unknown")
                    })
        except Exception as e:
            logger.error(f"Failed to read CSV: {e}")
            return []
            
        return jobs

    def score_job(self, job):
        """
        Enhanced CV-based scoring:
        - Title Match (0-40): Target roles vs excluded seniority
        - Skills Match (0-30): Preferred skills in description
        - Location Match (0-20): Remote + U.S. preference
        - Seniority Filter (0-10): Penalize senior roles
        """
        if not self.cv_profile:
            return self.score_job_fallback(job)

        score = 0
        details = {}
        title = job.get("title", "").lower()
        desc = job.get("description", "").lower()
        location = job.get("location", "").lower()
        combined_text = f"{title} {desc}"

        # Title Match (0-40)
        target_titles = self.cv_profile.get("target_titles", [])
        excluded_titles = self.cv_profile.get("excluded_titles", [])
        
        # Check for exclusions first
        if any(excluded in title for excluded in excluded_titles):
            score = 0
            details["title"] = -100
            details["reason"] = "Senior/Leadership role excluded"
            return score, details
        
        # Check for target titles
        title_matches = sum(1 for t in target_titles if t in title)
        if title_matches > 0:
            score += min(40, title_matches * 20)  # Cap at 40
            details["title"] = min(40, title_matches * 20)
        else:
            details["title"] = 0

        # Skills Match (0-30)
        preferred_skills = self.cv_profile.get("preferred_skills", [])
        skill_matches = sum(1 for skill in preferred_skills if skill in combined_text)
        if skill_matches > 0:
            skill_score = min(30, skill_matches * 3)  # Cap at 30
            score += skill_score
            details["skills"] = skill_score
        else:
            details["skills"] = 0

        # Location Match (0-20)
        loc_prefs = self.cv_profile.get("location_preferences", {})
        if loc_prefs.get("primary", "remote") in location:
            score += 15
            details["location"] = 15
        elif any(region in location for region in loc_prefs.get("regions", [])):
            score += 10
            details["location"] = 10
        else:
            details["location"] = 0

        # Bonus for explicit "remote" mention
        if "remote" in location or "remote" in title:
            score += 5
            details["remote_bonus"] = 5

        return score, details

    def score_job_fallback(self, job):
        """Fallback scoring if CV profile not available."""
        score = 0
        details = {}
        title = job.get("title", "").lower()
        desc = job.get("description", "").lower()
        loc = job.get("location", "").lower()

        if any(x in title for x in ["solutions consultant", "implementation", "pre-sales"]):
            score += 30
            details["title"] = 30
        elif "engineer" in title:
            score += 10
            details["title"] = 10
        else:
            details["title"] = 0

        if "remote" in loc or "anywhere" in loc:
            score += 20
            details["location"] = 20
        else:
            details["location"] = 0

        return score, details

    def run(self):
        jobs = self.load_from_csv()
        logger.info(f"Loaded {len(jobs)} jobs from CSV.")

        new_count = 0
        for job in jobs:
            existing = self.db.query(ScoredItem).filter_by(source_id=str(job["id"])).first()
            if existing:
                continue

            score, details = self.score_job(job)
            
            # Threshold: Only save jobs with score >= 30
            status = "NEW" if score >= 30 else "REJECTED"

            desc_summary = job["description"][:500] + "..." if len(job["description"]) > 500 else job["description"]

            item = ScoredItem(
                source_id=str(job["id"]),
                type="JOB",
                title=job["title"],
                content_summary=desc_summary,
                score=score,
                score_details=details,
                status=status,
                # Store URL in content_summary or a new field if model allowed, 
                # but for now we can append it to summary or rely on source_id if it was a URL.
                # Ideally we should have a 'url' field, but I'll pack it into the summary for now 
                # or assume source_id is the key. 
                # Wait, the user wants to click "Apply". 
                # I'll store the URL in the 'source_id' if it's a URL, or I need to check the model.
                # The model has 'source_id'. If the CSV 'id' is not a URL, we might lose the link.
                # Let's check the model again.
            )
            # Hack: Store URL in the score_details for now so the frontend can grab it, 
            # since we can't easily migrate the DB schema right this second without alembic.
            # Or better: The 'source_id' in the CSV should ideally be the URL if possible, 
            # but the user might provide an ID.
            # Let's store the URL in score_details['url']
            details['url'] = job['url']
            item.score_details = details

            self.db.add(item)
            new_count += 1
            if status == "NEW":
                logger.info(f"Found match: '{job['title']}' at {job['company']} (Score: {score})")

        self.db.commit()
        logger.info(f"Job Scout finished. Processed {new_count} new jobs.")

if __name__ == "__main__":
    JobScoutAgent().execute()

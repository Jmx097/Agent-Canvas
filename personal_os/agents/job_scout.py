import json
import feedparser
import requests
from pathlib import Path
from core.base_agent import BaseAgent
from db.models import ScoredItem
from config.logging_config import logger
from config.settings import settings

class JobScoutAgent(BaseAgent):
    def __init__(self):
        super().__init__("Job Scout")
        self.feeds_path = settings.BASE_DIR / "data" / "job_feeds.json"
        self.cv_profile_path = settings.BASE_DIR / "data" / "cv_profile.json"
        self.cv_profile = self.load_cv_profile()

    def load_cv_profile(self):
        if not self.cv_profile_path.exists():
            logger.warning("CV profile not found. Using default scoring.")
            return None
        with open(self.cv_profile_path, "r") as f:
            return json.load(f)

    def fetch_from_rss(self, url):
        try:
            feed = feedparser.parse(url)
            jobs = []
            for entry in feed.entries:
                jobs.append({
                    "id": entry.get("id", entry.get("link")),
                    "title": entry.get("title", "No Title"),
                    "company": entry.get("author", "Unknown"),
                    "description": entry.get("summary", entry.get("description", "")),
                    "url": entry.get("link"),
                    "location": "Unknown"
                })
            return jobs
        except Exception as e:
            logger.error(f"Failed to parse RSS {url}: {e}")
            return []

    def fetch_from_api(self, url):
        try:
            resp = requests.get(url, headers={"User-Agent": "PersonalOS/1.0"})
            if resp.status_code != 200:
                return []
            
            data = resp.json()
            jobs = []
            
            if "remoteok" in url:
                for item in data:
                    if not isinstance(item, dict): continue
                    jobs.append({
                        "id": item.get("id", item.get("url")),
                        "title": item.get("position", "No Title"),
                        "company": item.get("company", "Unknown"),
                        "description": item.get("description", ""),
                        "url": item.get("url"),
                        "location": item.get("location", "Remote")
                    })
            
            elif "jobicy" in url:
                for item in data.get("jobs", []):
                    jobs.append({
                        "id": item.get("id", item.get("url")),
                        "title": item.get("jobTitle", "No Title"),
                        "company": item.get("companyName", "Unknown"),
                        "description": item.get("jobDescription", ""),
                        "url": item.get("url"),
                        "location": item.get("jobGeo", "Remote")
                    })

            return jobs
        except Exception as e:
            logger.error(f"Failed to fetch API {url}: {e}")
            return []

    def fetch_jobs(self):
        if not self.feeds_path.exists():
            logger.warning("No feed config found.")
            return []

        with open(self.feeds_path, "r") as f:
            feeds = json.load(f)

        all_jobs = []
        for feed in feeds:
            logger.info(f"Fetching {feed['name']} ({feed['type']})...")
            if feed["type"] == "RSS":
                all_jobs.extend(self.fetch_from_rss(feed["url"]))
            elif feed["type"] == "API":
                all_jobs.extend(self.fetch_from_api(feed["url"]))
        
        return all_jobs

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
        jobs = self.fetch_jobs()
        logger.info(f"Fetched {len(jobs)} total jobs from feeds.")

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
                status=status
            )
            self.db.add(item)
            new_count += 1
            if status == "NEW":
                logger.info(f"Found match: '{job['title']}' at {job['company']} (Score: {score})")

        self.db.commit()
        logger.info(f"Job Scout finished. Processed {new_count} new jobs.")

if __name__ == "__main__":
    JobScoutAgent().execute()

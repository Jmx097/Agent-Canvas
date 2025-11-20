import json
import requests
import time
from pathlib import Path
from core.base_agent import BaseAgent
from db.models import ScoredItem
from config.logging_config import logger

class ThreadSpotterAgent(BaseAgent):
    def __init__(self):
        super().__init__("Thread Spotter")
        from config.settings import settings
        self.sources_path = settings.BASE_DIR / "data" / "thread_sources.json"

    def fetch_from_reddit_json(self, url):
        try:
            # Reddit requires a unique User-Agent
            headers = {"User-Agent": "PersonalOS/1.0 (by /u/PersonalOS_Bot)"}
            resp = requests.get(url, headers=headers)
            
            if resp.status_code != 200:
                logger.error(f"Failed to fetch Reddit JSON {url}: {resp.status_code}")
                return []

            data = resp.json()
            threads = []
            
            # Reddit JSON structure: data -> children -> data
            for child in data.get("data", {}).get("children", []):
                post = child.get("data", {})
                threads.append({
                    "id": post.get("id"),
                    "title": post.get("title", "No Title"),
                    "content": post.get("selftext", "") or post.get("url", ""), # Use URL if no text
                    "url": f"https://reddit.com{post.get('permalink')}",
                    "subreddit": post.get("subreddit"),
                    "comments_count": post.get("num_comments", 0),
                    "created_utc": post.get("created_utc")
                })
            return threads
        except Exception as e:
            logger.error(f"Failed to parse Reddit JSON {url}: {e}")
            return []

    def fetch_threads(self):
        if not self.sources_path.exists():
            logger.warning("No thread sources config found.")
            return []

        with open(self.sources_path, "r") as f:
            sources = json.load(f)

        all_threads = []
        for source in sources:
            logger.info(f"Fetching {source['name']} ({source['type']})...")
            if source["type"] == "Reddit":
                all_threads.extend(self.fetch_from_reddit_json(source["url"]))
                time.sleep(1) # Be nice to Reddit API
        
        return all_threads

    def score_thread(self, thread):
        """
        Scoring Rubric:
        - Relevance (0-30): nocode/automation keywords
        - Engagement (0-20): Low comments (opportunity)
        - Values (0-25): No crypto/spam
        """
        score = 0
        details = {}

        # Relevance
        text = (thread.get("title", "") + " " + thread.get("content", "")).lower()
        sub = thread.get("subreddit", "").lower()
        
        keywords = ["nocode", "automation", "make.com", "zapier", "workflow", "agent", "ai"]
        if any(x in text or x in sub for x in keywords):
            score += 30
            details["relevance"] = 30
        else:
            details["relevance"] = 0

        # Values (Penalty)
        if "crypto" in text or "buy now" in text or "token" in text:
            score = 0
            details["values"] = -100 # Kill it
            return score, details
        else:
            details["values"] = 10

        # Engagement (Opportunity)
        comments = thread.get("comments_count", 0)
        if comments < 10:
            score += 20
            details["engagement"] = 20 # Good opportunity to be early
        elif comments < 50:
            score += 10
            details["engagement"] = 10
        else:
            details["engagement"] = 5

        return score, details

    def run(self):
        threads = self.fetch_threads()
        logger.info(f"Fetched {len(threads)} total threads from sources.")

        new_count = 0
        for thread in threads:
            # Check if exists (using source_id)
            if self.db.query(ScoredItem).filter_by(source_id=str(thread["id"])).first():
                continue

            score, details = self.score_thread(thread)
            
            # Threshold check
            status = "NEW" if score >= 40 else "REJECTED"

            # Truncate content for DB
            content_summary = thread["content"][:500] + "..." if len(thread["content"]) > 500 else thread["content"]

            item = ScoredItem(
                source_id=str(thread["id"]),
                type="THREAD",
                title=thread["title"],
                content_summary=content_summary,
                score=score,
                score_details=details,
                status=status,
                url=thread.get("url")
            )
            self.db.add(item)
            new_count += 1
            
            if status == "NEW":
                logger.info(f"Found match: '{thread['title']}' (Score: {score})")

        self.db.commit()
        logger.info(f"Thread Spotter finished. Processed {new_count} new threads.")

if __name__ == "__main__":
    ThreadSpotterAgent().execute()

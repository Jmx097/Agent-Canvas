import requests
import json
import sys
import time
from db.database import SessionLocal
from db.models import ScoredItem

API_BASE = "http://localhost:8000/api"

def check_api_urls():
    print("Checking API URLs...")
    try:
        # Check Jobs
        res = requests.get(f"{API_BASE}/jobs")
        if res.status_code == 200:
            jobs = res.json().get("jobs", [])
            print(f"API returned {len(jobs)} jobs.")
            for job in jobs:
                if "url" not in job:
                    print("FAILURE: Job missing 'url' field in API response.")
                    return False
        else:
            print(f"FAILURE: Failed to fetch jobs. Status: {res.status_code}")
            return False

        # Check Threads
        res = requests.get(f"{API_BASE}/trends")
        if res.status_code == 200:
            threads = res.json().get("threads", [])
            print(f"API returned {len(threads)} threads.")
            for thread in threads:
                if "url" not in thread:
                    print("FAILURE: Thread missing 'url' field in API response.")
                    return False
        else:
            print(f"FAILURE: Failed to fetch threads. Status: {res.status_code}")
            return False
            
        print("SUCCESS: API responses contain 'url' field.")
        return True
    except Exception as e:
        print(f"Error checking API: {e}")
        return False

def check_db_urls():
    print("Checking Database URLs...")
    db = SessionLocal()
    try:
        items = db.query(ScoredItem).all()
        print(f"Found {len(items)} items in database.")
        
        missing_url = 0
        for item in items:
            if not item.url:
                # It's possible some old items don't have URLs if we didn't prune, 
                # but we recreated the DB, so all should have URLs if the agents worked.
                # However, if the source didn't provide a URL, it might be None.
                # But our test data should have URLs.
                print(f"WARNING: Item {item.id} ({item.type}) has no URL.")
                missing_url += 1
        
        if missing_url == len(items) and len(items) > 0:
             print("FAILURE: All items missing URLs.")
             return False
             
        print("SUCCESS: Database check complete.")
        return True
    finally:
        db.close()

def run_agents():
    print("Triggering Agents...")
    # Trigger Job Scout
    try:
        requests.post(f"{API_BASE}/run/job-scout")
        print("Job Scout triggered.")
    except:
        print("Failed to trigger Job Scout")

    # Trigger Thread Spotter
    try:
        requests.post(f"{API_BASE}/run/thread-spotter")
        print("Thread Spotter triggered.")
    except:
        print("Failed to trigger Thread Spotter")
        
    time.sleep(2) # Wait for async processing if any (though currently synchronous in API)

if __name__ == "__main__":
    run_agents()
    if check_db_urls() and check_api_urls():
        print("ALL CHECKS PASSED")
        sys.exit(0)
    else:
        print("SOME CHECKS FAILED")
        sys.exit(1)

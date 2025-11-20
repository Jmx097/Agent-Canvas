import requests
import json
import sys

url = "http://localhost:8000/api/chat"
payload = {"message": "Hello, are you working?"}
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code == 200 and "response" in response.json():
        print("SUCCESS: Chat API is working.")
    else:
        print("FAILURE: Chat API returned unexpected response.")
        sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

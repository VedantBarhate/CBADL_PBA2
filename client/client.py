import requests
import time

MAX_RETRIES = 3

for attempt in range(1, MAX_RETRIES + 1):
    response = requests.get("http://127.0.0.1:8000/sum", params={"a": 5, "b": 10})
    if response.status_code < 500:
        break
    print(f"Attempt {attempt}: got {response.status_code}, retrying...")
    time.sleep(2)

print(response.json())
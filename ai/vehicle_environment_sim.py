<<<<<<< HEAD
import random
import time
import requests

BACKEND_URL = "http://127.0.0.1:5000/vehicle"

while True:
    payload = {
        "vehicle_id": "BUS_101",
        "speed": random.randint(30, 90),
        "latitude": round(random.uniform(12.90, 13.10), 6),
        "longitude": round(random.uniform(80.10, 80.30), 6)
    }

    try:
        requests.post(BACKEND_URL, json=payload, timeout=1)
        print("Sent vehicle data:", payload)
    except:
        print("Backend not reachable")

    time.sleep(2)
=======
import random
import time
import requests

BACKEND_URL = "http://127.0.0.1:5000/vehicle"

while True:
    payload = {
        "vehicle_id": "BUS_101",
        "speed": random.randint(30, 90),
        "latitude": round(random.uniform(12.90, 13.10), 6),
        "longitude": round(random.uniform(80.10, 80.30), 6)
    }

    try:
        requests.post(BACKEND_URL, json=payload, timeout=1)
        print("Sent vehicle data:", payload)
    except:
        print("Backend not reachable")

    time.sleep(2)
>>>>>>> frontend-dev

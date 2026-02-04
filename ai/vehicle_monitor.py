import random
import time
import requests

BACKEND_URL = "http://127.0.0.1:5000/ai/status"

print("Vehicle Parameter Monitor started...")

while True:
    # 🔧 Simulated sensor values
    speed = random.randint(30, 100)
    engine_temp = random.randint(70, 110)
    fuel_level = random.randint(5, 100)

    # ✅ DEFINE FLAGS (THIS WAS MISSING)
    overspeed = speed > 60
    engine_overheat = engine_temp > 95
    low_fuel = fuel_level < 20

    payload = {
        "overspeed": overspeed,
        "low_fuel": low_fuel,
        "engine_overheat": engine_overheat
    }

    try:
        requests.post(
            BACKEND_URL,
            json=payload,
            timeout=0.3
        )
        print("Vehicle data sent:", payload)
    except Exception as e:
        print("Error sending vehicle data:", e)

    time.sleep(2)

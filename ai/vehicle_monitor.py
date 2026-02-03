import random
import time

MAX_SPEED = 60
MAX_TEMP = 95 

while True:
    speed = random.randint(30, 90)
    engine_temp = random.randint(70, 110)
    brake_pressure = random.choice([0, 1])

    alerts = []

    if speed > MAX_SPEED:
        alerts.append("OVERSPEED ⚠️")

    if engine_temp > MAX_TEMP:
        alerts.append("ENGINE OVERHEAT 🔥")

    if brake_pressure == 1 and speed > 40:
        alerts.append("EMERGENCY BRAKE ⚠️")

    print(f"Speed: {speed} km/h | Temp: {engine_temp}°C")
    for alert in alerts:
        print("ALERT:", alert)

    print("-" * 40)
    time.sleep(2)

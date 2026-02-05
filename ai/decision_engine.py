import requests
import time
import json


def collect_ai_inputs():
    try:
        with open("ai/shared_state.json", "r") as f:
            data = json.load(f)
    except:
        data = {}

    passenger_count = data.get("passenger_count", 0)
    driver_status = data.get("driver_status", "UNKNOWN")

    ai_inputs = {
        "driver_status": driver_status,
        "attention_score": data.get("attention_score", 0),
        "passenger_count": passenger_count,
        "seat_vacancy": data.get("seat_vacancy", 0),
        "fire": data.get("fire_detected", False),
        "dangerous_driving": driver_status in [
            "DANGEROUS DRIVING ⚠️",
            "DRIVER DISTRACTED 📱"
        ],
        "overcrowded": data.get("overcrowded", passenger_count > 40),

        # ✅ LIVE VEHICLE DATA
        "overspeed": data.get("overspeed", False),
        "low_fuel": data.get("low_fuel", False),
        "engine_overheat": data.get("engine_overheat", False)
    }

    return ai_inputs

    


def send_to_backend(payload):
    try:
        requests.post(
            "http://127.0.0.1:5000/ai/status",
            json=payload,
            timeout=0.5
        )
    except:
        pass


def decision_engine(ai_inputs):
    actions = []

    if ai_inputs["fire"]:
        actions.append("EMERGENCY: Stop vehicle and evacuate passengers")

    if ai_inputs["dangerous_driving"]:
        actions.append("Alert driver and control center")

    if ai_inputs["overcrowded"]:
        actions.append("Restrict boarding and announce crowd alert")

    if ai_inputs["overspeed"]:
        actions.append("Issue speed warning to driver")

    if ai_inputs["low_fuel"]:
        actions.append("Schedule refueling at next depot")

    if ai_inputs["engine_overheat"]:
        actions.append("Reduce speed and inspect engine")

    return actions


if __name__ == "__main__":
    print("AI Decision Engine started...")

    while True:
        ai_inputs = collect_ai_inputs()

        decisions = decision_engine(ai_inputs)

        payload = {
            "driver_status": ai_inputs["driver_status"],
            "attention_score": ai_inputs["attention_score"],
            "passenger_count": ai_inputs["passenger_count"],
            "seat_vacancy": ai_inputs["seat_vacancy"],
            "fire_detected": ai_inputs["fire"],
            "dangerous_driving": ai_inputs["dangerous_driving"],
            "decisions": decisions
        }

        send_to_backend(payload)

        print("Sent AI status to backend:", payload)

        time.sleep(2)


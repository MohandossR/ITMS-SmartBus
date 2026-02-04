def check_speed_alert(vehicle, speed_limit=None):
    """
    If speed_limit is None, default to 60 km/h.
    You can override per vehicle in the future.
    """
    if speed_limit is None:
        speed_limit = 60

    if vehicle.speed > speed_limit:
        return {
            "alert": True,
            "type": "OVERSPEED",
            "message": f"Overspeed detected: {vehicle.speed} km/h (limit {speed_limit})"
        }

    return {
        "alert": False,
        "type": "NORMAL",
        "message": f"Speed within limit ({speed_limit} km/h)"
    }
def check_ai_alerts(ai_status):
    if ai_status.get("fire_detected"):
        return "FIRE EMERGENCY"
    if ai_status.get("dangerous_driving"):
        return "DANGEROUS DRIVING"
    return "NORMAL"

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
    # Simulated combined AI inputs
    inputs = {
        "fire": True,
        "dangerous_driving": False,
        "overcrowded": True,
        "overspeed": True,
        "low_fuel": False,
        "engine_overheat": False
    }

    decisions = decision_engine(inputs)

    for d in decisions:
        print("AI DECISION:", d)

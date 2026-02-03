import random
import time

def get_vehicle_state():
    speed = random.choice(["NORMAL", "OVERSPEED"])
    fuel = random.choice(["OK", "LOW"])
    engine_temp = random.choice(["NORMAL", "OVERHEAT"])
    brake = random.choice(["NORMAL", "EMERGENCY"])

    return {
        "speed": speed,
        "fuel": fuel,
        "engine_temp": engine_temp,
        "brake": brake
    }

def get_environment_state():
    traffic = random.choice(["LOW", "MEDIUM", "HIGH"])
    terrain = random.choice(["URBAN", "HIGHWAY", "SLOPE"])

    return {
        "traffic": traffic,
        "terrain": terrain
    }

if __name__ == "__main__":
    while True:
        vehicle = get_vehicle_state()
        environment = get_environment_state()

        print("VEHICLE STATE:", vehicle)
        print("ENVIRONMENT STATE:", environment)
        print("-" * 50)

        time.sleep(2)

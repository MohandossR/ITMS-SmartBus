<<<<<<< HEAD
from datetime import datetime

class Vehicle:
    def __init__(self, vehicle_id, speed, latitude, longitude):
        self.vehicle_id = vehicle_id
        self.speed = speed
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return {
            "vehicle_id": self.vehicle_id,
            "speed": self.speed,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "timestamp": self.timestamp
        }

# In-memory storage
vehicle_history = []
=======
from datetime import datetime

class Vehicle:
    def __init__(self, vehicle_id, speed, latitude, longitude):
        self.vehicle_id = vehicle_id
        self.speed = speed
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return {
            "vehicle_id": self.vehicle_id,
            "speed": self.speed,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "timestamp": self.timestamp
        }

# In-memory storage
vehicle_history = []
>>>>>>> frontend-dev

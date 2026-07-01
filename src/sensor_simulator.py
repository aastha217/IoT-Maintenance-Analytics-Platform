import random
from datetime import datetime

def generate_sensor_data(machine_id):
    return {
        "machine_id": machine_id,
        "temperature": round(random.uniform(60, 95), 2),
        "vibration": round(random.uniform(1, 10), 2),
        "power": round(random.uniform(300, 600), 2),
        "timestamp": datetime.now().isoformat()
    }

for i in range(10):
    machine_id = f"M{i:03d}"
    print(generate_sensor_data(machine_id))
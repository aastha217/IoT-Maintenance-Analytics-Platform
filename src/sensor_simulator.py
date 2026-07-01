import random
import time
from datetime import datetime

from anomaly_detector import detect_anomaly


def generate_sensor_data(machine_id):
    return {
        "machine_id": machine_id,
        "temperature": round(random.uniform(60, 95), 2),
        "vibration": round(random.uniform(1, 10), 2),
        "power": round(random.uniform(300, 600), 2),
        "timestamp": datetime.now().isoformat()
    }


while True:

    for i in range(10):

        machine_id = f"M{i:03d}"

        sensor_data = generate_sensor_data(machine_id)

        print(sensor_data)

        alerts = detect_anomaly(sensor_data)

        if alerts:
            print(f"ALERT for {machine_id}: {alerts}")

        print("-" * 50)

    time.sleep(1)
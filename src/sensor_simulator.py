import time
from datetime import datetime

from anomaly_detector import detect_anomaly
from data_storage import save_sensor_data
from machine import Machine


machines = [
    Machine(f"M{i:03d}")
    for i in range(10)
]


while True:

    for machine in machines:

        sensor_data = machine.generate_reading()

        sensor_data["timestamp"] = datetime.now().isoformat()

        save_sensor_data(sensor_data)

        print(sensor_data)

        alerts = detect_anomaly(sensor_data)

        if alerts:
            print(
                f"ALERT for {sensor_data['machine_id']}: {alerts}"
            )

        print("-" * 50)

    time.sleep(1)
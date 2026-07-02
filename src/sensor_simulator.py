import time
from datetime import datetime
from producer import send_sensor_data

from anomaly_detector import detect_anomaly
from data_storage import save_sensor_data
from machine import Machine
from maintenance_predictor import predict_maintenance_risk


machines = [
    Machine(f"M{i:03d}")
    for i in range(10)
]


while True:

    for machine in machines:

        sensor_data = machine.generate_reading()

        sensor_data["timestamp"] = datetime.now().isoformat()

        alerts = detect_anomaly(sensor_data)

        risk = predict_maintenance_risk(sensor_data)

        sensor_data["risk_level"] = risk

        send_sensor_data(sensor_data)

        print(sensor_data)

        if alerts:
            print(
                f"ALERT for {sensor_data['machine_id']}: {alerts}"
            )

        print(f"Maintenance Risk: {risk}")

        print("-" * 50)

    time.sleep(1)
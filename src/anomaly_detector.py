def detect_anomaly(sensor_data):

    alerts = []

    if sensor_data["temperature"] > 80:
        alerts.append("High Temperature")

    if sensor_data["vibration"] > 6:
        alerts.append("High Vibration")

    if sensor_data["health"] < 50:
        alerts.append("Machine Health Critical")

    return alerts
def detect_anomaly(sensor_data):

    alerts = []

    if sensor_data["temperature"] > 90:
        alerts.append("High Temperature")

    if sensor_data["vibration"] > 8:
        alerts.append("High Vibration")

    return alerts
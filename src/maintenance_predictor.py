def predict_maintenance_risk(sensor_data):

    health = sensor_data["health"]
    temperature = sensor_data["temperature"]
    vibration = sensor_data["vibration"]

    score = 0

    if health < 70:
        score += 1

    if health < 50:
        score += 1

    if temperature > 80:
        score += 1

    if vibration > 6:
        score += 1

    if score >= 3:
        return "HIGH"

    elif score >= 1:
        return "MEDIUM"

    return "LOW"
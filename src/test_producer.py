from producer import send_sensor_data


sample_data = {
    "machine_id": "M001",
    "temperature": 75,
    "vibration": 4,
    "power": 400
}

send_sensor_data(sample_data)

print("Message sent successfully")
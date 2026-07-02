import json

from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(
        x.decode("utf-8")
    )
)


print("Listening for sensor data...\n")

for message in consumer:

    sensor_data = message.value

    print(sensor_data)
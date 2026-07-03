import json

from kafka import KafkaConsumer
from influx_storage import save_to_influx
from data_storage import save_sensor_data


consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda x: json.loads(
        x.decode("utf-8")
    )
)


print("Listening for sensor data...\n")

for message in consumer:

    sensor_data = message.value

    save_sensor_data(sensor_data)

    save_to_influx(sensor_data)

    print("Received:", sensor_data)
import json

from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


def send_sensor_data(sensor_data):

    producer.send(
        "sensor-data",
        sensor_data
    )

    producer.flush()
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

TOKEN = "82LaBVCNTOrxgslrlxnL33-AGtoJQ4uSQ-7nN7Ootn7MG4UnM0XRnxyI6A2Jf-lwc5ml87bCnFqV14wpG_OuuQ=="
ORG = "IoTAnalytics"
BUCKET = "sensor_data"
URL = "http://localhost:8086"

client = InfluxDBClient(
    url=URL,
    token=TOKEN,
    org=ORG
)

write_api = client.write_api(
    write_options=SYNCHRONOUS
)


def save_to_influx(sensor_data):

    point = (
        Point("machine_metrics")
        .tag("machine_id", sensor_data["machine_id"])
        .field("temperature", float(sensor_data["temperature"]))
        .field("vibration", float(sensor_data["vibration"]))
        .field("power", float(sensor_data["power"]))
        .field("health", float(sensor_data["health"]))
        .time(sensor_data["timestamp"], WritePrecision.NS)
    )

    write_api.write(
        bucket=BUCKET,
        org=ORG,
        record=point
    )
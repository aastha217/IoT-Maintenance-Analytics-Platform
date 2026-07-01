import csv
import os


def save_sensor_data(sensor_data):

    file_exists = os.path.isfile("data/sensor_data.csv")

    with open("data/sensor_data.csv", mode="a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=sensor_data.keys()
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(sensor_data)
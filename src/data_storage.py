import csv
import os


def save_sensor_data(sensor_data):

    file_path = "data/sensor_data.csv"

    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=sensor_data.keys()
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(sensor_data)
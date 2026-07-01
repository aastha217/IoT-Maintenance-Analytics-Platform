import random


class Machine:

    def __init__(self, machine_id):

        self.machine_id = machine_id

        self.health = 100

    def generate_reading(self):

        degradation = (100 - self.health) / 10

        temperature = round(
            random.uniform(60, 75) + degradation,
            2
        )

        vibration = round(
            random.uniform(1, 4) + degradation / 2,
            2
        )

        power = round(
            random.uniform(300, 450) + degradation * 5,
            2
        )

        self.health -= random.uniform(0, 0.5)

        self.health = max(self.health, 0)

        return {
            "machine_id": self.machine_id,
            "health": round(self.health, 2),
            "temperature": temperature,
            "vibration": vibration,
            "power": power
        }
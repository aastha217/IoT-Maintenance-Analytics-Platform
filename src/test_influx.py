from influx_storage import save_to_influx
from datetime import datetime

sample = {
    "machine_id": "TEST001",
    "temperature": 75,
    "vibration": 3,
    "power": 400,
    "health": 95,
    "timestamp": datetime.now().isoformat()
}

save_to_influx(sample)

print("Data written successfully")
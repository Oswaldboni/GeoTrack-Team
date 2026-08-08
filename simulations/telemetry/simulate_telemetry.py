import json
import random
import time
from datetime import datetime, timezone

VEHICLE_COUNT = 100
INTERVAL_SECONDS = 5

def generate_vehicle_id(index):
    return f"VH-{index:06d}"

def generate_message(vehicle_id):
    return {
        "vehicle_id": vehicle_id,
        "latitude": round(random.uniform(45.0, 46.0), 6),
        "longitude": round(random.uniform(-74.0, -73.0), 6),
        "speed_kmh": round(random.uniform(0, 120), 1),
        "direction_deg": random.randint(0, 359),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": random.choice([
            "ACTIVE",
            "INACTIVE",
            "MAINTENANCE"
        ]),
        "diagnostic": {
            "engine": random.choice(["OK", "WARNING"]),
            "battery_percent": random.randint(20, 100),
            "error_code": None
        }
    }

def simulate():
    vehicles = [
        generate_vehicle_id(i)
        for i in range(1, VEHICLE_COUNT + 1)
    ]

    cycle = 1

    while True:
        start = time.time()

        messages = [
            generate_message(vehicle_id)
            for vehicle_id in vehicles
        ]

        for message in messages[:5]:
            print(json.dumps(message, ensure_ascii=False))

        elapsed = time.time() - start

        print(
            f"\nCycle {cycle} : "
            f"{len(messages)} messages générés "
            f"en {elapsed:.4f} seconde(s)\n"
        )

        cycle += 1

        sleep_time = max(
            0,
            INTERVAL_SECONDS - elapsed
        )
        time.sleep(sleep_time)

if __name__ == "__main__":
    simulate()

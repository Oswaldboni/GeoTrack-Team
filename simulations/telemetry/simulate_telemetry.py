import argparse
import json
import random
import time
from datetime import datetime, timezone


def generate_vehicle_id(index: int) -> str:
    return f"VH-{index:06d}"


def generate_message(vehicle_id: str) -> dict:
    return {
        "vehicle_id": vehicle_id,
        "latitude": round(random.uniform(45.0, 46.0), 6),
        "longitude": round(random.uniform(-74.0, -73.0), 6),
        "speed_kmh": round(random.uniform(0, 120), 1),
        "direction_deg": random.randint(0, 359),
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
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


def simulate(
    vehicle_count: int,
    interval_seconds: float,
    cycles: int,
    sample_size: int,
) -> None:
    vehicles = [
        generate_vehicle_id(i)
        for i in range(1, vehicle_count + 1)
    ]

    cycle = 1

    while cycles == 0 or cycle <= cycles:
        start = time.perf_counter()

        messages = [
            generate_message(vehicle_id)
            for vehicle_id in vehicles
        ]

        for message in messages[:sample_size]:
            print(json.dumps(message, ensure_ascii=False))

        elapsed = time.perf_counter() - start

        print(
            f"\nCycle {cycle} : "
            f"{len(messages)} messages générés "
            f"en {elapsed:.4f} seconde(s)\n"
        )

        if cycles == 0 or cycle < cycles:
            time.sleep(max(0, interval_seconds - elapsed))

        cycle += 1


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("la valeur doit être supérieure à 0")
    return parsed


def non_negative_int(value: str) -> int:
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("la valeur doit être positive ou nulle")
    return parsed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Génère des messages de télémétrie GeoTrack."
    )
    parser.add_argument("--vehicles", type=positive_int, default=100)
    parser.add_argument("--interval", type=float, default=5.0)
    parser.add_argument(
        "--cycles",
        type=non_negative_int,
        default=1,
        help="nombre de cycles ; 0 exécute la simulation en continu",
    )
    parser.add_argument("--sample-size", type=non_negative_int, default=5)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()

    if args.interval < 0:
        parser.error("--interval doit être positif ou nul")

    return args


if __name__ == "__main__":
    arguments = parse_args()
    if arguments.seed is not None:
        random.seed(arguments.seed)
    simulate(
        vehicle_count=arguments.vehicles,
        interval_seconds=arguments.interval,
        cycles=arguments.cycles,
        sample_size=arguments.sample_size,
    )

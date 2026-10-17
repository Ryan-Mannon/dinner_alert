import subprocess

from datetime import datetime
from time import monotonic, sleep

BEDROOMS = ["Bedroom 1", "Bedroom 2", "Bedroom 3"]
COOLDOWN_SECONDS = 3


def announce(room: str, message: str) -> None:
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {room}: {message}")
    subprocess.run(["say", "Dinner is ready!"], check=True)


def notify_house(message: str) -> None:
    print("\nSending announcement...")
    for room in BEDROOMS:
        announce(room, message)


def main() -> None:
    print("Dinner Alert System")
    print("Press Enter to announce, or type q to quit.")

    last_announcement = float("-inf")

    while True:
        command = input("> ")

        if command.lower() == "q":
            print("Shutting down.")
            break

        now = monotonic()
        if now - last_announcement < COOLDOWN_SECONDS:
            print("Please wait before sending another announcement.")
            continue

        last_announcement = now
        notify_house("Dinner is ready!")


if __name__ == "__main__":
    main()

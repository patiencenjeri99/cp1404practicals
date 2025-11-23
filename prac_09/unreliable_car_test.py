"""
CP1404/CP5632 Practical
Test UnreliableCar
"""

from unreliable_car import UnreliableCar


def main():
    """Test driving an UnreliableCar many times."""
    unreliable_car = UnreliableCar("Unreliable", 100, 30)

    drives = 0
    attempts = 100

    for i in range(attempts):
        distance = unreliable_car.drive(1)
        if distance > 0:
            drives += 1

    print(f"Attempted to drive {attempts} times.")
    print(f"Car successfully drove {drives} times.")

    # Basic sanity checks (not strict pass/fail)
    assert 0 < drives < attempts, "Car reliability logic seems incorrect."


main()

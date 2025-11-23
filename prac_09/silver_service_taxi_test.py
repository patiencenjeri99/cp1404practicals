"""
CP1404 Practical9
Test SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi functionality."""
    taxi = SilverServiceTaxi("Hummer", 200, 2)  # fanciness 2

    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()

    print(f"Taxi details: {taxi}")
    print(f"Fare for 18km trip: ${fare:.2f}")

    # Assert expected fare (prac says 48.78)
    assert abs(fare - 48.78) < 0.1, "Fare calculation is incorrect"


main()

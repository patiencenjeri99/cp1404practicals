"""
CP1404 Practical9
Test Taxi class
"""

from taxi import Taxi


def main():
    """Test the Taxi class."""
    # Create a taxi: name="Prius 1", fuel=100
    my_taxi = Taxi("Prius 1", 100)

    # Drive 40 km
    my_taxi.drive(40)
    print(f"{my_taxi}, fare=${my_taxi.get_fare():.2f}")

    # Restart the fare and drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, fare=${my_taxi.get_fare():.2f}")


main()

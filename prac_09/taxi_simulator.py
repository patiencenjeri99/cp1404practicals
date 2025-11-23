"""
CP1404 Practical9
Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Run the Taxi Simulator program."""
    print("Let's drive!")

    # Create taxis list
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    bill_to_date = 0.0
    current_taxi = None

    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            # Choose taxi
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = input("Choose taxi: ")

            if not taxi_choice.isdigit():
                print("Invalid taxi choice")
            else:
                taxi_index = int(taxi_choice)
                if 0 <= taxi_index < len(taxis):
                    current_taxi = taxis[taxi_index]
                else:
                    print("Invalid taxi choice")

        elif choice == "d":
            # Drive the chosen taxi
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                bill_to_date += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display each taxi with index."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

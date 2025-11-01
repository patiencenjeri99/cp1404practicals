"""
CP1404 Practical - Used_cars modified
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

print()
#create a new car object called Toyota
Toyota = Car("Toyota", 100)
Toyota.add_fuel(20)
print(f"Added fuel. {Toyota.name} now has fuel: {Toyota.fuel}")
Toyota.drive(100)
print(Toyota)


main()
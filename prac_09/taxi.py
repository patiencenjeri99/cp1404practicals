"""
CP1404 Practical9
Taxi class, inherits from Car
"""
from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23    # CLASS VARIABLE

    def __init__(self, name, fuel):
        """Initialise a Taxi instance."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0   # instance variable

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km")

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

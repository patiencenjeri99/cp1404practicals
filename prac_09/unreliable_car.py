"""
CP1404 Practical
UnreliableCar class, inherits from Car
"""

import random
from car import Car


class UnreliableCar(Car):
    """Specialised Car that sometimes does not drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability  # 0–100 chance of driving

    def drive(self, distance):
        """Drive only if random number < reliability.
        Always return distance actually driven.
        """
        random_number = random.uniform(0, 100)

        if random_number < self.reliability:
            # Car drives normally
            return super().drive(distance)
        else:
            # Car fails to drive
            return 0

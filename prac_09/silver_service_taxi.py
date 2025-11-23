"""
CP1404 Practical9
SilverServiceTaxi class, inherits from Taxi
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness and flagfall."""

    flagfall = 4.50  # CLASS VARIABLE

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness

        # Adjust the instance's price_per_km using fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the fare including flagfall."""
        base_fare = super().get_fare()
        return base_fare + self.flagfall

    def __str__(self):
        """Return a string representation including flagfall and fancy price."""
        return (f"{super().__str__()} plus flagfall of "
                f"${self.flagfall:.2f}")

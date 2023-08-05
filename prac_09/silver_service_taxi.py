"""
CP1404/CP5632 Practical
Silver Service Taxi Class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent SilverServiceTaxi object."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """String representation of SilverServiceTaxi object."""
        return f"{super().__str__()} plus flagfall of {self.flagfall}"

    def get_fare(self):
        """Retrieve new fare with flagfall"""
        return round((self.flagfall + super().get_fare()) * 10) / 10

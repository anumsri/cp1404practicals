"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive Car if number is less than reliability"""
        random_number = random.randint(0, 100)
        if random_number > self.reliability:
            drive_distance = 0
        else:
            drive_distance = distance
        actual_distance = super().drive(drive_distance)
        return actual_distance


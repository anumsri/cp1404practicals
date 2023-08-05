"""
CP1404/CP5632 Practical
Silver service taxi testing
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Silver Taxi", 60, 4)
    my_taxi.drive(20)
    print(my_taxi)
    # print(my_taxi.get_fare())
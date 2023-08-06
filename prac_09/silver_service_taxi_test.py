"""
CP1404/CP5632 Practical
Silver service taxi testing
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Silver Taxi", 100, 2)
    my_taxi.drive(18)
    print(my_taxi.get_fare())
    print(my_taxi)

main()
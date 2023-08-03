"""
CP1404 Arpisitt Numsri
Testing for taxi class
"""

from taxi import Taxi


def main():
    """Testing for Taxi Class"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()

"""
Taxi Simulator for CP1404
Arpisitt Numsri
"""
from prac_06.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi Simulator main program"""
    taxi_list = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
                 SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    current_taxi = None
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis Available")
            display_taxis(taxi_list)
        elif choice == "d":
            current_taxi.start_fare()
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()


def display_taxis(taxi_list):
    """Display taxi list nicely"""
    for i, taxi in enumerate(taxi_list):
        print(f"{i} - {taxi}")



main()

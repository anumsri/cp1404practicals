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
    total_cost = 0
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis Available")
            display_taxis(taxi_list)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxi_list[taxi_choice]
            except IndexError:
                print("Invalid choice")
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                cost = current_taxi.start_fare()
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                total_cost += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()


def display_taxis(taxi_list):
    """Display taxi list nicely"""
    for i, taxi in enumerate(taxi_list):
        print(f"{i} - {taxi}")



main()

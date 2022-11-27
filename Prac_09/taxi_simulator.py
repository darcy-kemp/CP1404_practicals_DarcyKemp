"""Cp1404 Darcy Kemp taxi simulator.
Program to simulate the use of taxis for a user."""
from Prac_09.taxi import Taxi
from Prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's Drive!")
    print(MENU)
    user_menu_choice = input(">>>").lower()
    current_cost = 0
    while user_menu_choice != 'q':

        if user_menu_choice == 'c':
            # Error handling for index error. Did not include Value error as it was not shown in the sample.
            display_taxis(taxis)
            try:
                current_taxi = taxis[int(input("Choose taxi: "))]
            except IndexError:
                print("Invalid taxi choice")
            print(f"Bill to date: ${current_cost:.2f}")
            print(MENU)
            user_menu_choice = input(">>>").lower()

        elif user_menu_choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive.")
            else:
                current_taxi.start_fare()
                current_taxi.drive(int(input("Drive how far? ")))
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                current_cost += current_taxi.get_fare()
            print(f"Bill to date: ${current_cost:.2f}")
            print(MENU)
            user_menu_choice = input(">>>").lower()
        else:
            print('Invalid option')
            user_menu_choice = input('>>>').lower()
    print(f"Total trip cost: ${current_cost:.2f}")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()

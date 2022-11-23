"""Cp1404 Darcy Kemp taxi simulator.
Program to simulate the use of taxis for a user."""
from Prac_09.taxi import Taxi
from Prac_09.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print(MENU)
    user_menu_choice = input(">>>").lower()
    while user_menu_choice == 'q':
        if user_menu_choice == 'c':
            print('a')
        elif user_menu_choice == 'd':
            print('a')
        else:
            print('invalid menu choice')
            user_menu_choice = input('>>>')

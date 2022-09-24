"""CP1404 | prac_02 Temperatures | Darcy Kemp
Program to convert Celsius and Fahrenheit using functions
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":

        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit))

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit(fahrenheit)
            print(f"Result: {celsius:.2f}C")

        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit(fahrenheit):

    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


def convert_celsius(celsius):

    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()

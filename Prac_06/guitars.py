"""CP1404 | prac_06 guitars| Darcy Kemp
program to create guitar objects from user input and append them to a list

I have no idea where to put the estimation, I will put it here.

est: 40
real: 45
"""
from Prac_06.guitar import Guitar

guitars = []

guitar_name = "-1"

while guitar_name != "":
    guitar_name = input("name: ")
    if guitar_name != "":
        guitar_year = int(input("year: "))
        guitar_cost = int(input("cost: "))

        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
i = 0
for guitar in guitars:
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
    i += 1

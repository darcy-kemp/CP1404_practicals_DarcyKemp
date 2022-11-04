"""CP1404 | prac_06 guitar_test| Darcy Kemp
program to create guitar objects from user input and append them to a list
"""

from Prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(f"expected True")
print(f"result: {gibson.is_vintage()}")

print("expected: 100")
print(f"real: {gibson.get_age()}")

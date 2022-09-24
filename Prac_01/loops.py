"""
CP1404 | prac_01 Counting Loops | Darcy Kemp
Program to print a range
"""

for i in range(1, (20+1), 2):
    print(i, end=' ')
print()

for i in range(0, (100+1), 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Number of Stars: "))

for i in range(number_of_stars):
    print("*", end='')

for i in range(number_of_stars + 1):
    print(i * '*')
print()


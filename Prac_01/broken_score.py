"""
CP1404 | prac_01 Broken Score | Darcy Kemp
Broken program to determine score status
"""



score = float(input("Enter score: "))
if score < 0 or 100 < score:
    print("Invalid Score")
elif score < 50:
    print("Fail")
elif score < 90:
    print("passable")
else:
    print("excellent")

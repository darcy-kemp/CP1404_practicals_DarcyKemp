"""CP1404 | prac_05 State Names | Darcy Kemp
State names in a dictionary
"""

# Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
codes = CODE_TO_NAME.keys()
names = CODE_TO_NAME.values()

for key in CODE_TO_NAME:
    print(f"{key:3} is {CODE_TO_NAME[key]}")

state_code = input("Enter short state: ").upper()
while state_code != "":

    try:
        print(state_code, "is", CODE_TO_NAME[state_code])

    except KeyError:
        print("Invalid short state")

    state_code = input("Enter short state: ").upper()

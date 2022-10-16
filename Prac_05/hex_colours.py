"""CP1404 | prac_05 hex colours | Darcy Kemp
program to return hex codes of colours in a dictionary
"""
HEX_VALUE_TO_COLOUR = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALICE BLUE": "#f0f8ff",
                       "ALIZARIN CRIMSON": "#e32636", "AMARANTH": "#e52b50",
                       "AMBER": "#ffbf00", "AMETHYST": "#9966cc", "AQUA": "#00ffff",
                       "AUREOLIN": "#fdee00", "BABY BLUE": "#89cff0"}

colour_name = input("Enter colour name: ").upper()
while colour_name != "":

    try:
        print(colour_name, "is", HEX_VALUE_TO_COLOUR[colour_name])

    except KeyError:
        print("Invalid colour name")

    colour_name = input("Enter colour name: ").upper()
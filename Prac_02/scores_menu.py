"""
CP1404 | prac_02 Scores Menu | Darcy Kemp
Program to determine score status using functions and print equal stars
"""
MENU = """R - run score calculation program
Q - Quit"""


def main():
    print(MENU)
    user_selection = input(">>>").upper()

    while user_selection != "Q":
        score = float(input("Enter score: "))

        while score < 0 or score > 100:
            score = float(input("Please enter valid score(0-100): "))

        score_bracket = determine_score(score)
        print(score_bracket)
        print("*" * int(score))


def determine_score(score):
    if score < 0 or 100 < score:
        score_bracket = "Invalid Score"
    elif score < 50:
        score_bracket = "Fail"
    elif score < 90:
        score_bracket = "passable"
    else:
        score_bracket = "excellent"
    return score_bracket


main()

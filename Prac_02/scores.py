"""
CP1404 | prac_02 Scores | Darcy Kemp
Program to determine score status using functions
"""


def main():
    score = float(input("Enter score: "))
    score_bracket = determine_score(score)
    print(score_bracket)


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

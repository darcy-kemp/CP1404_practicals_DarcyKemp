"""CP1404 | prac_02 Password Stars | Darcy Kemp
Program to return a number of stars equal to user input
"""

MIN_PW_LENGTH = 6


def main():
    user_pw = get_password()

    print_stars(user_pw)


def print_stars(password):
    print('*' * len(password))


def get_password():
    user_pw = input("please input a password: ")
    while len(user_pw) < MIN_PW_LENGTH:
        user_pw = input("please enter a valid password: ")
    return user_pw


main()

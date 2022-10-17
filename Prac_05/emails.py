"""CP1404 | prac_05 emails | Darcy Kemp
program to pair user_names extrapolated from an email with the email in a dictionary
est:30
real:42
"""
user_name_to_user_email = {}

user_email = input("Email: ")

while user_email != "":
    try:
        user_name = user_email.split("@")
        del(user_name[-1])
        user_name = user_name[0].split(".")
        user_name_formatted = " ".join(user_name).title()

        user_name_is_correct = input(f"Is {user_name_formatted} your name?: [y/n]").lower()
        if user_name_is_correct != "y" and user_name_is_correct != "":
            user_name_formatted = input("Name: ").title()

        user_name_to_user_email[user_name_formatted] = user_email
        user_email = input("Email: ")
    except IndexError:
        print("Invalid email. Must contain an @ symbol.")
        user_email = input("Email: ")

for key in user_name_to_user_email:
    print(f"{key} ({user_name_to_user_email[key]})")

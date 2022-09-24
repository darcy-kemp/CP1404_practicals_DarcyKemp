"""
CP1404 | prac_01 menus | Darcy Kemp
program to demonstrate menus
"""

menu = """(H)ello
(G)oodbye
(Q)uit"""

user_name = input("Enter Name: ")
print(menu)

user_choice = input(">>>").lower()

while user_choice != "q":
    if user_choice == "h":
        print(f"Hello {user_name}")

    elif user_choice == "g":
        print(f"Goodbye {user_name}")

    else:
        print("Invalid Selection")

    print(menu)
    user_choice = input(">>>").lower()

print("Finished.")

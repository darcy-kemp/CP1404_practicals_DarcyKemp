"""CP1404 | prac_07 project management| Darcy Kemp

Estimate: 60min
Real:
"""

from Prac_07.project import Project
import datetime
MENU = """(L)oad Projects 
(S)ave Projects 
(D)isplay Projects 
(F)ilter by date
(A)dd new project
(U)pdate a project 
(Q)uit program"""
VALID_MENU_CHOICE = ["L", "S", "D", "F", "A", "U", "Q"]


def get_menu_choice():
    print(MENU)
    user_choice = input(">>>").upper()
    while user_choice not in VALID_MENU_CHOICE:
        print("Please enter a valid menu choice.")
        user_choice = input(">>>").upper()
    return user_choice


def load_projects():
    name_of_file = input("File name:")
    projects = []
    with open(name_of_file, "r") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost = float(parts[3])
            completion_percent = int(parts[4])
            projects.append(Project(name, date, priority, cost, completion_percent))

    return projects


def save_projects(projects):
    file_name = input("File name: ")
    with open(file_name, "w") as out_file:
        for line in projects:
            print(f"{line}", file=out_file)


def add_new_project(projects):
    name = input("name: ")
    date = input("date (in d/m/y format): ")
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    priority = int(input("priority level: "))
    cost = float(input("Estimated cost: "))
    completion_percent = int(input("Completion percentage: "))
    projects.append(Project(name, date, priority, cost, completion_percent))
    return projects


def update_project(projects):
    project_number = int(input("project number: "))
    new_priority = input("New priority level: ")
    new_completion = input("New completion level(%): ")
    projects[project_number - 1].priority = new_priority
    projects[project_number - 1].completion = new_completion
    return projects


def main():
    user_menu_choice = get_menu_choice()
    projects = []
    while user_menu_choice != "Q":
        if user_menu_choice == "L":
            projects = load_projects()
            user_menu_choice = get_menu_choice()
        elif user_menu_choice == "S":
            save_projects(projects)
            user_menu_choice = get_menu_choice()
        elif user_menu_choice == "D":
            print("test")
            user_menu_choice = get_menu_choice()
        elif user_menu_choice == "F":
            print("test")
            user_menu_choice = get_menu_choice()
        elif user_menu_choice == "A":
            projects = add_new_project(projects)
            user_menu_choice = get_menu_choice()
        elif user_menu_choice == "U":
            projects = update_project(projects)
            user_menu_choice = get_menu_choice()


main()



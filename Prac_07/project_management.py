"""CP1404 | prac_07 project management| Darcy Kemp

Estimate: 60min
Real: 300 mins
"""

from Prac_07.project import Project
import datetime
from operator import attrgetter
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
            date = parts[1]
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
    date = input("date (in dd/mm/yyyy format): ")
    priority = int(input("priority level: "))
    cost = float(input("Estimated cost: "))
    completion_percent = int(input("Completion percentage: "))
    projects.append(Project(name, date, priority, cost, completion_percent))
    projects.sort()
    return projects


def update_project(projects):
    i = 0
    for project in projects:
        print(f"{i} {project}")
        i += 1
    project_number = int(input("project number to update: "))
    new_priority = int(input("New priority level: "))
    new_completion = int(input("New completion level(%): "))
    projects[project_number].priority = new_priority
    projects[project_number].completion = new_completion
    projects.sort()
    return projects


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion != 100]
    completed_projects = [project for project in projects if project.completion == 100]
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed Projects:")
    for project in completed_projects:
        print(project)


def filter_projects_by_date(projects):
    cutoff_date = input("show projects that start after date (dd/mm/yyyy:) ")
    cutoff_date = datetime.datetime.strptime(cutoff_date, "%d/%m/%Y").date()
    projects.sort(key=attrgetter('date'))
    for project in projects:
        if project.is_after_date(cutoff_date):
            print(project)


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
            display_projects(projects)
            user_menu_choice = get_menu_choice()
        elif user_menu_choice == "F":
            filter_projects_by_date(projects)
            user_menu_choice = get_menu_choice()
        elif user_menu_choice == "A":
            projects = add_new_project(projects)
            user_menu_choice = get_menu_choice()
        elif user_menu_choice == "U":
            projects = update_project(projects)
            user_menu_choice = get_menu_choice()


main()

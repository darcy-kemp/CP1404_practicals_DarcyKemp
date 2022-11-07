"""CP1404 | prac_07 my guitars| Darcy Kemp
program to create guitar objects from a read file
"""

from Prac_06.guitar import Guitar
NAME_OF_FILE = "guitars.csv"


def main():
    guitars = []
    with open(NAME_OF_FILE, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))

    while True:
        guitar_name = input("name: ")
        if guitar_name == "":
            break
        guitar_year = int(input("year: "))
        guitar_cost = int(input("cost: "))

        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    guitars.sort()
    print(guitars)

    with open(NAME_OF_FILE, "w") as out_file:
        for line in guitars:
            print(f"{line}", file=out_file)


if __name__ == '__main__':
    main()

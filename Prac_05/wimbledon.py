"""CP1404 | prac_05 wimbledon | Darcy Kemp
program to pair user_names extrapolated from an email with the email in a dictionary
est:30
real:30
"""
FILE_NAME = "wimbledon.csv"
CHAMPION_INDEX = 2
COUNTRY_INDEX = 1


def read_file(name_of_file):
    with open(name_of_file, "r", encoding="utf-8-sig") as in_file:
        wimbledon_data = []
        next(in_file)
        for line in in_file:
            wimbledon_data.append(line.split(","))
    return wimbledon_data


def process_data(data, country_index, champion_index):
    countries = set()
    champion_to_victories = {}
    for entry in data:
        champion_to_victories[entry[champion_index]] = champion_to_victories.get(entry[champion_index], 0) + 1
        countries.add(entry[country_index])
    return champion_to_victories, countries


def print_processed_data(champion_to_victories, countries):
    print("Wimbledon champions:")
    for key in champion_to_victories:
        print(f"{key} won {champion_to_victories[key]} times.")

    print(f"\nThese {len(countries)} countries have won wimbledon:")
    countries = ", ".join(sorted(countries))
    print(f"{countries}")


def main(file_name, country_index, champion_index):

    wimbledon_data = read_file(file_name)

    champion_to_number_of_wins, countries_won_wimbledon = process_data(wimbledon_data, country_index, champion_index)

    print_processed_data(champion_to_number_of_wins, countries_won_wimbledon)


main(FILE_NAME, COUNTRY_INDEX, CHAMPION_INDEX)

"""CP1404 | prac_05 wimbledon | Darcy Kemp
program to pair user_names extrapolated from an email with the email in a dictionary
est:30
real:30
"""
FILE_NAME = "wimbledon.csv"
champion_to_number_of_wins = {}
countries_that_won_wimbledon = []

with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
    next(in_file)
    for line in in_file:
        current_data_line = line.split(",")
        champion_to_number_of_wins[current_data_line[2]] = champion_to_number_of_wins.get(current_data_line[2], 0) + 1
        country = current_data_line[1]

        if country not in countries_that_won_wimbledon:
            countries_that_won_wimbledon.append(country)

print("Wimbledon champions:")
for key in champion_to_number_of_wins:
    print(f"{key} is {champion_to_number_of_wins[key]}")

print(f"\nThese {len(countries_that_won_wimbledon)} countries have won wimbledon:")
countries_that_won_wimbledon = ", ".join(countries_that_won_wimbledon)
print(f"{countries_that_won_wimbledon}")

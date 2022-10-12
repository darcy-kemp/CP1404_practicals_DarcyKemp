"""CP1404 | prac_04 list comprehension | Darcy Kemp
User selects how many "picks" then multiple random number lines are returned
"""
import random
LOWER_RANDOM_BOUNDARY = 1
UPPER_RANDOM_BOUNDARY = 45


def main():

    number_of_picks = int(input("How many picks?: "))

    for i in range(1, number_of_picks + 1, 1):
        random_lottery_pick = []

        for j in range(6):
            current_random_int = random.randint(LOWER_RANDOM_BOUNDARY,UPPER_RANDOM_BOUNDARY)

            while current_random_int in random_lottery_pick:
                current_random_int = random.randint(LOWER_RANDOM_BOUNDARY, UPPER_RANDOM_BOUNDARY)

            random_lottery_pick.append(current_random_int)

        print(f"Pick number {i} is: {random_lottery_pick}")

main()

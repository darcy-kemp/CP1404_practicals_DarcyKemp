"""CP1404 | prac_04 lists warmup | Darcy Kemp
List simple questions and tasks
"""
numbers = [3, 1, 4, 1, 5, 9, 2]
#3
#2
#1
#[3, 1, 4, 1, 5, 9]
#[1]
#True
#False
#False
#[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
numbers[-1] = 1

numbers.reverse()
numbers = numbers[:-2]
numbers.reverse()

print(f"{numbers}")

if 9 in numbers:
    print("9 is in numbers")
else:
    print("9 is not in numbers")

"""CP1404 | prac_03 exceptions to complete | Darcy Kemp
experimenting with try-catch statements
"""


is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)

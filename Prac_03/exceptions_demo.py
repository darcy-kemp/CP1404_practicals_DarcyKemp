"""CP1404 | prac_03 exceptions | Darcy Kemp
experimenting with try-catch statements
"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        denominator = 1
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# A value error will occur if any of the inputs are not integers

# A ZeroDivisionError will occur if the denominator input is 0

# There are multiple ways to avoid the zero division error. One is to implement an if statement that checks if the
# denominator is 0 then forces it to be 1.

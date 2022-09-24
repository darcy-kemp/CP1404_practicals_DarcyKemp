"""CP1404 | prac_01 Sales_Bonus | Darcy Kemp
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Sales: $"))

while sales != 0:

    if sales < 1000:
        bonus = 0.1 * sales
    else:
        bonus = 0.15 * sales

    print(f"Bonus is: ${bonus}")
    sales = float(input("Sales: $"))
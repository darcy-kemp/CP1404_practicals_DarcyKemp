"""
CP1404 | prac_01 Shop Calculator | Darcy Kemp
Program to add inputs and discount if total greater than a set amount
"""
number_of_items = int(input("Number of Items: "))
total_price = 0

while number_of_items < 0:
    print("Invalid Number of Items")
    number_of_items = int(input("Number of Items: "))

for i in range(number_of_items):
    price_of_item = float(input("Price of Item: $"))
    total_price += price_of_item

if total_price >= 100:
    total_price = total_price * 0.9

print(f"Total Price Is: ${total_price}")

"""
CP1404/CP5632 - Practical
Small shop calculator program
"""

total_price = 0
number_of_items = int(input("Number of Items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of Items: "))
for i in range(number_of_items):
    price_of_items = float(input("Price of Item: "))
    total_price += price_of_items

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number_of_items} items is {total_price:.2f}")
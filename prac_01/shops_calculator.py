# Get the number of items and ensure it's a valid number
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# get the total price
total_price = 0

# Loop to get the price of each item
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply a 10% discount if the total is over $100
if total_price > 100:
    total_price *= 0.9

# Display the total price formatted to 2 decimal places
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
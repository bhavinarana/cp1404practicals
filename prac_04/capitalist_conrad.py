"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 17.5%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $100, or falls below $1.00, the program should end.
The price should be displayed to the nearest cent (e.g., $33.59, not $33.5918232901).
"""

import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0       # Minimum price before stopping the simulation
MAX_PRICE = 100.0     # Maximum price before stopping the simulation
INITIAL_PRICE = 10.0  # Initial starting price of the stock
FILENAME = "stock_output.txt"  # Output filename to write results

# Start price
price = INITIAL_PRICE
number_of_days = 0  # Counter to track the number of days

# Open the file for writing
out_file = open(FILENAME, 'w')

# Write the starting price
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate stock price changes day by day
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0

    # Determine whether the price increases or decreases
    if random.randint(1, 2) == 1:
        # Price increases: random value between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Price decreases: random value between -MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Calculate the new price based on the percentage change
    price *= (1 + price_change)
    number_of_days += 1  # Increment day count

    # Write the result of the day to the file
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file after the simulation ends
out_file.close()
"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""

# Get the first sales input
sales = float(input("Enter sales: $"))

# Continue asking for sales until a negative value is entered
while sales >= 0:
    # Calculate the bonus based on the sales amount
    if sales >= 1000:
        bonus = sales * 0.15
    else:
        bonus = sales * 0.10

    # Print the calculated bonus
    print(f"Bonus: ${bonus:.2f}")
    
    # Get the next sales input
    sales = float(input("Enter sales: $"))

print("Negative sales entered. Program terminated.")
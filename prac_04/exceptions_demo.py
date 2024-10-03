# Answering the questions in comments:
# 1. A `ValueError` will occur when the user enters a non-integer value for either the numerator or denominator.
# 2. A `ZeroDivisionError` will occur when the user enters 0 as the denominator.
# 3. To avoid the possibility of a `ZeroDivisionError`, we can check if the denominator is zero before performing the division.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    # Check to avoid ZeroDivisionError
    while denominator == 0:
        print("Denominator cannot be zero. Please enter a valid number.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
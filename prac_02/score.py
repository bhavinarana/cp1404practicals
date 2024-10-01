"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

# Function to determine the result based on score
def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# Get the score from the user
user_score = float(input("Enter score: "))


user_result = determine_result(user_score)
print(user_result)

# Generate a random score between 0 and 100
random_score = random.uniform(0, 100)
random_result = determine_result(random_score)
print(f"Random score: {random_score:.2f}, Result: {random_result}")
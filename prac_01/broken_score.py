"""
CP1404/CP5632 - Practical
Program to determine score status
"""

# Get the score from the user
score = float(input("Enter score: "))

# Check the score and print the appropriate message
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
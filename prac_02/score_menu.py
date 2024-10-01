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


# Function to get a valid score between 0 and 100
def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


# Function to show stars equal to the score
def show_stars(score):
    stars = '*' * int(score)
    print(stars)


# Main function
def main():
    # Get an initial valid score
    score = get_valid_score()

    # Display menu and get the user's choice
    menu = """Menu:
    (G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit"""
    print(menu)

    choice = input("Enter your choice: ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice! Please choose from the menu.")

        # Display menu again and get new choice
        print(menu)
        choice = input("Enter your choice: ").upper()

    # Farewell message when quitting
    print("Farewell!")



if __name__ == "__main__":
    main()
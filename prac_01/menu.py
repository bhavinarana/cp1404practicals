# Get the user's name
name = input("Enter name: ")

# Display the menu options
menu = "(H)ello\n(G)oodbye\n(Q)uit"

# Display the menu and get the initial choice
print(menu)
choice = input(">>> ").upper()  # Convert input to uppercase to handle both lower and uppercase inputs

# Loop until the user chooses 'Q' (Quit)
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Display the menu again and get a new choice
    print(menu)
    choice = input(">>> ").upper()

# Final message after the user quits
print("Finished.")

main():
# Define the minimum length as a local variable
min_length = 9

# Get the password from the user
password = get_password(min_length)

# Print stars corresponding to the password length
print_stars(password)


def get_password(min_length):
    password = input("Enter your password: ")
    # Check if the password meets the minimum length
    if len(password) >= min_length:
        return password
    else:
        print(f"Password must be at least {min_length} characters long.")
        return get_password(min_length)


def print_stars(password):

    print('*' * len(password))


main()

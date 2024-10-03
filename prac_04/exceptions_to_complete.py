is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # TODO: this line - set `is_finished` to True when a valid integer is entered
    except ValueError:  # TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", result)

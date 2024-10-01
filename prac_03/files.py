# Question 1: Write name to file
def write_name_to_file():
    name = input("Enter your name: ")
    with open("name.txt", 'w') as file:
        file.write(name)


# Question 2: Read name from file and print greeting
def read_name_from_file_and_greet():
    with open("name.txt", 'r') as file:
        name = file.read().strip()  e
    print(f"Hi {name}!")


# Question 3: Read first two numbers and print their sum
def sum_first_two_numbers():
    with open("numbers.txt", 'r') as file:
        first_number = int(file.readline().strip())
        second_number = int(file.readline().strip())
    print(f"The sum of the first two numbers is: {first_number + second_number}")


# Question 4: Sum all numbers in the file
def sum_all_numbers():
    total = 0
    with open("numbers.txt", 'r') as file:
        for line in file:
            total += int(line.strip())
    print(f"The total sum of all numbers is: {total}")


# Run each function in sequence to test
if __name__ == "__main__":
    print("Testing Question 1: Write Name to File")
    write_name_to_file()

    print("\nTesting Question 2: Read Name from File and Greet")
    read_name_from_file_and_greet()

    print("\nTesting Question 3: Sum First Two Numbers")
    sum_first_two_numbers()


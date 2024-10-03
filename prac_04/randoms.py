import random

# Line 1: Generate a random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))  # line 1
# Smallest number: 5
# Largest number: 20

# Line 2: Generate a random odd integer between 3 and 9 (inclusive), step 2
print(random.randrange(3, 10, 2))  # line 2
# Smallest number: 3
# Largest number: 9
# Could it produce a 4? No, because it steps by 2 from 3: 3, 5, 7, 9

# Line 3: Generate a random float between 2.5 and 5.5 (inclusive of lower bound but not upper)
print(random.uniform(2.5, 5.5))  # line 3
# Smallest number: 2.5
# Largest number: 5.5

# Code to produce a random number between 1 and 100 (inclusive)
print(random.randint(1, 100))  # Generates a random integer between 1 and 100
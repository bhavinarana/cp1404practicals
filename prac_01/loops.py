# a. Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()  # Newline after the loop

# b. Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()  # Newline after the loop

# c. Print n stars on one line
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()  # Newline after the stars

# d. Print n lines of increasing stars
for i in range(1, n + 1):
    print('*' * i)
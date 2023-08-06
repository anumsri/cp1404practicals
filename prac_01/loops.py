"""
CP1404/CP5632 - Practical
For Loops
"""
# a
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# b
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# c
for i in range(20, 1, -1):
    print(i, end=' ')
print()

# d
number = int(input("Number of stars: "))
print("*" * number)

# c.
number = int(input("Number of stars: "))
for i in range(number):
    print('*', end= '')

# d.
number = int(input("Number of stars: "))
for i in range(1, number + 1):
    print(i * '*')

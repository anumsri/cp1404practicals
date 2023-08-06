"""
CP1404/CP5632 - Practical
Answer's for files program
"""

# Q1
out_file = open('name.txt', 'w')
name = input(str("Enter Name: "))
print(name, file=out_file)
out_file.close()

# Q2
in_file = open('name.txt', 'r')
name = in_file.read().strip
print(f"Your name is", name)
in_file.close()

# Q3
in_file = open('numbers.txt', 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

# Q4
in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()

"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        raise ValueError("Numerator and denominator must be valid numbers!")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    # Will occur when input of Numerator and Denominator are not integers
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    # Will occur when input Denominator is zero
    print("Cannot divide by zero!")
print("Finished.")

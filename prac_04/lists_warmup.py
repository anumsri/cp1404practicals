"""
CP1404/CP5632 - Practical
List warmup
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
# 1. Numbers[0] = 3
# 2. Numbers[-1] = 2
# 3. Numbers[3] = 1
# 4. Numbers[:-1] = [3, 1, 4, 1, 5, 9]
# 5. Numbers[3:4] = [1, 5]
# 6. 5 in numbers = True
# 7. 7 in numbers = False
# 8. "3" in numbers = False
# 9. numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
9 in numbers

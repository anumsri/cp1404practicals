"""
CP1404 - Practical
Get password with minimum length and display asterisk
"""

MINIMUM = 3


def get_password():
    """Get password of valid length and display asterisks"""
    password = input("Enter Password: ")
    while len(password) < MINIMUM:
        print(f"Password must be longer than {MINIMUM}")
        password = input("Enter Password: ")
    print("*" * len(password))


get_password()

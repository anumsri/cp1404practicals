"""
CP1404 - Practical
Get password with minimum length and display asterisk
"""

MINIMUM = 3


def main():
    password = get_password(MINIMUM)
    display_asterisk(password)


def display_asterisk(password):
    print("*" * len(password))


def get_password(minimum_length):
    """Get password of valid length and display asterisks"""
    password = input("Enter Password: ")
    while len(password) < minimum_length:
        print(f"Password must be longer than {minimum_length}")
        password = input("Enter Password: ")
    return password


main()

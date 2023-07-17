"""
CP1404/CP5632 Practical
Email Storing program
Estimate: 30 minutes
Actual:   50 minutes
"""


def main():
    """Create dictionary of names and email"""
    email_to_name = {}
    email = input("Enter Email: ")
    while email != "":
        name = get_name(email)
        verification = input(f"Is your name{name}? (Y/N)")
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    """Retrieve name from given email"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()

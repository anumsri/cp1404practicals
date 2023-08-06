"""
CP1404/CP5632 - Practical
Score menu program
"""

MENU = """(G)et a valid score 
(P)rint result 
(S)how stars
(Q)uit"""


def main():
    """Display menu and get choice"""
    score = ""
    print(MENU)
    choice = input("Enter choice:").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            get_rating(score)
        elif choice == "S":
            display_asterisk(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter choice: ").upper()
    print("Have a good day!")


def get_valid_score():
    """Check if score is valid"""
    score = int(input("Enter score: "))
    while score <= 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def get_rating(score):
    """Determine rating of the score."""
    if score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")


def display_asterisk(score):
    """Print asterisk depending on len of score"""
    print("*" * score)


main()

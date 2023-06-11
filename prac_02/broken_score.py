"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Get score and display its rating."""

    score = float(input("Enter score: "))
    print(get_rating(score))
    print(random.randint(0, 100))


def get_rating(score):
    """Determine rating of the score."""
    if 0 > score > 100:
        return "Invalid score"
    elif score >= 50:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


main()

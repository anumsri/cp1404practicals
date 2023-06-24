"""
CP1404/CP5632 Practical
Quick Pick Lottery ticket generator
"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
MAX_PER_LINE = 6


def main():
    num_picks = int(input("How many quick picks? "))
    get_quick_picks(num_picks)


def get_quick_picks(num_picks):
    """Get random quick picks in range of minimum and maximum"""
    for i in range(num_picks):
        quick_pick = []
        while len(quick_pick) < MAX_PER_LINE:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            if number not in quick_pick:
                quick_pick.append(number)
        print(" ".join(str(number) for number in quick_pick))


main()

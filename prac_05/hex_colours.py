"""
CP1404/CP5632 Practical
Hex Colours program
"""

COLOUR_TO_CODE = {
    "absolute zero": "0048ba",
    "acid green": "b0bf1a",
    "aliceblue": "f0f8ff",
    "alizarin crimson": "e32636",
    "amaranth": "e52b50",
    "amber": "ffbf00",
    "amethyst": "faebd7",
    "antiqueWhite": "9966cc",
    "aqua": "00ffff",
    "ash Grey": "b2beb5"}

colour = input("Enter colour: ").lower()
while colour != "":
    code = COLOUR_TO_CODE.get(colour)
    if code:
        print(f"{colour} has code {code}")
    else:
        print("Invalid colour")
    colour = input("Enter colour: ").lower()

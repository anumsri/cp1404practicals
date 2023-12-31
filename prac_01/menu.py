"""
CP1404/CP5632 - Practical
Simple Menu Driven Program
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter Name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")

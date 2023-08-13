"""Wikipedia Program CP1404"""

import wikipedia


def main():
    while True:
        user_input = input("Enter page title or search phrase: ")
        if not user_input:
            break
        page = wikipedia.page(user_input)
        print("Summary:")
        print(page.summary)


main()

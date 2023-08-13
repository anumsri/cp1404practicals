"""Wikipedia Program CP1404"""

import wikipedia


def main():
    while True:
        user_input = input("Enter page title or search phrase: ")
        if not user_input:
            break

        try:
            page = wikipedia.page(user_input, auto_suggest=False)
            print("Title: ", page.title)
            print("Summary:")
            print(page.summary)
            print("URL= ", page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)


main()

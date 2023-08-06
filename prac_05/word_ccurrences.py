"""
CP1404/CP5632 Practical
Word Occurrences Program
Estimate: 20 minutes
Actual:   40 minutes
"""
word_count = {}
text = input("Enter text: ")
words = text.split()
for word in words:
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1

words = list(word_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_count[word]}")
from collections import Counter

def repeated_word(string):
    words = string.lower().split()

    dict = Counter(words)

    for word in words:
        if dict[word]>1:
            return word


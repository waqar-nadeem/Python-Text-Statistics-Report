import string
from collections import Counter

text = input("Enter text: ")

characters = len(text)
characters_no_spaces = len(text.replace(" ", ""))
words_list = text.split()
words = len(words_list)
sentences = text.count('.') + text.count('!') + text.count('?')

word_freq = Counter(word.strip(string.punctuation).lower() for word in words_list)

print("Text Statistics Report")
print("Characters:", characters)
print("Characters (no spaces):", characters_no_spaces)
print("Words:", words)
print("Sentences:", sentences)
print("Most Common Words:")
for word, count in word_freq.most_common(10):
    print(word, "-", count)

"""CP1404 | prac_05 word occurrences | Darcy Kemp
program to count occurrences of a word in a string
est:30
real:22
"""
user_input_string = str(input("Text: "))
word_to_occurrences = {}
max_word_length = 0

for word in user_input_string.split(" "):
    word_to_occurrences[word] = word_to_occurrences.get(word, 0) + 1

    if len(word) > max_word_length:
        max_word_length = len(word)

word_to_occurrences = dict(sorted(word_to_occurrences.items()))


for key in word_to_occurrences:
    print(f"{key:{max_word_length}} is {word_to_occurrences[key]}")

"""CP1404 | prac_05 word occurrences | Darcy Kemp
program to count occurrences of a word in a string

"""
user_input_string = str(input("Text: "))
word_to_occurrences = {}

for word in user_input_string.split(" "):
    word_to_occurrences[word] = word_to_occurrences.get(word, 0) + 1

for key in word_to_occurrences:
    print(f"{key} is {word_to_occurrences[key]}")

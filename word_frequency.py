#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies


import re
import string

# Function to validate sentence
def is_sentence(text):
    text = text.strip()
    if not isinstance(text, str) or not text:
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True

# Prompt user until valid sentence is entered
user_sentence = input("Enter a sentence: ")

while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# Split sentence into words
words = user_sentence.split()

# Initialize lists
word_list = []
frequency_list = []

# Count word frequencies using lists
for word in words:
    cleaned = word.strip(string.punctuation).lower()
    if cleaned in word_list:
        index = word_list.index(cleaned)
        frequency_list[index] += 1
    else:
        word_list.append(cleaned)
        frequency_list.append(1)

# Print results
print("\nWord Frequencies:")
for i in range(len(word_list)):
    print(f"{word_list[i]}: {frequency_list[i]}")

#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

#import re
#import string

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
#def is_sentence(text):
 #   text = text.strip()
    # Check if the text is not empty and is a string
  #  if not isinstance(text, str) or not text.strip():
   #     return False

    # Check for starting with a capital letter
#    if not text[0].isupper():
 #       return False

    # Check for ending punctuation
  #  if not re.search(r'[.!?]$', text):
   #     return False

    # Check if it contains at least one word (non-whitespace characters)
    #if not re.search(r'\w+', text):
     #   return False

    #return True

#user_sentence = input("Enter a sentence: ")

#while not is_sentence(user_sentence):
 #   print("This does not meet the criteria for a sentence.")
  #  user_sentence = input("Enter a sentence: ")
    
#words = user_sentence.split()
#word_list = []
#frequency_list = []

#for word in words:
 #   cleaned = word.strip(string.punctuation).lower()
  #  if cleaned in word_list:
   #     index = word_list.index(cleaned)
    #    frequency_list[index] += 1
    #else:
     #   word_list.append(cleaned)
      #  frequency_list.append(1)

# Print results
#print("\nWord Frequencies:")
#for i in range(len(word_list)):
 #   print(f"{word_list[i]}: {frequency_list[i]}")
    
#input("\nPress Enter to exit...")


import re
import string

def is_sentence(text):
    text = text.strip()
    if not isinstance(text, str) or not text:
        return False
    if not text[0].isupper():
        return False
    if not (text.endswith(".") or text.endswith("!") or text.endswith("?")):
        return False
    # Instead of regex, just check that there's at least two words
    if len(text.split()) < 2:
        return False
    return True

print("DEBUG: Program started")

user_sentence = input("Enter a sentence: ")
print("DEBUG: You typed:", repr(user_sentence))

while not is_sentence(user_sentence):
    print("DEBUG: Failed is_sentence check")
    user_sentence = input("Enter a sentence: ")
    print("DEBUG: You typed:", repr(user_sentence))

print("DEBUG: Passed is_sentence check")

words = user_sentence.split()
print("DEBUG: Words after split ->", words)

word_list = []
frequency_list = []

for word in words:
    cleaned = word.strip(string.punctuation).lower()
    print("DEBUG: Processing word ->", cleaned)
    if cleaned in word_list:
        index = word_list.index(cleaned)
        frequency_list[index] += 1
    else:
        word_list.append(cleaned)
        frequency_list.append(1)

print("DEBUG: Word list ->", word_list)
print("DEBUG: Frequency list ->", frequency_list)

print("\nWord Frequencies:")
for i in range(len(word_list)):
    print(f"{word_list[i]}: {frequency_list[i]}")

input("\nPress Enter to exit...")




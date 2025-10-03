#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
def get_positive_integer():
  while True:
    user_input = input("How many terms of the Fibonacci sequence do you want? ")
    if user_input.isdigit():
      num = int(user_input)
      if num > 0:
        return num
    print("Please enter a positive integer.")

def generate_fibonacci(n):
  sequence = []
  a, b = 0, 1
  for _ in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence

def main():
  num_terms = get_positive_integer()
  fib_sequence = generate_fibonacci(num_terms)
  print("Fibonacci sequence:")
  print(" ".join(str(num) for num in fib_sequence))

main()

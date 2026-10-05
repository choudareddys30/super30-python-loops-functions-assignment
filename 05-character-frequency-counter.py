#5 Character Frequency Counter

#Take a string from the user and calculate how many times each character occurs.
#  Example: "banana" should identify the frequencies of b, a, and n.

text = input("Enter a string: ")
frequency = {}

for character in text:
  if character in frequency:
    frequency[character] += 1
  else:
    frequency[character] = 1

for character, count in frequency.items():
  print(f"'{character}': {count}")

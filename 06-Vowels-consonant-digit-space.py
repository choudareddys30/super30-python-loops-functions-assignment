#6 Vowel, Consonant, Digit and Space Counter
#Create a program that analyzes a sentence and counts vowels, consonants, digits, spaces,
#  and special characters separately.

sentence = input("Enter a sentence: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0

for char in sentence:
  if char.lower() in 'aeiou':
      vowels +=1
  elif char.isalpha():
      consonants +=1
  elif char.isdigit():
      digits +=1
  elif char.isspace():
      spaces +=1
  else:
      special_characters +=1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special Characters: {special_characters}")
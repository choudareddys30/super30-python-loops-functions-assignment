#1. Number Analyzer using for loop

#Take a number N from the user. Print all numbers from 1 to N, identify whether each 
# number is even or odd, and finally display the total count of even and odd numbers.

n = int(input("Enter a Number:"))
even_count = 0
odd_count = 0
if n <= 0:
  print("Please enter a positive integer.")
else:
  for i in range(1, n+1):
    if i % 2 == 0:
      print(f"{i} is Even")
      even_count += 1
    else:
      print(f"{i} is Odd")
      odd_count += 1

print(f"Count of Even Numbers: {even_count}")
print(f"Count of Odd Numbers: {odd_count}")
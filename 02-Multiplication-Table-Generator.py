#2 Multiplication Table Generator

# Take a number from the user and print its multiplication table from 1 × N through 10 × N 
# using a for loop. Then modify the program so the ending range can also be supplied by the user.

n = int(input("Enter a Number:"))

for i in range(1, 11):
  print(f"{n} x {i} = {n*i}")

n = int(input("Enter a Number:"))
end_number = int(input("Enter the Ending Number:"))

if n <= 0 or end_number <= 0:
  print("Please enter positive integers.")
else:
  for i in range(1, end_number + 1):
    print(f"{n} x {i} = {n*i}")
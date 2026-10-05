#3 Sum and Average Without sum()

#Given a list of numbers, calculate the total and average using a loop. Do not use Python's 
# built-in sum() function.

l = [10, 20, 30, 40, 50]
total = 0
average = 0
length = len(l)
for i in l:
  total += i
print(f"Total: {total}")
if len(l) > 0:
  average = total / length
  print(f"Average: {average}")
else:
  print("The list is empty. Cannot calculate average.")

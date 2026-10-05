#9 Student Marks Analyzer

#Store marks of multiple students in a list. Using loops, calculate highest marks, 
# lowest marks, average marks, number of students who passed, and number who failed.
#  Consider 40 as the passing mark.

marks = [85, 32, 76, 40, 95, 28, 60]

highest = marks[0]
lowest = marks[0]
total = 0
passed = 0
failed = 0

for mark in marks:
    if mark > highest: # 85 > 85
        highest = mark

    if mark < lowest: # 32 < 85
        lowest = mark

    total += mark # 0+85

    if mark >= 40: # 
        passed += 1
    else:
        failed += 1 #

average = total / len(marks) #

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", round(average, 2))
print("Students passed:", passed)
print("Students failed:", failed)
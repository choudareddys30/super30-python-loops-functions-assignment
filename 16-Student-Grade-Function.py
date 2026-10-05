#16 Student Grade Function

#Create a function that accepts marks for five subjects, calculates total and percentage, 
# and returns a grade based on rules you define such as A, B, C, D, or Fail. Add appropriate 
# validation for invalid marks.

def student_grade(marks):
    if len(marks) != 5:
        return "Please provide marks for exactly five subjects."

    total = 0

    for mark in marks:
        if type(mark) not in (int, float):
            return "Invalid marks. Please provide numbers only."

        if not 0 <= mark <= 100:
            return "Invalid marks. Each mark must be between 0 and 100."

        total += mark

    percentage = (total / 500) * 100

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    return {
        "total": total,
        "percentage": percentage,
        "grade": grade
    }


marks = [80, 75, 90, 85, 70]
result = student_grade(marks)
print(result)
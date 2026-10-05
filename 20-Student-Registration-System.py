#20 Final Challenge — Student Registration System

#Build a menu-driven application using functions + for loops + while loops. 
# The system should allow users to add a student, view all students, search by ID, 
# update student details, delete a student, calculate class average marks, 
# display the highest-performing student, and exit. 
# Store the records using appropriate Python data structures.

students = {}


def add_student():
    student_id = int(input("Enter student ID: "))
    if type(student_id) != int:
        print("Student ID must be an integer.")
        return
    
    if student_id == "":
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    marks = float(input("Enter marks (0–100): "))

    if name == "":
        print("Student name cannot be empty.")
    elif not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
    else:
        students[student_id] = {"name": name, "marks": marks}
        print("Student added successfully.")


def view_students():
    if not students:
        print("No students registered.")
        return

    for student_id, details in students.items():
        print(
            f"ID: {student_id} | "
            f"Name: {details['name']} | "
            f"Marks: {details['marks']}"
        )


def search_student():
    student_id = int(input("Enter student ID to search: "))

    if student_id in students:
        details = students[student_id]
        print("Name:", details["name"])
        print("Marks:", details["marks"])
    else:
        print("Student not found.")


def update_student():
    student_id = int(input("Enter student ID to update: "))

    if student_id not in students:
        print("Student not found.")
        return

    name = input("Enter new name: ").strip()
    marks = float(input("Enter new marks (0–100): "))

    if name == "":
        print("Student name cannot be empty.")
    elif not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
    else:
        students[student_id] = {"name": name, "marks": marks}
        print("Student updated successfully.")


def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def class_average():
    if not students:
        print("No students registered.")
        return

    total = 0

    for details in students.values():
        total += details["marks"]

    average = total / len(students)
    print(f"Class average marks: {average:.2f}")


def highest_performing_student():
    if not students:
        print("No students registered.")
        return

    highest_marks = -1

    for details in students.values():
        if details["marks"] > highest_marks:
            highest_marks = details["marks"]

    print("Highest-performing student(s):")

    for student_id, details in students.items():
        if details["marks"] == highest_marks:
            print(
                f"ID: {student_id} | "
                f"Name: {details['name']} | "
                f"Marks: {details['marks']}"
            )


while True:
    print("\n--- Student Registration System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search by ID")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Class Average Marks")
    print("7. Highest-Performing Student")
    print("8. Exit")

    choice = input("Enter your choice (1–8): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        class_average()
    elif choice == "7":
        highest_performing_student()
    elif choice == "8":
        print("Application closed.")
        break
    else:
        print("Invalid choice. Please try again.")
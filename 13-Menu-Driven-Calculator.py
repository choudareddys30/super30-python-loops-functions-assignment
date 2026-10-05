#13 Menu-Driven Calculator

#Build a continuously running calculator using while. 
# Provide Addition, Subtraction, Multiplication, Division, Modulus, and Exit operations.
#  Handle division by zero properly.

while True:
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = input("Enter your choice (1–6): ")

    if choice == "6":
        print("Calculator closed.")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Please try again.")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", num1 / num2)

    elif choice == "5":
        if num2 == 0:
            print("Cannot calculate modulus with zero.")
        else:
            print("Result:", num1 % num2)
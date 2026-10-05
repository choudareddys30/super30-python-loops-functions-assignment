#10 ATM Withdrawal Simulator using while

#Start with a balance of ₹10,000. Continuously show the user options to check balance,
#deposit money, withdraw money, or exit. The program should continue until the user explicitly 
# chooses Exit.

balance = 10000

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1–4): ")

    if choice == "1":
        print(f"Your balance is ₹{balance:.2f}")

    elif choice == "2":
        amount = float(input("Enter the deposit amount: ₹"))

        if amount > 0:
            balance += amount
            print(f"Deposit successful! Balance: ₹{balance:.2f}")
        else:
            print("Please enter an amount greater than zero.")

    elif choice == "3":
        amount = float(input("Enter the withdrawal amount: ₹"))

        if amount <= 0:
            print("Please enter an amount greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Withdrawal successful! Balance: ₹{balance:.2f}")

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
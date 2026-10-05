#19 Bank Account Mini Application

#Create functions for deposit(), withdraw(), check_balance(), and transaction_history().
#  Use a while loop to keep the banking application running. Prevent withdrawals when 
# sufficient balance is unavailable.

balance = 10000
transactions = []


def deposit():
    global balance

    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited: ₹{amount:.2f}")
        print(f"Deposit successful! Balance: ₹{balance:.2f}")
    else:
        print("Amount must be greater than zero.")


def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Amount must be greater than zero.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        transactions.append(f"Withdrawn: ₹{amount:.2f}")
        print(f"Withdrawal successful! Balance: ₹{balance:.2f}")


def check_balance():
    print(f"Your balance is ₹{balance:.2f}")


def transaction_history():
    if not transactions:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)


while True:
    print("\n--- Banking Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        check_balance()
    elif choice == "4":
        transaction_history()
    elif choice == "5":
        print("Thank you for using the banking application!")
        break
    else:
        print("Invalid choice. Please try again.")
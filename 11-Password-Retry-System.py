#11 Password Retry System

#Store a predefined password and give the user a maximum of three attempts to enter it 
#correctly. Use a while loop. After three incorrect attempts, display "Account Locked".

password = "Hello@123"
attempts = 0

while attempts < 3:
    entered_password = input("Enter your password: ")

    if entered_password == password:
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Incorrect password.")

        if attempts == 3:
            print("Account Locked")
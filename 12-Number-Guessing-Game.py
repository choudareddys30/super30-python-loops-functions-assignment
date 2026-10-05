#12 Number Guessing Game

#Generate a random number between 1–100. Keep asking the user to guess until they find the 
# correct number. After each incorrect guess, display "Too High" or "Too Low". Finally display 
# the number of attempts taken.

#import random

#secret_number = random.randint(1, 100)
secret_number = 42 
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct guess!")
        print("Number of attempts:", attempts)
        break
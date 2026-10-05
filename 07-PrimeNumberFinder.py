#7 Prime Number Finder

#Ask the user for a starting and ending number. 
# Print all prime numbers within that range using nested loops.
# Prime numbers are numbers greater than 1 that have no divisors other than 1 and themselves.
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1): #1 to 10+1 (1,2,3,4,5,6,7,8,9,10)
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)
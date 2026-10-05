#15 Reusable Number Analysis Function

# Create a function def analyze_number(number): ...

# It should determine whether the number is positive/negative/zero, even/odd, and prime/not 
# prime. Return the results rather than only printing them.

def analyze_number(number):
    # Positive, negative, or zero
    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    # Even or odd
    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    # Prime or not prime
    is_prime = False

    if number > 1:
        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        prime_status = "Prime"
    else:
        prime_status = "Not prime"

    return {
        "sign": sign,
        "parity": parity,
        "prime_status": prime_status
    }


number = int(input("Enter an integer: "))
result = analyze_number(number)
print(result)
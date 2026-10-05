# 14 Create Your Own sum() Function

# Write def my_sum(numbers) It should accept a list of numbers and return their sum without
#  using Python's built-in sum().

def my_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


marks = [10, 20, 30, 40, 50]
print("Sum:", my_sum(marks))
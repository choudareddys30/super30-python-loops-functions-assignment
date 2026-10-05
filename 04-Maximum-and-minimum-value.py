#4 Find Maximum and Minimum Without max() / min()

# Write a program that finds the largest and smallest values in a list using loops only.

l = [10, 20, 30, 40, 50]

max_value = l[0]
min_value = l[0]

if not l:
    print("The list is empty. Cannot find maximum and minimum values.")
else:
    for i in l:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i

    print(f"Maximum Value: {max_value}")
    print(f"Minimum Value: {min_value}")
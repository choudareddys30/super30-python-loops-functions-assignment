#8 Pattern Generator
#Using nested for loops, generate the following pattern for a user-supplied value of N:

n = int(input("Enter the number of rows: ")) #5

for row in range(1, n + 1): #(1,2,3,4,5)
    for number in range(1, row + 1): 
        print(number, end=" ")
    print()
# Get the input from the user for the value of n and then find the sum of first n natural numbers.

n = int(input("Enter a number: "))
sum = 0
while(n>0):
    sum = sum + n
    n = n - 1
    print("The sum of first n natural numbers is", sum)
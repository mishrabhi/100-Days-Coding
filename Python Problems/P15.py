# Get a number as input from user and then check whether that number is a strong number or not. A number is said to be strong number if the sum of the factorial of each digit in the number is same as that of the number.
 
sum = 0
num = int(input("Enter a number: "))
temp = num
while(num):
    i = 1
    fact = 1
    rem = num % 10
    while(i<=rem):
        fact = fact * i
        i = i + 1
    sum = sum + fact 
    num = num // 10
    if (sum == temp):
        print("Given number is strong number")
    else:
        print("Given number is not strong number")
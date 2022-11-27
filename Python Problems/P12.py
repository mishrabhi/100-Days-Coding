# Get a number from user and then find the sum of the digits in the given number.

#E.g. let the number = 341

#Sum of digits is 3+4+1= 8

num = int(input("Enter any number: "))
sum = 0
while(num>0):
    dig = num%10
    sum = sum + dig
    num = num//10
    print("The sum of the digits in the number is: ",sum)

# Get an input number from the user and check whether it is a positive or negative number.

num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num == 0:
    print("Neither Positive nor Negative")
else:
    print("The number is negative")
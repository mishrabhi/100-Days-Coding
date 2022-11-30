# Get an input from the user and the print the reverse of the given number as the output

num = str(input("Enter a number: "))
print(str(num)[::-1])

# OR

num = int(input("Enter a number: "))
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10 
print("Reversed Number: " + str(reversed_num))
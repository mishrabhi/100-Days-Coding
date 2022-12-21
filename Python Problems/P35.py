# Get a string from the user and find the sum of numbers in the string

Str1 = input('Enter a string:')
Sum = 0
for i in Str1:
    if ord(i) >= 48 and ord(i) <= 57:
        Sum = Sum + int(i)
print('Sum is: ' + str(Sum))
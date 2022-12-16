# Get a string as input from user and print the length of the string without using strlen() function

str1 = input("Enter a string: ")
count = 0
for s in str1:
    count = count + 1
print("Length of the string is:",count)
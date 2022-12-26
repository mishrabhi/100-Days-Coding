# Get a string as input from the user and then get another string which has to be removed from the string.

# Get the third input, the new substring which is placed in that substring position.

# Finally print the output by replacing the substring with new string.

# Get the first string from the user
first_string = input("Enter the first string: ")

# Get the second string from the user
second_string = input("Enter the string to be removed: ")

# Get the third string from the user
third_string = input("Enter the new string to be placed: ")

# Replace the second string with the third string in the first string
result = first_string.replace(second_string, third_string)

# Print the resulting string
print(result)
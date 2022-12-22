# Get a string as the input from the user and find the frequency of characters in the string

string = "program"
for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")
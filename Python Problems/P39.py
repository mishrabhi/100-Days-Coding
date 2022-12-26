# Get two strings as input from the user and check whether it is Anagram or not.

str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
# convert both the strings into lowercase
str1 = str1.lower()
str2 = str2.lower()
# check if length is same
if(len(str1) == len(str2)):
    # sort the string
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
         print(str1 + " and " + str2 + " are not anagram.")
else:
    print(str1 + " and " + str2 + " are not anagram.")

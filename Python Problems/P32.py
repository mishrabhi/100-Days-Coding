# Get a string as the input from the user and then remove all the vowel letters from the string and give the output.

string = input("Enter the string: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
for i in range(len(string)):
    if string [i] not in vowels:
        result = result + string[i]

print("After removing Vowels: ", result)
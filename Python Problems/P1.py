
#Problem 1: Take an input character from the user and check whether the given input is a vowel or consonant.

ch = input("Please enter your own character: ")
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print("The given character", ch, "is a vowel")
else:
    print("The given character", ch, "is a consonant")



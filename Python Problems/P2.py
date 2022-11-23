#Problem2:Take an input character from user and check whether it is an alphabet or not.

ch = input("Please enter a character: ")
if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is Not an Alphabet")
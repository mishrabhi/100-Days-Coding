# Get an algebraic expression as input from the user and then remove all the brackets in that.
Exp = input("Enter an Equation: ")
Equation = ''
for i in Exp:
    if ord(i) == 41 or ord(i) == 40 or ord(i) == 91 or ord(i) == 93 or ord(i) == 123 or ord(i) == 125:
        #if true
        pass
    else:
        #if false
        #add it to empty string
        Equation = Equation + i
print("String without bracket is "+ Equation)
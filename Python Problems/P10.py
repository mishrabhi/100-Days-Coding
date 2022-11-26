
#Get a number from user for which you need to fin the factorial, then calculate the factorial and give it as the output.

#Input

#4

#Output

#24

num = int(input("Enter a number: "))
fact = 1
if (num < 0):
    print("Factorial can't be defined")
else:
    for i in range(1,num+1):
     fact = fact * i
    print("Factorial is", fact)
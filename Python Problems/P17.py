# Get an input from the user and find the factors of the number.

#Input

#4

#Output

#1,2,4  

def print_factors(x):
    print("The factors of",x,"are: ")
    for i in range(1, x+1):
        if x % i == 0:
            print(i)
num = int(input("Enter any number: "))
print_factors(num)
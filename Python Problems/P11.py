# Fibonacci series is a special series where nth term is the sum of previous two terms in the series. The series starts with 0 and 1 as the first and second term of the series respectively.

#Here you need to get the value for nth term from user and then print Fibonacci series containing n terms.

#Input

#5

#Output

#0,1,1,2,3

num = int(input("Enter any number: "))
a,b = 0,1
print("Fibonacci Series:",a,",",b,end=",")
for i in range(2,num):
    c = a+b
    a=b
    b=c
    print(c,",", end=" ")
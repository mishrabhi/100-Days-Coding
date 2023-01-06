# Given an integer array of size N, write a program to sort the array;

n=int(input("Enter size of array\n"))
arr=list(map(int,input("Enter elements of array\n").split()))
arr.sort(reverse=False) #arr.sort() also be used
print("Ascending order array")
print(*arr)
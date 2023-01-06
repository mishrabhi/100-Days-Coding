# Given an integer array of size N. Write Program to find sum of positive square elements in the array.

def SumOfSquare(arr,n):
 sum = 0
 for i in range(0,n):
    sum = sum + arr[i]*arr[i]
 return sum
n = int(input())
arr = list(map(int,input().split(' ')))
print(SumOfSquare(arr,n))
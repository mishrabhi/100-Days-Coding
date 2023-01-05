# Get an array as the input from the user and find the sum of the elements

n = int(input("Enter size of array: "))
arr = []
print("Enter array elements: ")
for i in range(0,n):
    temp = int(input())
    arr.append(temp)
Sum = 0
for i in range(len(arr)):
 Sum = Sum + arr[i]
print("Sum: ",Sum)
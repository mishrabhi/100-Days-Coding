# Get an array as input from the user and then find the smallest and largest element in the array.

n = int(input("Enter size of array: "))
arr = []
print("Enter array elements: ")
for i in range(0,n):
    temp = int(input())
    arr.append(temp)
small = arr[0]
large = arr[0]
for i in range(len(arr)):
 if arr[i] < small:
    small = arr[i]
 if arr[i] > large:
    large = arr[i]
print ("Smallest Number: ",small)
print ("Largest Number: ",large)
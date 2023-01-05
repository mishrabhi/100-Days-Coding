# Get an array as input from the user and then count the number of even and odd elements present in the array.

n = int(input("Enter size of array: "))
arr = []
print("Enter array elements: ")
for i in range(0,n):
    temp = int(input())
    arr.append(temp)
even = 0
odd = 0
for i in range(0, n):
 if arr[i]%2==0 :
    even += 1
 else:
    odd += 1
print("Number of even elements: ",even )
print("Number of odd elements: ",odd)
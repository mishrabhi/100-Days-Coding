# Get an array as input from the user and check the type of the array, whether it is odd, even or mixed type.

n = int(input("Enter size of array: "))
arr = []
print("Enter array elements: ")
for i in range(0,n):
    temp = int(input())
    arr.append(temp)
o = 0
e = 0
for i in range(0,n):
    if(arr[i] % 2 == 1):
        o = o + 1
    else:
        e = e + 1
if(o == n):
    print("Odd")
elif(e == n):
    print("Even")
else:
    print("Mixed");
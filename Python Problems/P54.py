# Given an integer array of size N. Write Program to find whether Arrays are disjoint or not
# Two arrays are said to be disjoint if they have no elements in common.

def disjoint_arrays(arr1,arr2):
    for i in range(0,len(arr1)):
        for j in range(0,len(arr2)):
            if (arr1[i] == arr2[j]):
                return -1
                return 1;
arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
res = disjoint_arrays(arr1,arr2)
if (res == -1):
    print("The arrays are not disjoint")
else:
    print("The arrays are disjoint")
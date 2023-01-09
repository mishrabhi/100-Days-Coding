#  Given an integer array of size N. Write Program to find maximum product subarray in a given array

def MaxSubArrProd(arr,n):
    ans =arr[0]
    for i in range(0,n):
        prod = arr[i]
        for j in range(i+1,n):
            ans = max(ans,prod)
            prod = prod * arr[j]
            ans = max(ans,prod)
        return ans;
n = int(input())
arr = list(map(int,input().split()))
print(MaxSubArrProd(arr,n))
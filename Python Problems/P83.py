# Given a complete binary tree with the height of H, we index the nodes respectively top-down and left-right from 1. The i-th node stores a positive integer Vi. Define Pi as follows: Pi=Vi if the i-th node is a leaf, otherwise Pi=max(Vi*PL, Vi*PR), where L and R are the indices of the left and right children of i, respectively. Your task is to caculate the value of P1.

# Input

# There are several test cases (fifteen at most), each formed as follows:

# The first line contains a positive integer H (H ≤ 15).
# The second line contains 2H-1 positive integers (each having a value of 109 at most), the i-th integer shows the value of Vi.
# The input is ended with H = 0.

z=0
while z==0:
    h=int(input())
    if h==0:
        break
    n=(1<<h)-1
    p=[0]*(n+10)
    v=[ int(x) for x in input().split() ]
    for i in range(n-1,-1,-1):
        if 2*i+1 >=n:
            p[i]=v[i]
        else:
            p[i]=v[i]*max(p[2*i+1],p[2*i+2])
        ans=p[0]%1000000007
        print(ans)
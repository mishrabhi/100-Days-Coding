# You are given an array A of N elements. For any ordered triplet (i,j,k) such that i, j, and k are pairwise distinct and 1≤i,j,k≤N, the value of this triplet is (Ai?−Aj?)⋅Ak?. You need to find the maximum value among all possible ordered triplets.

# Note: Two ordered triplets (a,b,c) and (d,e,f) are only equal when a=d and b=e and c=f. As an example, (1,2,3) and (2,3,1) are two different ordered triplets.

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    a=input().split()
    for i in range(0,n):
        a[i]=int(a[i])
    a.sort()
    a1=(a[-2]-a[0])*a[-1]
    a2=(a[-1]-a[0])*a[-2]
    print(max(a1,a2))
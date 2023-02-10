# You are given a binary string S of length N. You can perform the following operation on S:

# Pick any set of indices such that no two picked indices are adjacent.
# Flip the values at the picked indices (i.e. change 0 to 1 and 1 to 0).
# For example, consider the string S=1101101.
# If we pick the indices {1,3,6}, then after flipping the values at picked indices, we will get 1?10?110?1→0111111.
# Note that we cannot pick the set {2,3,5} since 2 and 3 are adjacent indices.

# Find the minimum number of operations required to convert all the characters of S to 0.

T = int(input())
for i in range(T):
 N = int(input())
 S = list(input())
 count = 0
 while(S.count('1')!=0):
    cnt = 0
 t = 0
 for i in range(N):
    if(t==1):
        t = 0
        continue
    elif(S[i]=='1'):
        cnt += 1
        S[i]='0'
        t = 1
    if(cnt!=0):
        count += 1
    print(count)
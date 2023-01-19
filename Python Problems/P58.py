# # Nejiya has a bucket having a capacity of K liters. It is already filled with X liters of water.

# Find the maximum amount of extra water in liters that Nejiya can fill in the bucket without overflowing.

r = int(input())
for i in range(r):
    k,y = map(int,input().split())
    ans = int(k-y)
    a = ans + y
    print(ans)
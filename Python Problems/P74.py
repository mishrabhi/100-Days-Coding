# You have a grid with N rows and M columns. You have two types of tiles — one of dimensions 2×2 and the other of dimensions 1×1. You want to cover the grid using these two types of tiles in such a way that:

# Each cell of the grid is covered by exactly one tile; and
# The number of 1×1 tiles used is minimized.
# Find the minimum number of 1×1 tiles you have to use to fill the grid.

t=int(input())
while t!=0:
    m,n=map(int,input().split())
if m%2==0 and n%2==0:
    print('0')
elif m%2==0 and n%2==1:
    print(m)
elif m%2==1 and n%2==0:
    print(n)
else:
     print(m+n+-1)
     t-=1
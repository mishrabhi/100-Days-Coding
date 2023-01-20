# Given the time control of a chess match as a+b, determine which format of chess out of the given 4 it belongs to.

# 1) Bullet if a+b<3

# 2) Blitz if 3≤a+b≤10

# 3) Rapid if 11≤a+b≤60

# 4) Classical if 60<a+b

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    c = a+b
    if(a+b<3):
        print(1)
    elif(3<=a+b<=10):
        print(2)
    elif(11<=a+b<=60):
        print(3)
    elif(60<a+b):
        print(4)
# Anusree has decided to go to a gold mine along with N of his friends (thus, total N+1 people including Anusree go to the gold mine).

# The gold mine contains a total of X kg of gold. Every person has the capacity of carrying up atmost Y kg of gold.

# Will Anusree and his friends together be able to carry up all the gold from the gold mine assuming that they can go to the mine exactly once.

T = int(input())
for i in range(T):
    x,y,z = map(int,input().split())
    x = x + 1
    if(x * z >= y):
        print("Yes")
    else:
        print("No")
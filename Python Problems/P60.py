# The weather report of Magicland is Good if the number of sunny days in a week is strictly greater than the number of rainy days.

# Given 7 integers A1,A2,A3,A4,A5,A6,A7 where Ai=1 denotes that the ith day of week in Magicland is a sunny day, Ai=0 denotes that the ith day in Magicland is a rainy day. Determine if the weather report of Magicland is Good or not.

t = int(input())
for i in range(t):
    b=7
    a= list(map(int,input().split()))
    x=a.count(0)
    y=a.count(1)
    if x>y:
        print("No")
    else:
        print("Yes")
# Add an element to the set. :

# Delete an element from the set. (If the number is not present in the set, then do nothing). :

# If the number is present in the set, then print "Yes"(without quotes) else print "No"(without quotes).

t = int(input())
s = set()
for i in range(t):
    n,a = map(int,input().split())
    if n == 1:
        s.add(a)
    elif n == 2:
        if(a in s):
            s.remove(a)
    elif n == 3:
        if(a in s):
            print("Yes")
        else:
            print("No")
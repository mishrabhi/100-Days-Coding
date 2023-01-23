# First line of input contains a single integer T denoting the number of test cases.

# For each test case:

# First line contains the string A

# Second line contains the string B.

for _ in range(int(input())):
    a = set(input())
    b = set(input())
    ans = False
    al = len(a)
    bl = len(b)
    if(al<bl):
        for e in a:
            if(e in b):
                ans = true
                break
        else:
            for e in b:
                if(e in a):
                    ans = True
                    break
            if(ans):
                print("Yes")
            else:
                print("No")
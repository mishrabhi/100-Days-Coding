# Ajinkya decided to buy a new tablet. His budget is B, so he cannot buy a tablet whose price is greater than B. Other than that, he only has one criterion — the area of the tablet's screen should be as large as possible. Of course, the screen of a tablet is always a rectangle.

# Ajinkya has visited some tablet shops and listed all of his options. In total, there are N available tablets, numbered 1 through N. For each valid i, the i-th tablet has width Wi, height Hi and price Pi.

# Help Ajinkya choose a tablet which he should buy and find the area of such a tablet's screen, or determine that he cannot buy any tablet

t = int(input())
for A in range(t):
    n,b = map(int,input().split(" "))
    dict = {}
    for x in range(n):
        w,h,i = map(int,input().split(" "))
        dict[w*h] = i
    dd = sorted(dict)
    #print(dd)
    for x in range(len(dd)-1,-1,-1):
        m = dict[dd[x]]
        if m<=b:
            print(dd[x])
            break
        else:
            print("no tablet")

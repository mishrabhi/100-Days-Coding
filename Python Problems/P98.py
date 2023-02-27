# There are N breakfasts in the restaurant “Fat Hut” where the Arun works. The ith breakfast has an attractiveness Ai? and cost Ci?.

# Arun has noticed that nobody takes the jth breakfast if there exists at least one breakfast i such that Ai?≥Aj? and Ci?<Cj?.

# In other words, if a breakfast is less attractive and more expensive than any of the other dishes, then nobody is interested in that breakfast.

# Arun will be happy if all the N breakfasts have a chance to be taken. Unfortunately, Arun has no power over prices. On the other hand, he can change the attractiveness of some breakfasts by some real number. However, after the changes, the attractiveness of the ith breakfast must lie in the interval [Li?,Ri?].

# He would also like to change the attractiveness of the minimum number of breakfasts. Help the Chef do it.

from bisect import bisect
from copy import copy
from operator import itemgetter
INF = 1E9
def solve(n, aclr):
    aclr.sort()
    aclr.sort(key=itemgetter(1))
    alrv = [(a*n -i , l*n - i, r*n-i) for i,(a,_,l,r) in enumerate(aclr)]
    costs = [n+1, 0]
    qual = [0]
    for a,l,r in alrv:
        pl = bisect(qual, l)
        if pl > 0:
            qual = [l] + qual[pl:]
            costs = [n+1] + costs[pl:]
        pa = bisect(qual, a)
        if pa != 0:
            if pa < len(qual):
                qual[pa] = a
            else:
                qual.append(a)
                costs.append(costs[-1]-1)
            pr = bisect(qual, r)
            if pr < len(qual):
                qual = qual[:pr]
                costs = costs[:pr+1]
            res = min(costs)+n
            if res > n:
                return -1
            else:
                 return res
        for _ in range(int(input())):n = int(input());print(solve(n, [[int(a) for a in input().split()] for _ in range(n)]))

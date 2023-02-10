# Alice and Bob went to a pet store. There are N animals in the store where the ith animal is of type Ai?.

# Alice decides to buy some of these N animals. Bob decides that he will buy all the animals left in the store after Alice has made the purchase.

# Find out whether it is possible that Alice and Bob end up with exactly same multiset of animals.

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]
    b = Counter(nums)
    c = True
    for i in b:
        if b[i]%2==1:
            c = False
    if c:
        print("YES")
    else:
        print("NO")
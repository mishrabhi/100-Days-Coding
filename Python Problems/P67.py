# For her next karate demonstration, Arunima will break some bricks.

# Arunima stacked three bricks on top of each other. Initially, their widths (from top to bottom) are W1,W2,W3.

# Arunima strength is S. Whenever she hits a stack of bricks, consider the largest k≥0 such that the sum of widths of the topmost k bricks does not exceed S; the topmost k bricks break and are removed from the stack. Before each hit, Arunima may also decide to reverse the current stack of bricks, with no cost.

# Find the minimum number of hits Arunima needs in order to break all bricks if she performs the reversals optimally. You are not required to minimize the number of reversals.

for _ in range(int(input()))
s,w1,w2,w3 = map(int,input().split())
if(w1+w2+w3<=s):
    print(1)
elif(w1+w2<=s or w2+w3<=s):
    print(2)
else:
    print(3)
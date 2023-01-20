# No play and eating all day makes your belly fat. This happened to Manish during the lockdown. His weight before the lockdown was w1 kg (measured on the most accurate hospital machine) and after M months of lockdown, when he measured his weight at home (on a regular scale, which can be inaccurate), he got the result that his weight was w2 kg (w2>w1).

# Scientific research in all growing kids shows that their weights increase by a value between x1 and x2 kg (inclusive) per month, but not necessarily the same value each month. Manish assumes that he is a growing kid. Tell him whether his home scale could be giving correct results.

for i in range(int(input())):
    w1,w2,x1,x2,M = map(int,input().split(""))
    h = (w2-w1)
    s1 = x1 * M
    s2 = x2 * M
    if (h>=s1 and h<=s2):
        print("1")
    else:
        print("0")
# Let X be the set of all integers between 0 and n-1. Suppose we have a collection S1, S2, ..., Sm of subsets of X. Say an atom A is a subset of X such that for each Si we have either A is a subset of Si or A and Si do not have any common elements.

# Your task is to find a collection A1, ..., Ak of atoms such that every item in X is in some Ai and no two Ai, Aj with i ≠ j share a common item. Surely such a collection exists as we could create a single set {x} for each x in X. A more interesting question is to minimize k, the number of atoms.


for _ in range(int(input())):
    n,m=map(int,input().split())
    atomlist = ['']*n
    for k in range(m):
        s=[]
        s.extend(input().split()[1:])
        for w in range(n):
            if str(w) in s:
                atomlist[w]+="1"
            else:
                atomlist[w]+="0"
    print (len(set(atomlist)))
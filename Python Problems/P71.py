# There are N students in a class, where the i-th student has a score of Ai?.

# The i-th student will boast if and only if the number of students scoring less than or equal Ai? is greater than the number of students scoring greater than Ai?.

# Find the number of students who will boast.

t = int(input())
lc = []
for mml in range(0,t):
    l = int(input())
    jk = str(input())
    tp = []
    for kkc in jk.split(""):
        tp.append(int(kkc))
    lc.append(tp)

    for bb in lc:
        ofr = 0
        for iir in range(0,len(bb)):
            l = 0
            m = 0
            for kke in range(0,len(bb)):
                if bb[kke]<=bb[iir]:
                    l+=1
                else:
                    m+=1
                ifl>m:
                    ofr+=1
                    print(ofr)
# A string is called boring if all the characters of the string are same.

# You are given a string S of length N, consisting of lowercase english alphabets. Find the length of the longest boring substring of S which occurs more than once.

# Note that if there is no boring substring which occurs more than once in S, the answer will be 00.

# A substring is obtained by deleting some (possibly zero) elements from the beginning of the string and some (possibly zero) elements from the end of the string.

t = int(input())
for _ in range(t):
    d = {}
    n = int(input())
    s = input()
    mx = 0
    i = 0
    while(i<n):
        c = 1
        ss = s[i]
        while(i<n-1 and s[i]==s[i+1]):
            c+=1
            i+=1
            ss+=s[i]
            mx = max(mx,c-1)
            d[ss]=d.get(ss,0)+1
            if(d[ss]==2):
                mx = max(mx,len(ss))
                i+=1;
                print(mx)
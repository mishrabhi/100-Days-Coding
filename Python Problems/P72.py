# In this problem you will have to implement a simple editor. The editor maintains the content of a string S and have two following functions:
 

# "+ i x": insert a string x into the current string S after the i'th character of the S (we use 1-indexing in this problem). When i equals to 0 it mean we add x at the beginning of S.
# "? i len": Print the sub-string of length len starting at position i'th of S.
# At the beginning, the editor holds an empty string. There will be Q queries of the two types described above.

# Input

# The first line contains the integer Q. Each line in the next Q lines contains one query.

# Output

# For each query of the second type, print out the answer sub-string in one line.

def insert(string_s, insert_s, pos_i=0):
 return string_s[:pos_i] + insert_s + string_s[pos_i:]
q = int(input())
s = ''
for _ in range(q):
    query = input().split()
    c = query[0]
    i = int(query[1])
    if c == '+':
        sub = query[2]
        if i == 0:
            s = sub + s
        else:
            s = insert(s,sub,i)
    else:
        l = int(query[2])
        print(s[i-1:i+l-1])
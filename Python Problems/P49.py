# Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the minimum scalar product (Dot product) of 2 vectors.

def swap(vec1, pos1, pos2):
 vec1[pos1], vec1[pos2] = vec1[pos2], vec1[pos1]
def SpeecialSort(vec1,n):
 vec1.sort()
 idx=0
 while idx<n and vec1[idx] < 0 :
    idx=idx+1
 start = idx
 end = n-1
 while(start<end):
    swap(vec1, start, end)
    start = start + 1
    end = end + 1
def MinimumScalarProduct(vec1,vec2,n):
 sop=0
 for i in range(0,n):
    min = 2147483647
    for j in range(i,n):
        if(vec1[i]*vec2[j]) < min :
            min = vec1[i]*vec2[j]
            id1 = i
            id2 = j
    sop = sop + min
    swap(vec1,i,id1)
    swap(vec2,i,id2)
 return sop
n = int(input())
vec1 = list(map(int,input().split(' ')))
vec2 = list(map(int,input().split(' ')))
SpeecialSort(vec1,n)
print(MinimumScalarProduct(vec1,vec2,n))

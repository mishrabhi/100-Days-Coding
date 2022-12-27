# Get two strings as input from the user, first with wildcard characters (* and ?) and second without wildcard characters.
#Then check whether they match or not.

def solve(a,b):
    n,m=len(a),len(b)
    if n==0 and m==0:
        return True
    if n > 1 and a[0] == '*' and m == 0:
        return False
    if (n > 1 and a[0] == '?') or (n != 0 and m !=0 and a[0] == b[0]):
        return solve(a[1:],b[1:]);
    if n !=0 and a[0] == '*':
        return solve(a[1:],b) or solve(a,b[1:])
    return False

str1=input("First string with wild characters: ")
str2=input("Second string without wild characters: ")
print(solve(str1,str2))
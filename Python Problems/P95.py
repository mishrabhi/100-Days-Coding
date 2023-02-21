# Kulyash is given an integer N. His task is to break N into some number of (integer) powers of 2.

# To achieve this, he can perform the following operation several times (possibly, zero):

# Choose an integer X which he already has, and break X into 2 integer parts (Y and Z) such that X=Y+Z.
# Find the minimum number of operations required by Kulyash to accomplish his task.

def solve(num):
    if num==1:
        return 0
    else:
        return num%2+solve(num//2)
n=int(input())
for i in range(n):
    num=int(input())
    print(solve(num))
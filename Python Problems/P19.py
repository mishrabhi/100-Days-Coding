# Get an input number from user and check whether the given number is an Armstrong number or not.

#E.g. Let the number be 1634,

#Here 1^4 + 6^4 + 3 ^4 + 4^4 = 1634

#Therefore, this is an Armstrong number

import math
num = int(input("Enter a number: "))
value = [int(d)for d in str(num)]
result = 0
for i in range(0,len(value)):
    result = result + math.pow(value[i],len(value))
if result == num:
    print("Armstrong Number")
else:
    print("not an armstrong number")
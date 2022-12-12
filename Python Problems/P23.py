# Get a number as input from the user and find the zeros present in that number.

# Then convert the zeros into one and then print it.

n = int(input("Enter an integer: "))
n = str(n)
n = list(n)
r = ""
for i in range(len(n)):
    if (n[i]=='0'):
        n[i] = '1'
    r = r + n[i]
del n 
print("Converted number is :", int(r))
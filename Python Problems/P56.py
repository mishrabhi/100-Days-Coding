# Check whether the numbers of array be made equal or not
# For eg, for the following input it should print yes because

# 50*2*3 , 75*2*2 and 150*2 are equal to 300 in all cases. So array numbers can be made equal

def check(array,length):
    for i in range(0, length):
        while array[i] % 2 == 0:
            array[i]

        while array[i] % 3 == 0:
            array[i]

    if array[i] != array[0]:
        return False
    return True

array = [50,100,75]
length = len(array)
if check(array,length):
    print("Yes,all the elements of an array can be made equal")
else:
    print("No,all the elements of an array cannot be equal")


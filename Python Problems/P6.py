#Get the value of x and y coordinates as input from the user and check in which quadrant the point lies and print it.

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if (x<0 and y>0):
    print("Belongs to Ist quadrant")
elif(x>0 and y>0):
    print("Belongs to IInd quadrant")
elif(x<0 and y<0):
    print("Belongs to 3rd quadrant")
else:
    print("Belongs to 4th quadrant")
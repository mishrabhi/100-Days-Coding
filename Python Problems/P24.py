# Get the number of lines as the input and print stars in that many lines or rows in a pyramid shape.

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i + 1):
        print("*",end = "")
    print("\n")
# You are given the height H (in metres) and mass M (in kilograms) of Anusree. The Body Mass Index (BMI) of a person is computed as M/H^2.

# Report the category into which Anusree falls, based on his BMI:

# Category 1: Underweight if BMI ≤18

# Category 2: Normal weight if BMI ∈{19, 20,…, 24}

# Category 3: Overweight if BMI ∈{25, 26,…, 29}

# Category 4: Obesity if BMI ≥30

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=a/(b*b)
    if(c<=18):
        print(1)
    elif(19<=c<=24):
        print(2)
    elif(25<=c<=29):
        print(3)
    elif(30<=c):
        print(4)
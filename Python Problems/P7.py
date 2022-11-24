#Get the number of month and year as input from the user and check the number of days present in that month.

#Input
#Enter month : 2
#Enter year : 2000
#Output
#29

month = int(input("number of month: "))
year = int(input("enter the year: "))

if (month == 2 and (year%400 == 0) or ((year%100 !=0) and (year % 4 == 0))):
    print('Number of days is 29')
elif(month == 2):
    print("number of days is 28")
elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("Number of days is 31")
else:
    print("Number of days is 30")

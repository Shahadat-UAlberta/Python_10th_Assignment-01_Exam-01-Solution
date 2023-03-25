# 6. Write a Python program to check whether a year is leap year or not.

year = int(input("2021:"))

if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 == 0:
            print(str(year) + " is a leap year")
        else:
            print(str(year) + " is not a leap year")
    else:
        print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")

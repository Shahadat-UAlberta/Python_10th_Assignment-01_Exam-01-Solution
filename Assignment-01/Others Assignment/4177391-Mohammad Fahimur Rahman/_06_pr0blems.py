# Write a Python program to check whether a year is leap year or not.

# Any year that is evenly divisible by 4 is a leap year:

num1 = int(input())

if num1 % 4 ==0:
    print("leap year")
else:
    print("not leap year")
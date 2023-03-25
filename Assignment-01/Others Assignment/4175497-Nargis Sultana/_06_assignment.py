# Write a python program to check whether a year is leap year or not.

L= int(input("Enter the year"))
if (L%4==0 and L%100==0) or (L%400==0):
    print("The year is leap year")
else:
    print("The year is not a leap year")
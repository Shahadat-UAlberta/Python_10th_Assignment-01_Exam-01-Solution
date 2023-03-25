# Write a python program to check whether a number is negative, positive or zero.

A= float(input("Enter a number = "))
if A==0:
    print("The number is zero")
if A>0:
    print("The number is positive and the value is = %.2f"%A)
if A<0:
    print("The number is negative and the value is = %.2f"%A)


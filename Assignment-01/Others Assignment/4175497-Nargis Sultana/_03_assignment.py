# Write a python program to check whether a number is divisible by 5 and 50 or not.

a= int(input("Enter a number = "))
if a %5==0:
    print("The number is divisible by 5")
if a %50==0:
    print("The number is divisible by 50")
if a %5!=0 and a %50!=0:
    print("The number is not divisible by 5 nor 50")


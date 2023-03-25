# 4. Write a Python program to check whether a number is negative, positive or zero.

num= int(input("-3:"))

if num > 0:
    print(str(num) + " is positive")
elif num < 0:
    print(str(num) + "is negative")
else:
    print(str(num) + " is zero")
# 3. Write a Python program to check whether a number is divisible by 5 and 50 or not.

A = int(input())
if ((A%5==0) and (A%50==0)):
    print ("The Number %d is divisible by 5 and 50" %A)
else:
    print ("The Number %d is not divisible by 5 and 50" %A)
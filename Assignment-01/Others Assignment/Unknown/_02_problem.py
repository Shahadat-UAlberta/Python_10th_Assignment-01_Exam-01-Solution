# Write a Python program to find maximum between three numbers.

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 < num2 > num3:
    print("Num2 is greater than num1 & num3")
elif num2 < num1 > num3:
    print("Num1 is greater than num2 & num3")
elif num1 < num3 > num2:
    print("Num3 is greater than num1 & num2")
else:
    print("Out of Context.")
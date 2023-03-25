# 3. Write a Python program to check whether a number is divisible by 5 and 50 or not.

number = int(input())
if number % 5 == 0 and number % 50 == 0:
    print("The number is divisible by 5 and 50")
else:
    print("The number is not divisible by 5 and 50")

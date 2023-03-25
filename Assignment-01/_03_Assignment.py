# Write a Python program to check whether a number is divisible by 5 and 50 or not.

number = int(input())
if number % 5 == 0 or number % 50 == 0:
    print("Divisible")
else:
    print("Not divisible")
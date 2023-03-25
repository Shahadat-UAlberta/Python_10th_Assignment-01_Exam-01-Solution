# 3. Write a Python program to check whether a number is divisible by 5 and 50 or
def divisible_by_5_and_50(n):
    return n % 5 == 0 and n % 50 ==0
num=int(input("5:"))

if divisible_by_5_and_50(num):
    print(str(num) + " is not divisible by 5 and 50")
else:
    print(str(num) + " is  divisible by 5 and 50")

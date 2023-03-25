# 2. Write a Python program to find maximum between three numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b and a > c:
    print(f'The maximum is {a}')
elif b > c:
    print(f'The maximum is {b}')
else:
    print(f'The maximum is {c}')

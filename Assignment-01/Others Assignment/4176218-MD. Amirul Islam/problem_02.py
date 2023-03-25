# 2. Write a Python program to find maximum between three numbers.

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

if x > y and x > z:
    print(f'The maximum is {x}')
elif x > z:
    print(f'The maximum is {y}')
else :
    print(f'The maximum is {z}')
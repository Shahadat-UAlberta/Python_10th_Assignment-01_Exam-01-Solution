
# Write a Python program to find maximum between two numbers.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a > b:
   # print(f'The maximum number is: {a}')
    print("%.2f" % a)
else:
    # print(f'The maximum number is: {b}')
    print("%.2f" % b)

print("-----------------")

a = 200
b = 400
maximum = max(a, b)

print(maximum)



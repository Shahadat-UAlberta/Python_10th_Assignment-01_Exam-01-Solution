
# Write a Python program to find maximum between three numbers.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a > b :
    print("%.2f" % a)

if a > c:
    print("%.2f" % a)
elif b > c:
    print("%.2f" % b)

else:
    print("%.2f" % c)

print("-----------------")
a = 2
b = 4
c = 8
maximum = max(a, b, c)
print(maximum)
print("--------------------")

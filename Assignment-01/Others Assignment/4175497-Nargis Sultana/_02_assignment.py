# Write a python program to find maximum between three numbers.

a= int(input("Enter a number = "))
b= int(input("Enter the 2nd number = "))
c= int(input("Enter the 3rd number = "))

if a>b and a>c:
    print("A has the maximum value =%d" %a)
if b>a and b>c:
    print("B has the maximum value =%d" %b)
if c>a and c>b:
    print("C has the maximum value =%d" %c)

maximum = max(a, b, c)
print("The maximum value is = %d" % maximum)

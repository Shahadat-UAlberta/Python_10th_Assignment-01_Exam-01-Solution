# Write a python program to find maximum between two numbers.

a= int(input())
b= int(input())
if a>b:
    print("The maximum value = %d" %a)
else:
    print("The maximum value = %d" %b)

maximum= max(a,b)
print("The maximum value is= %d" % maximum)


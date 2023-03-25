# 2. Write a Python program to find maximum between three numbers.
def find_maximum(a,b,c):
    maximum=a

    if b> maximum:
     maximum=b

     if c > maximum:
       maximum=c

       return maximum

#Testing the function

print(find_maximum(10, 20, 30)) #output=30
print(find_maximum(10, 40, 70)) #output=70
print(find_maximum(10, 60, 80)) #output=80

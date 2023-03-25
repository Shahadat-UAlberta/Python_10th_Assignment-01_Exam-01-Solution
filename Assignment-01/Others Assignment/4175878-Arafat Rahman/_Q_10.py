# 10. Write a Python program to check whether a character is uppercase or lowercase alphabet.

char = input("A:")

if char.isupper():
    print(char + " is an uppercase alphabet")
elif char.islower():
    print(char + " is an lowercase alphabet")
else:
    print(char + " is not an alphabet")


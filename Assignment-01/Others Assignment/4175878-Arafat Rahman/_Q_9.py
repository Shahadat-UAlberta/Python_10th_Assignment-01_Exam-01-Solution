# 9. Write a Python program to input any character and check whether it is alphabet, digit or special character.

char =input("$:")

if char.isalpha():
    print(char + " is an alphabet")
elif char.isdigit():
    print(char + " is a digit")
else:
    print(char + " is a special character")



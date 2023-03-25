# Write a Python program to input any character and check whether it is alphabet, digit or special character.

num1 = input()

if num1.isalpha():
    print("Alphabet")

elif num1.isdigit() or num1.isnumeric():
    print("Digit")

else:
    print("spacial character")

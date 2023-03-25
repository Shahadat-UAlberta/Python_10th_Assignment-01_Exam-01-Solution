# 9. Write a Python program to input any character and check whether it is alphabet, digit or special character.

character = input("Enter any character: ")

if character.isalpha():
    print("The character is an alphabet")
elif character.isdigit():
    print("The character is a digit")
else:
    print("The character is a special character")
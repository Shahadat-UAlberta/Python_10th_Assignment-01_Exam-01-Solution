# 9. Write a Python program to input any character and check whether it is alphabet, digit or special character.

character = input("Enter any character: ")

if 'a' <= character <= 'z' or 'A' <= character <= 'Z':
    print("The character is an alphabet")
elif '0' <= character <= '9':
    print("The character is a digit")
else:
    print("The character is a special character")
# 7. Write a Python program to check whether a character is alphabet or not.

character = input("Enter a character: ")

if 'a' <= character <= 'z' or 'A' <= character <= 'Z':
    print("Character is alphabet")
else:
    print("Character is not alphabet")
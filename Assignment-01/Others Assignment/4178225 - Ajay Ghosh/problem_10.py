# 10. Write a Python program to check whether a character is uppercase or lowercase alphabet.

character = input("Enter a character: ")

if character.isupper():
    print("The character is uppercase.")
elif character.islower():
    print("The character is lowercase.")
else:
    print("The character is not an alphabet")

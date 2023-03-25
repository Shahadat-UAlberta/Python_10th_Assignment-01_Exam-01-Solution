# 10. Write a Python program to check whether a character is uppercase or lowercase alphabet.

character = input("Enter a character: ")

if 'A' <= character <= 'Z':
    print("The character is uppercase.")
elif 'a' <= character <= 'z':
    print("The character is lowercase.")
else:
    print("The character is neither uppercase nor lowercase.")

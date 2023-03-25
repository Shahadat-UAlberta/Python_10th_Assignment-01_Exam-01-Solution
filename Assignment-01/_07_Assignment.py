# Write a Python program to check whether a character is alphabet or not.

letter = input("Enter a character: ")

if 'a' <= letter <= 'z' or 'A' <= letter <= 'Z':
    print("Input is alphabet")
else:
    print("Input is not alphabet")
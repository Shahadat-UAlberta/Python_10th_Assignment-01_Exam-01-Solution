# 8. Write a Python program to input any alphabet and check whether it is vowel or consonant.

char = input("a:").lower()

if char in ['a','e','i','o','u']:
    print(char + " is a vowel")
else:
    print(char + " is a consonant")
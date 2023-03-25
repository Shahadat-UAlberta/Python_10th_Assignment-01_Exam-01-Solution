# 8. Write a Python program to input any alphabet and check whether it is vowel or consonant.
from re import U

alphabet = input("Enter any alphabet: ")

if (alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u'
        or alphabet == 'A' or alphabet == 'E' or alphabet == 'I' or alphabet == 'O' or alphabet == 'U'):
    print(f'\'{alphabet}\' is vowel')

else:
    print(f'\'{alphabet}\' is consonant')
print( "------ PROBLEM 8 -------")
# PYTHON PROGRAM TO INPUT ANY ALPHABET AND CHECK WHETHER IT IS VOWEL OR CONSONANT.

var81=input()

if var81 in {'a','e','i','o','u'} or var81 in {'A','E','I','O','U'}:
    print(f"The character {var81} is a vowel.")
else:
    print(f"The character {var81} is a consonant.")

print( "------ PROBLEM 9 -------")
# PYTHON PROGRAM TO INPUT ANY CHARACTER AND CHECK WHETHER IT IS ALPHABET, DIGIT OR SPECIAL CHARACTER:

num91=input()
if num91.isalpha():
    print(f"The given character '{num91}' is an alphabet.")
elif num91.isdigit():
    print(f"The given character '{num91}' is a digit.")
else:
    print(f"The given character '{num91}' is a special character.")
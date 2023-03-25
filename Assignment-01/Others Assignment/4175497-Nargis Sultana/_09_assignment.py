# Write a python program to check whether a character is alphabet or not.

character= input("Input any character: ")
if "a" <= character <= "z" or "A" <= character <= "Z":
    print("Its an alphabet")
elif "0"<=character<="9":
    print("Its a digit")
else:
    print("Its a special character")
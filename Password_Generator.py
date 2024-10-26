import random
def Generate(length):
    str="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$!&*"
    generatedpass=""
    for i in range(0,length):
        generatedpass+=random.choice(str)
    return generatedpass
try:
    length=int(input("Enter Length of the password: "))
    generatedpass=Generate(length)
    print(f"Generated Password is: {generatedpass}")
except ValueError:
    print("Enter a valid number")
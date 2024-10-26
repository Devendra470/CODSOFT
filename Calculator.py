def calculator(num1,num2,operation):
    if(operation=="+"):
        print(f"Addition is: {num1+num2}")
    elif(operation=='-'):
        print(f"Substraction is: {num1-num2}")
    elif(operation=='*'):
        print(f"Multiplication is: {num1*num2}")
    elif(operation=='/'):
        if(num2==0):
            print("Error Division by zero is not defined")
        else:
            print(f"Division is: {num1/num2}")
    else:
        print("Invalid Operation!")

try:
    num1=float(input("Enter first Number: "))
    num2=float(input("Enter Second Number: "))
    operation=str(input("Enter Operation to be performed(+,-,*,/): "))
    calculator(num1,num2,operation)
except ValueError:
    print("Please Enter Valid Numbers")


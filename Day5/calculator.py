#Create a function that defines a calculator and call the add,subtract,multiply and divide funct
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
def calculator(a,b):     
    print(f"Addition is :{add(a,b)}")
    print(f"Subtraction is :{subtract(a,b)}")
    print(f"Multiplication is :{multiply(a,b)}")
    print(f"Division is :{divide(a,b)}")
calculator(a,b)
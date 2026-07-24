#Create a function that calls factorial
def factorial(number):
    result=1
    for i in range(1,number+1):
        result=result*i
    return result
number=int(input("Enter the number :"))
print(f"Factorial is : {factorial(number)}")
    
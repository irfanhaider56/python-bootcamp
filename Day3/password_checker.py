correct_password="Irfan@12"
password=input("Enter the password: ")

if password=="Irfan@12":
    print("Access Granted")
else:
    print("Enter correct password")

#practice Questions
#Check whether a number is divisible by 5
number=int(input("Enter the number:"))
if number%5==0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

#Find the largest of two numbers
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
if number1>number2:
    print(f"Largest number is: {number1}")
else:
    print(f"Largest number is: {number2}")

#Check largest of three numbers
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
number3=int(input("Enter third number: "))
if number1>number2:
    if number1>number3:
        print(f"Largest number is: {number1}")
elif number2>number1:
    if number2>number3:
        print(f"Largest number is: {number2}")
else:
    print(f"Largest number is: {number3}")

#Check if a year is even or odd
year=int(input("Enter the year: "))
if year%2==0:
    print("Year is even")
else:
    print("Year is odd")

#Check whether a person can apply for driving licence
age=int(input("Enter the age of a person:"))
if age>=18:
    print("Eligible to apply for driving licence")
else:
    print("You are under 18")
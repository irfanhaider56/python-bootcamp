#Python basic syntax
print("hello world!")
print("My name is Irfan Haider")
print("I am learning python")
#Learning varibales(Variables are the containers 
# in which data types are stored)
name="irfan haider"
age=18
height=175
weight=50
print(name)
print(age)
print(height)
print(weight)
#Learning Data Types
name="irfan haider"     #str
age=18                  #int
cgpa=3.68               #float
is_student=True         #bool
#Check their types
print(type("irfan haider"))
print(type(18))
print(type(3.68))
print(type(True))
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))
#Learning how to give input in python
name=input("Enter your name: ")
print(name)
#We use input() and int(input()) bacause input only returns text, so get float,int we have to use them
age=int(input("Enter your age: "))
print(age)
#Mini_challenge:-
name=input("Enter your name: ")
age=int(input("Enter your age: "))
department=input("Enter your department name: ")
university=input("Enter your university name: ")
print(f"Welcome {name}!")
print(f"You are {age} years old")
print(f"You study {department}")
print(f"Your university is {university}")
#Practice Exercises
#print your name
print("Irfan Haider")
#print your age
print(22)
#store your city name in a variable and print it
city="Dera Ghazi Khan"
print(city)
#Store your cgpa in a variable and print it
cgpa=3.68
print(cgpa)
#Ask the user for their favourite color
color=input("What is your favourite color: ")
print(color)
#Ask for two numbers and print their sum
num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number"))
print(f" Your sum is :{num_1+num_2}")
#print the type of a string 
print(type("irfan haider"))
name="irfan"
print(type(name))
#print type of integer
print(type(18))
age=22
print(type(age))
#Print type of a float
print(type(3.68))
cgpa=3.68
print(type(cgpa))
#print type of a boolean
print(type(True))
student=True
print(type(student))
#Home work Challenge
name=input("What is your name: ")
age=int(input("What is your age: "))
fav_lan=input("What is your favourite programming language: ")
print("---Student Profile---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Language: {fav_lan}")


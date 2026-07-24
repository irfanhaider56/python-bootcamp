#Create a function that prints your favourite programming language
def fav_lan(x):
    print(f"My favourite language is : {x}")
fav_lan("Python")

#Create a function that returns the square of a number
def square(x):
    x=x*x
    print(x)
square(4)

#create a function that returns cube of a  number
def cube(x):
    x=x*x*x
    print(x)
cube(9)

#create a function that checks if a number is even 
def check_even(x):
    if x%2==0:
        print("Number is even")
check_even(3400)

#Create a function that returns largest of 2 numbers
def largest_num(x,y):
    if x>y:
        print(f"{x}")
    else:
        print(f"{y}")
largest_num(34,56)

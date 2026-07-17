#Nested_if
age=int(input("Enter your age: "))
citizen=input("Are you a citizen of pakistan? (yes/no) : ")
if age>=18:
    if citizen.lower()=="yes":
        print("You are eligible to vote")
elif age>=18:
    if citizen.lower()=="no":
        print("Citizenship required")
else:
    print("Too young to vote")
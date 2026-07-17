#Build a student result system
name=input("Enter the name of a student: ")
Roll_number=input("Enter the roll number of a student: ")
marks=int(input("Enter the marks of a student: "))
print("=========Student Result=========")
print(f"Name: {name}")
print(f"Roll No: {Roll_number}")
print(f"Marks: {marks}")


if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
elif marks>=60:
    print("Grade: D")
else:
    print("Grade: F")

if marks>=50:
    print("status: passed")
else:
    print("status: failed")
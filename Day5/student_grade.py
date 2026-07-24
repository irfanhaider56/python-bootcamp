#create a student grade function that returns grades of a student
def grade(marks):
    if marks>=90:
        return "A"
    elif marks>=80:
        return "B"
    elif marks>=70:
        return "C"
    elif marks>=60:
        return "D"
    else:
        return "F"
marks=int(input("Enter the marks of a student: "))
print(f"Your grade is :{grade(marks)}")

#Build a student attendance system
total_present=0
students_present=int(input("How many students are present: "))
for students in range(students_present):
    print(f"Student {students} is present")
    total_present+=1
print(f"Total students are present : {total_present}")
#Find pattern printing using loops
for rows in range(5):
    for coloums in range(rows+1):
        print("*",end=" ")            
    print()                           #Moves to the next row

#print numbers from 50 to 100
for i  in range(50,101):
    print(i)

#print  all multiples of 5 from 1 to 100
for i in range(1,101):
    if i%5==0:
        print(i)

#print the square of a number from 1 to 10
for i in range(1,11):
    square=i*i
    print(square)    

#Count how many numbers between 1 to 50 are even
count=0
for i in range(1,51):
    if i%2==0:
       # print("Even Number")
        count+=1
print(f"Total even numbers count are: {count}")

#Print the alphabet from A to Z 

for i in range(65,91):
    print(chr(i))

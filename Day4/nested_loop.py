#Nested loops are loops inside the loop
for row in range(3):
    for column in range(3):
        print("*", end=" ")
    print()    #this print() moves to next row

for row in range(6):
    for coloum in range(row):
        print("*",end=" ")
    print()
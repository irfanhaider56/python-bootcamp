#ask a user enter a number and then find multiplication table of that number
number=int(input("Enter the number:"))
for i in range(1,11):
    print(f"{number}x{i} = {number*i}")
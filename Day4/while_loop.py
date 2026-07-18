#A while loop runs as long as the condition is true
count=1
while count<=5:
    print(count)
    count+=1
        #Always update the variable count+=1 ,otherwise it will create infinite loop

#print numbers from 10 down to 1 using while loop
numbers=10
while numbers>=1:
    print(numbers)
    numbers-=1

#print "python" five times using while loop
count=1
while count<=5:
    print("python")
    count+=1

#print all numbers divisible by 3 between 1 and 30 using while loop
numbers=1
while numbers<=30:
        numbers+=1
        if numbers%3==0:
             print(numbers)

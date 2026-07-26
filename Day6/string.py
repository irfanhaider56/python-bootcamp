#Strings is a sequece of characters enclosed in quotes
name="Irfan Haider"
city="Multan"
print(name)
print(city)

#Strings Indexing __every character has an index
name="irfan haider"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

#Negative indexing
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])

#String Slicing ---- strings[start:end] ---- : used to tell what is starting and ending point
name="Irfan Haider"
print(name[0:4])
print(name[4:8])
print(name[:3])
print(name[3:])
print(name[:])

#Steps in slicing---- :: used for steps 
print(name[::2])
print(name[::-1])

#String length
name="Irfan Haider"
print(len(name))

#Membership operators---returns true or false
name="Irfan Haider"
print("an" in name)
print("Haider" in name)
print("khosa" in name)

#Strings methods
    #Uppercase method
name="Irfan Haider"
print(name.upper())
    #lowercase method
print(name.lower())
    #capitalize method
print(name.capitalize())
    #title method
print(name.title())

#strip method removes extra spaces
name="   Irfan Haider   "
print(name.strip())

#Replace method replace words
sentence="My name is Irfan Haider"
print(sentence.replace("Haider","Khosa"))

#find method
print(sentence.find("is"))

#count method----count gets at least one argument
print(sentence.count("a"))

#startwith and endwith method
print(sentence.startswith("My"))
print(sentence.endswith("er"))

#Split method is used to make list of random things
fruits="apple,banana,cake,mango"
print(fruits.split(","))

#Join method is used for reverse of split
fruits=['apple','banana','cake','mango']
print(",".join(fruits))

#check functions
print("Haider".isalpha())
print("123".isdigit())
print("Haider123".isalnum())

#String Concatination
first="Irfan"
last="Haider"
print(first+" "+last)

#String Reptition
print("Irfan \n"*10)

#F-Strings
name="Irfan Haider"
print(f"My name is {name}")

#Practice Exercises 

#Take your name as input and print original name,uppercase,lowercase and length
name=input("Enter your name: ")
print(name)
print(name.upper())
print(name.lower())
print(len(name))

#Take a sentence from the user and count how many times the letter "a" appears
sentence=input("Enter the sentence: ")
print(sentence.count("a"))

#Check whether a word start with "Py"
language="Python is a beautiful language"
print(language.startswith("Py"))

#Replace every space with "-"
language="I love Python"
print(language.replace(" ","-"))

#Reverse a string without using [::-1]
language="Python"
reverse=""
for char in language:
    reverse=char+reverse
print(reverse)
#Check whether a string is a palindrome
name="Irfan Haider"
print("Palindrome" in name)
#Count the number of vowels,consonants,digits and spaces in a sentence entered by the user
sentence=input("Enter the sentence: ")
vowels=0
consonants=0
digits=0
spaces=0
for char in sentence:
    if char.lower() in "aeiou":
        vowels+=1
    elif char.isalpha():
        consonants+=1
    elif char.isdigit():
        digits+=1
    elif char==" ":
        spaces+=1
print(f"Vowels are :{vowels}")
print(f"Consonants are :{consonants}")
print(f"Digits are : {digits}")
print(f"Spaces are : {spaces}")


#Write a program that asks the user to enter a password and checks whether :
#it has at least 8 characters, at least one uppercase letter ,one lowercase letter
#one digit and one special character such as @,#,$,! etc.
password=input("Enter the password : ")
uppercase=False
lowercase=False
digits=False
special_char=False
for char in password:
    if char.isupper():
        uppercase=True
    elif char.islower():
        lowercase=True
    elif char.isdigit():
        digits=True
    elif char in "@#$%^&*":
        special_char=True
if len(password) < 8:
     print("❌ Password must be at least 8 characters long.")
elif not uppercase:
    print("❌ Password must contain at least one uppercase letter.")
elif not lowercase:
    print("❌ Password must contain at least one lowercase letter.")
elif not digits:
    print("❌ Password must contain at least one digit.")
elif not special_char:
    print("❌ Password must contain at least one special character.")
else:
    print("✅ Password is strong.")
#Create a function of password validator
password="Irfan@!2"
def login(password):
    if entered_password==password:
        return "Acess Granted"
    else:
        return "Please, enter correct password"
entered_password=input("Enter password to login : ")
print(f"{login(password)}")

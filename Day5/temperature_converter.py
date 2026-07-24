#Create a function of temperature converter
def celsius_to_fahrenheit(c):
    F=(c*9/5)+32
    return F
c=int(input("Enter the temperature in celsius: "))
print(f"Fahrenheit is : {celsius_to_fahrenheit(c)}")
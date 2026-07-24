#Local variables will be called only where they are defined in any function while global variable will be 
#called everywhere in the program


def result():               #local variable
    x=10
    print(x)
result()

x=100
def result():
    print(x)
result()


#Multiple parameters
def info(name,age,city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
info("Irfan Haider",23,"D.G.Khan")
info("Rizwan Haider",20,"Nehal Wala")
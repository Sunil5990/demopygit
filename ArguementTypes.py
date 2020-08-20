def person1(name, age): #Formal Arguement
    print(name, end=" ")
    print(age-5)

def person2(name, age=18):  # Formal Arguement
     print(name, end=" ")
     print(age)
def sum(*b):
    #print(a)
    #print(b) # as b having multiple values so it will be a tuple
    #print(type(b))
    c = 0
    for i in b:
        c=c+i
    return c

person1('Sunil',28) #Actual Arguement: call using Position
person1(age=28, name='Sunil') #Call using keyword Arguement
person2('Sunil') # Default Arguement

x = sum(5, 6, 45, 78) # Variable Length Arguement
print(x)
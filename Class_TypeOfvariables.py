# Instance Variable
# Class Variable

class Car:
    wheels = 4 #Class/Static Var : belongs to Calss namespace
    def __init__(self,comp,mil):
        self.mil=mil #Instance Var : belongs to Instance namespace
        self.comp=comp #Instance Var : belongs to Instance namespace


c1 = Car("BMW",10)
c2 = Car("Suzuki",20)

Car.wheels=5

print(c1.comp,c1.mil,c1.wheels)
print(c2.comp,c2.mil,c2.wheels)
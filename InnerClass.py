class Student:

    def __init__(self, name, rollno,lap):
        self.name = name
        self.rollno=rollno
        self.lap=lap

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()


    class laptop:
        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram

        def show(self):
            print(self.brand,self.cpu,self.ram)
lap1 = Student.laptop("Acer",'i7',16)
lap2 = Student.laptop("HP",'i5',8)
s1 = Student('Sunil',2,lap1)
s2 = Student('Gautam',3,lap2)
s1.show()
s2.show()
#lap1 = s1.lap
#lap2 = s2.lap
#lap2 = Student.laptop()
#print(id(lap1))
#print(id(lap2))
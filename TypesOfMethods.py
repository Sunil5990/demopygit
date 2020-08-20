# Class Methods
# Instance Methods - Accessors methods(i.e. getters), Mutator Methods (i.e setters)
# Static Methods : to do something extra, not for class variables and instance variables

class Student:
    school = "JNV Hathras"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    @classmethod #Decorator for class methods
    def get_school(cls): #to get class variables in methods use lcs keywords, for instance var use self
        return cls.school

    @staticmethod #Decorator for static methods
    def info(): #Method nothing to do with Instance/Class variables so no need to have cls/self keywords
        print("This is Student Class.. in abc module")

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def get_m2(self):
        return self.m2

    def get_m3(self):
        return self.m3

    def set_m1(self,m1):
        self.m1=m1

    def get_m2(self,m2):
        self.m2=m2

    def get_m3(self,m3):
         self.m3=m3

s1 = Student(75,98,96)
s2 = Student(78,97,85)

print(s1.avg())
print(s1.get_m1())
s1.set_m1(88)
print(s1.get_m1())
print(Student.get_school())
Student.info()
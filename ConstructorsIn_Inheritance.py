# super method to call super class constructor, methods
#MRO: Method resolution order - Self then left to right (used in case of multiple inheritance)
class A:
    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B:
    def __init__(self):
        #super().__init__()
        print("in B Init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")
#a1=A()
#b1=B()
c1=C()
#b1.__init__()
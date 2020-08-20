#Single level Inheritance: A->B i.e B is child of A
#Multi level Inheritance: A->B->C i.e B is child of A and C is child of B
#Multiple Inheritance: A,B-> C is hild of both independent classes A and B

class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B: #Single level Inheritance
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):
    def feature5(self):
        print("Feature 5 working")


a1=A()
a1.feature1()
a1.feature2()
b1 = B()
c1=C()

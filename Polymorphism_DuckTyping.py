# for object ide in this case thing matter is method execute, if we change the type of object it behaves like that and
#code of class laptop works without any change
class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()


ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)
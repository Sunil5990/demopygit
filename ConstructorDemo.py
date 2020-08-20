class Computer:
    def __init__(self):
        self.name = "Sunil"
        self.age=28

  #  def update(self):
   #     self.age=30

    def compare(self, other):
        if self.age==other.age:
            return True
        else:
            return False

c1 = Computer()
print(c1.__sizeof__())
c2 = Computer()
c2.name="Gautam"
#print(c1.name)
#print(c2.name)

#c1.update()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c2.age)
print(c1.age)
# Abstract class in Python should be sub class of ABC class
# Class having atleast 1 abstract method is called abstract class
# Instance can not be created for abstract class. (i.e. Abstract class don have objects)
#Abstract methodshaving only declaration
#
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Its Running")

#com=Computer()
lap1=Laptop()
lap1.process()
#com.process()
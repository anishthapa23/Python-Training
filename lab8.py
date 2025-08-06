#calculate exponents using decorators
"""def exponents(func):
    def wrapper(*args,**kwargs):
        results = func(*args,**kwargs)
        return results **2
    return wrapper
@exponents
def calculator(a,b):
    return (a+b)

print(calculator(10,20))

#@property -> use for the lastname and firstname = fullname
class person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
obj1 = person("Anish", "Thapa")
print(obj1.firstname)
print(obj1.lastname)
print(obj1.fullname)
"""
#4 pillars of OOP -> Encapsulation, Inheritance, Abstraction and Polymorphism

#inheritance -> parent class -> properties and methods -> child class
class parent:
    def __init__(self,lastname):
        self.lastname = lastname

    def hello(self):
        print("Family name: ",self.lastname)

class Child(parent):
    
    def __init__(self, firstname,lastname):
        self.firstname = firstname
        super().__init__(lastname)#super le parent class ko constructor lai call garcha.
        print(f"{self.firstname} {self.lastname}")
    
    def hi(self):
        print("First name: ",self.firstname)

obj2 = Child("Anish","Thapa")
obj2.hello()
obj2.hi()


# wap to create a parent class named Classes with attribute like class_name section and have to 
# inherit it to child class named Students with attributes like name, age, and methods like study, 
# attend_class, and display_info using constructor and use super() to access parent class attributes and methods

class classes:
    def __init__(self,class_name):
        self.class_name = class_name
        print("Hello",self.class_name)
    
class Student(classes):
    def study(self,name, age,class_name):
        self.name = name
        self.age = age
        print(f"{self.name},{self.age}")
obj3 = Student("Tribal Chief")
obj3.study("Roman",22)


#encapsulation in python
#hi = "hello" #public -> can access anywhere
#hi = "hello" #protected -> can access 
#hi = "hello" #private -> getter and setter to get it

"""class Bank:

    def __init__(self,_name,_balance):
        self._name = _name #"__"double underscore in variable shows fully private variable
        self._balance = _balance

    @property
    def getbalance(self):
        return self._balance
    
    @getbalance.setter
    def setbalance(self,balance):
        self._balance = balance
    def _calculateminbalance(self):
        return self._balance > 500

user1 = Bank("Anish", 1000)
print(user1._name)
print(user1.getbalance)
user1.getbalance = 2000
print(user1.getbalance)
"""

# abstraction in python -> hidding complex logic from user
from abc import ABC, abstractmethod
class Coffee(ABC):
    def makeCoffee(self):
        self.gason()
        self.addCoffee()
        self.addMaterials()
        self.servein()

    @abstractmethod
    def gason(self):
        pass
    @abstractmethod
    def addCoffee(self):
        pass
    @abstractmethod
    def addMaterials(self):
        pass
    @abstractmethod
    def servein(self):
        pass

class Espresso(Coffee):
    def gason(self):
        print("coffee machine on")
    def addCoffee(self):
        print("addCoffee beans and exxtract it")
    def addMaterials(self):
        print("water, sugar and milk")
    def servein(self):
        print("serve in cup")
    
class Cappuccino(Coffee):
    def gason(self):
        print("coffee machine on")
    def addCoffee(self):
        print("extracted coffee powder")
    def addMaterials(self):
        print("water, sugar and milk")
    def servein(self):
        print("serve in cup")

exp = Espresso()
exp.makeCoffee()

cap = Cappuccino()
cap.makeCoffee()




#Concept of oop using python.
#This is the programming paradigm based on the concept of program
#Programming paradigm => 
#class, object, methods, attributes, decorators, constructor, magic/dunder methods
#4 Pillars -> inderitance, encapsulation, polmorphism, abstraction
#class -> building block f oop, blueprint for creating objects

"""class Abc:
    #class attributes/properties,/variables, methods and constructor
    name = "Anish"
    age = 22
    gender = "Male"

    def printDetails(self):
        print(f"Name: {self.name}, Age:  {self.age}, Gender: {self.gender}")
        #until decorators use garidaina should use self in every function inside class.

    def world(a,b,c):
        print("Hello World!")
        print(a , b , c) 

#object -> instance of a class, contains attributes and methods
one = Abc()
print(one.age)
print(one.name)#Anish
one.name = "John"
print(one.name)#John
print(one.gender)

one.printDetails()
one.world(2,4)
"""
#wap to create a class named hello with attribute like name, model, year and methods like start, stop, and display info

"""class hello:
        name = "BMW"
        model = "X5"
        year = 2025
#constructor -> magic method runs when the object is created
        def __init__(self,name, model, year):
             print("This is constructor")
             self.name = name
             self.model = model
             self.year = year
        def start(self):
            print("Car started")
        def stop(self):
            print("Car stopped!")
        def display(self):
            print(f"Name: {self.name}, Model: {self.model}, Year: {self.year}")

two = hello("Mercedes", "GlC 200", "2003")
two.start()
two.stop()
two.display()
"""
"""#wap to create a class named student with attrubutes like name, age, and methods 
# like study, attend, class and display info using constructor
class Student:
     def __init__(self,name, age):
          self.name = name
          self.age = age
          print(f"Name: {self.name}, Age: {self.age} ")
     def study(self):
          print("Studying! ")
     def attend(self):
          print("Attended! ")
     def classes(self):
          print("Regular in class! ")

hi = Student("Aneesh", 22)
hi.study()
hi.attend()
hi.classes()
"""

"""class ones:
    two = "This is method one"
#normal method
    def one(self):
        print( "This is one.")
#class method

    @classmethod #methi bhako properties lai cls use garera use garna sakincha
    def twos(cls):
       print(f"This is class method {cls.two}")

#static method
    @staticmethod
    def threes(a,b):
        print(f"Static method: {a+b}" )
     
ones.twos()
ones.threes(10,20)
   """     
def add_five(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 5
    return wrapper
@add_five#decorators to run function 
def add_numbers(a):
    return a
print(add_numbers(10))

from abc import ABC, abstractmethod

class Teahouse(ABC):
    
    def processCompleted(self):
        self.order()
        self.addingMaterials()
        self.serve()

    @abstractmethod
    def order(self):
        pass

    @abstractmethod
    def addingMaterials(self):
        pass
    
    @abstractmethod
    def serve(self):
        pass

class milkTea(Teahouse):
    def order(self):
        print("Ordering milk tea!")
   
    def addingMaterials(self):
        print("Adding milk,sugar,teapowder")

    def serve(self):
        print("Serving!")

class blackTea(Teahouse):
    def order(self):
        print("Ordering black tea!")
    
    def addingMaterials(self):
        print("Adding water,sugar,teapowder")

    def serve(self):
        print("Serving!")
user1 = milkTea()
user1.processCompleted()

user2 = blackTea()
user2.processCompleted()


#polymorphism -> 

class Human:
    def walk(self):
        print("Walking! with 2 legs")

class Lion:
    def walk(self):
        print("Walking with 4 legs!")

class Dog:
    def walk(self):
        print("Walking with 4 legs!")

obj1 = Human()
obj2 = Lion()
obj3 = Dog()

for i in [obj1, obj2, obj3]:
    i.walk()

"""
#error handling and exception handling
#try, except, else, finally

try:
    a= int(input("Enter a number: "))
    print(a)
#except ZeroDivisionError:
#   print("Can't divide!")
except Exception as e:
    print(e)

else:
    print("Code is working!")
finally:
    print("Code Works! ")

"""

#wap using try, except, else, finally print the number is odd or not by using input from the user
def num():
    try:
        a=int(input("Enter a number: "))
        if(a%2!=0):
            print("It is odd!")
        else:
            print("It is not odd!")
    except Exception as e:
        print(e)
    else:
        print("It works!")
    finally:
        print("Code is working!")

num()



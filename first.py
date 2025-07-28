#python first class 
"""
Halka History!
Guido can rossan - 1988
High level, indentation programming language

Unlike many other programming languages that use curly braces 
or keywords to define code blocks,
Python uses indentation to indicate the structure and scope of code.
indentation - aghadi halka gap aaunu.

Aja halka basic syntax matra ho 
Data types, operator and operands.

reserve words -> if, try, except, else, def, finally, class, as, elif, type, pass

"""

print("Hello Sansar!")
a = 10
a = "Aneesh"
print(a)
print(type(a))#to know the data type of variable.
if True:
    pass #indentation works as a paramerter.
#camelCase; can be used
"This is also a comment because no any variable is assigned."
"""
    Sting - collection of characters in ''," ",""" """

"""
b = ''' this also can be printed

jei order can lekheko cha tei ma print huncha 
        console ma'''
print(b)

c = "Hello"
d = "Everyone!"
print(c+d) #to concatinate two string.
age = "22"
print("My name is " + a + " and age is " + age )

#int
num1 = 10
num2 = 20
print(type(num1))
print(num1+num2)

#complex
j = 10
num3 = 1+2j
print(type(num3))
print(num3)

#bool -> True or False
print(type(True))
print(False)

#none 
noValue = None
print(noValue)
print(type(noValue))

#Array -> list -> collecion of items
list1 = [1,2,3,4, True, 5.5, "Aneesh"]
#index -> 0; length -1
#length -> (0,6)
print(list1)
print(list1[6])
print(type(list1))

#tuple -> collection of items
tup1 = (1,2,3,4,5, "aneesh")
print(tup1)
print(tup1[2])
print(type(tup1))

#set -> collection of unique value
set1 = {1,2,3,4,5,1,2,3}#use {} in set
print(type(set1))
print(set1)#same aako value haru remove garcha

#dict -> collection of keys and values pairs
dict1 = {
    "name" : "Aneesh",
    "age" : "22",
    "gender" : "Male"
} 
print(dict1)
print(type(dict1))
print(dict1.values())
print(dict1.keys())
print(dict1["name"])

#Type conversion and ask input from the user
names = input("Enter your name: ")
print(type(names))
print(names)
"""string -> str()
int -> int()
float -> float()
complex -> complex()
boolean -> bool()
list -> list()
tuple -> tuple()
set -> set()
dict -> dict()"""

num11 = int(input("Enter 1st number: "))
num22 = int(input("Enter 2nd number: "))
print(num11+num22)
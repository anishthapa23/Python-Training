#operators and operands
print(5+5)
#operand -> numbers=5
#operator -> +
#python has 7 operator:

#Arithmetic operator
print("sub",5-5)
print("mul",5*5)
print("div",5/5)
print(5%5) #remainder
print(5**2) #power
print(5//5) #value je ma cha tesmai division bhayera aaucha value.

#wap to print the sum of two number by asking input from the user
"""a=input("Enter first number: ")
b=input("Enter second number: ")
print(sum = a+b)"""

#f -> string ()
print(f"The sum of two number is {5+6}")#string bhitra nai operation garna milxa.
# =,+=,-=,**=

#Assignment operators
a=10
print(a)
a *= 10
print(a)
a **=2
print(a)
a %=2
print(a)
print(20**20)

#comparison operator -> always in boolean
# ==, >, <, >=, <=
print(5==5) #true
print(5>5) #false
print(5<5) #false
print(5<=5) #true

#logical operator -> and, or, not
#and
print(True and True) #true
print(True and False) #false
print(False and False) #false
print(False and True) #false
#or
print(True or True) #true
print(True or False) #true
print(False or False) #false
print(False or True) #true
#not
print( not True)
print( not False)

#identity operator -> is. output in boolean 
a=20
b=20
print(a is b)
print(a is not b)

#Membership opeators -> in and not in -> boolean
#list ma value xa ki nai check garinxa
list1 = {1,2,3,4}
print(4 in list1)
print(5 not in list1)

#bitwise opeator -> |, &, ^
print(5&6)
# 5 -> 0101
# 6 -> 0110
# output 4

#ternary operator
age = 20
print("above 18" if {age>18} else "below 18")

#wap to print the number is odd or not by asking input from the user
num = int(input("Enter a number: "))
print("Is even" if num%2==0 else "Is odd")

#wap to print if the user can drive or not
age = int(input("Enter our age: "))
print("Can drive" if age>=18 else "Can't Drive")

#Conditions in python
#if, else, elif, match
value = 2
if (value%2 != 0):
    print("The given value is Odd")
elif(value == 0):
    print("Value is 0")
elif(value > 100):
    print("The value is above 100")
else:
    print("The given value is Even")

#wap to print if the given value is rizz, buzz, or rizzbuzz conditions are 
#rizz -> number divide by 3
#buzz -> number divide by 7
#rizzbzz -> number divide by both 3 and 7
num = int(input("Enter a number: "))
if(num%3==0 and num%7==0):
    print("The number is rizzbuzz.")
elif(num%3==0):
    print("The number is rizz.")
elif(num%7==0):
    print("The number is buzz.")

#Match Statement
day = "Tuesday"
match(day):
    case "Sunday":
        print("Is Sunday")
    case "Tuesday":
        print("Is Tuesday")
    case"Friday":
        print("Is Friday")
    case _:
        print("none of the above") 


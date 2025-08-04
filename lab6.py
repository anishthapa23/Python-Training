#list comprehension in python -> ouptput is a list
#like terrnary operator similar to one line code 
list1 = [1,2,3,4,5,]
for i in list1:
    print(i * 2)

#expression -> expression for item in iterable
#expression -> expression for item in iterable if condition
output1 = [i*2 for i in list1 if i %2 ==0]
print(output1)

#wap to print the square of even numbers from 1 to 100

op = [i**2 for i in range(0,101) if i%2==0]
print(op)

#wap to print the multiplication table of 7 using list comprehension
[print(f"7 * {i} =  {7*i}") for i in range (1,11)]

#calculator app using fun -> add, sub, div, mul, **, //, %, exit and ask the 3 input for the user 2 will be numbers 
#and will be option and use recurion to call the function again and again until the user wants to exit.

def add(a,b):
    print("Sum = ",a+b)
def sub(a,b):
    print("Sub = ",a-b)
def mul(a,b):
    print("Mul = ",a*b)
def div(a,b):
    print("Div = ",a/b)
def square(a,b):
    print("Square = ",a**b)
def rem(a,b):
    print("Rem = ",a%b)
def division(a,b):
    print("Division = ",a//b)

a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Remainder")
print("7. RemDivision")
print("8. Exit")

while True:
    choice = int(input("Enter number to perform operation: "))
    if(choice > 8):
        print("Enter between 1-8: ")
    else:
        break


match(choice):
    case 1:
        add(a,b)
    case 2:
        sub(a,b)
    case 3:
        mul(a,b)
    case 4:
        div(a,b)
    case 5:
        square(a,b)
    case 6:
        rem(a,b)
    case 7:
        division(a,b)
    case 8:
        print("Thank you! ")
        exit
"""
# list comprehension in python -> output is a list
# like ternary operator similar to one line code ok
list1 = [1,2,3,4,5]
for i in list1:
    print(i * 2)

# expression -> [expression for item in iterable ]
# expression -> [expression for item in iterable if condition]
output1 = [i*2 for i in list1 if i % 2 == 0]
print(output1)

# wap to print the square of even numbers from 1 to 100
output1 = [i**2 for i in range(0,101) if i % 2 == 0]
print(output1)
# wap to print the multiplication table of 7 using list comprehension
[print(f"7 * {i} = {7*i}") for i in range(1,11)]
# calculator app using fun -> add, sub, div, mul, **, exit and ask the 3 input for the user 2 will be numbers and 1 will be option and use recurstion to call the function again and again until the user wants to exit
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def div(num1, num2):
    return num1 / num2
def mul(num1, num2):
    return num1 * num2
def expo(num1, num2):
    return num1 ** num2

def caluculator():
    print("welcome to Calculator app")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exponentiation")
    print("6. Exit")
    options = int(input("Select Your Options: "))
    list_of_options = [1,2,3,4,5]
    if options in list_of_options:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if options == 1:
            print(f"Result: {add(num1, num2)}")
        elif options == 2:
            print(f"Result: {sub(num1, num2)}")
        elif options == 3:
            print(f"Result: {div(num1, num2)}")
        elif options == 4:
            print(f"Result: {mul(num1, num2)}")
        elif options == 5:
            print(f"Result: {expo(num1, num2)}")
    else:
        print("Exiting the calculator app")
        return
    

caluculator()
"""


#Python -> 
#def -> A block of code run when the it is called

def hello():
    print("Hello Everyone!")

hello() #calling the function
#function -> parameter, arguments
def printName(name):
    print(f"Hello World {name}")#biccha ma kunai variable print garnu cha bhane use fstring

printName("Aneesh")

#return statement
def add(a,b):
    return a+b
print(add(2,2))
#no parameter but return statement
name = "Sarthak"
def getinfo():
    return f"Hello World {name}"
print(getinfo())

#function types -> return, no return 
#1. no parameter, no return 
#2. parameter, no return 
#3. no parameter, return 
#4. parameter, return 

#parameter type in python func
#1. Default parameter -> in this function we set the default value

def defaultPrameter(a=10, b=0):
    print(a+b)

defaultPrameter() #Uses default values
defaultPrameter(30) #b = 0
defaultPrameter(30,10) #Uses provided value

#wap t print the power of two numbers using default parameter
def defParameter(a=2, b=25):
    print(a**b)

defParameter() #uses default values
defParameter(9) #uses provided value

#2. Positional parameter

def normalFu(name, age):
    print(f"My name is {age} and age is {name}")

normalFu("Anish",22) #positional argments


#2. Named paramter
normalFu(age= 22,name="Anish")

#3. * args parameter -> multiple arguments
def abc(a,b, *args):
    print(a,b)
    for i in args:
        print(i)
abc(10,20,30,40)

#4. **kwargs paramter
def abc(*args, **kwargs):
    print(args)
    print(kwargs)

abc("Jhapa" "Nepal" "Dubai", name="Anish",age=27,city="kathmandu")


#wap to use all the parameter tyes in a single functtion

def para(a,b,*args,**kwargs):
    print(a+b)#uses default parameter
    print(args)#args
    print(kwargs)#kwargs
para(10,20,"Dog", 5, "Lion",game = "UFC", player = "Brock", KO = "Suplex")


def abcd(a,b,c, *args, **kwargs):
    print(f"a : {a}, b : {b}, c : {c}")
    print("Additional args: ", args)
    print("Keyword args: ",kwargs)

abcd(10,20,30,40,50, name = "Roman", age = 45, gender = "Male")

#def -> lambda function -> anonymous function
x = lambda : 22 #lambda ma by default return huncha
print(x())
adds = lambda a,b : a+b
print(adds(10,20))

#wap to print the given value is even or odd using lambda function
a = lambda num : f"The given number is even" if num%2==0  else "The given number is odd."
print(a(int(input("Enter a number: "))))


#recursion -> function calling itself
def rec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n + rec(n-1)
print(rec(10))







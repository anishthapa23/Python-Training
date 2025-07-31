#Dict in python -> consists of keys and values pairs
"""dict1 = {
    "name" : "Aneesh THapa",
    "age": 21,
    "gender": "male"
         }
print(dict1)
print(dict1["age"])
dict1["age"] = 22
print(dict1["age"])
#dict methods ->
print(dict1.keys())#prints only keys (name,age,gender)
print(dict1.values())#prints only values 
print(dict1.items())#prints all items
print(dict1.get("age"))
dict1.pop("age")
print(dict1)
#update
dict1.update({"name":"Aneesh Thapa","age": 22, "gender": "Male"})
print(dict1)

#WAP to print the keys and values in the dict(name:"John Doe")
for keys, values in dict1.items():
    print(f"{keys}: {values}")

"""

#loop in python -> continuous execution of a block of code until the condition is met
#for loop -> while loop -> nested loop
#breaking statement -> break, continue, pass
#Data type -> range(start, stop, step)
#range(0,100,2)
print(range(0,10,2))

for i in range(0,11,2):
    print(i)

#print(hello world 100)
print("Hello World",0)
print("Hello World",100)
#using for loop
for i in range(0,101):
    print("Hello World",i)

#while loop
#while (condition):
#code block  -> print, increment/decrement

i=0
while(i<=101):
    print("Hello Everyone!",i)
    i+=1

# Wap to print the even numbers from 0 to 100
for i in range (0,100):

    if(i==0):
        print("it is zero.")
    elif(i%2==0):
        print(i," is even.")
    else:
        print(i," is odd.")
# wap to print multiplication table of 7
for i in range (0,11):
    num = 7
    print("7 * ",i ,"=", num*i)
# wap to print the fibonacci series from 0 to 100 
a=0
b=1
print(a)
print(b)
c=a+b
for i in range(3,10):
    print(c)
    a=b
    b=c
    c=a+b
    i=i+1

# wap to print the factorial of a number of your choice
fact=1
num=int(input('enter number'))
if num==0:
    print(0)
elif num==1:
    print(1)
else:
    for i in range(1,num+1):
      fact*=i
    print(fact)

# wap to print the sum of all the numbers from 0 to 100
sum = 0
for i in range(0,101):
    sum = sum+i
    print(sum)
# wap to print the fizz if number is divisible by 3, buzz if number is divisible by 5,
#  fizzbuzz if number is divisible by both 3 and 5 from 0 to 100
for i in range(0,101):
    if(i%3==0 and i%5==0):
        print(i, "is fizzbuzz.")
    elif(i%3==0):
        print(i, "is fizz.")
    elif(i%5==0):
        print(i, "is buzz.")

# wap to print the reverse of a number
rev=0
num = 122
rem=num%10
rev=rev*10+rem
num = num/10
print(rev)



#pattern programming
"""
*
**
***
****
*****
******
"""
for i in range(0,6):
    for j in range(i):
        print("*",end=" ")
        print()

#break
for i in range(0,11):
    if(i==5):
        break
    print(i) #will print numbers from 0 to 4
#continue
for i in range(0,11):
    if (i==5):
        continue
    print(i)
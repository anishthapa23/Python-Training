#String manipulation
"""print("Aneesh \n Thapa")
print("Anish \\ Thapa")
print("Anish\tThapa")
print("My name is Anish")
name = "Anish Thapa"

#String slicing
print(name[0])
print(name[0:6])
print(name[-1: -4: -1])
print(name[::-1])#reverse

#String methods
#.upper(), .lower(), .titlt(), .capatilize(), .strip(), .replace(), .find(), .count()
one = "two"
two = "three"
three = "four"
print(one.upper())
print(one.lower())
print(one.strip())#remove leading and trailing whitespace
print(one.capitalize())
print(one.replace("two" , "one"))#replaces two with one
print(two.count("t"))#count the occurance of t in a string
print(three.split())#split the string into list at each space
print(one.istitle())#false
print(three.isupper())#false
print(two.isalpha())#true(contains no space = true)
print(two.isalnum())#false (contains num ,space and letter in string)

#wap to print if the given value is palindrome or not
a = "121"
b = a[::-1]
if(a==b):
    print("The number is a palindrome.")
else:
    print("The number is not palindrome.")

#list in python
list1 = [1,2,3,4,5]
print(list1)
#methods
print(list1.index(5))
list1.append(6) #adds to last value
print(list1)
list1.insert(0,7)#adds value in the index
print(list1)
list1.pop()#remove last index
print(list1)
list1.remove(3) #value to be removed
print(list1)
list1.sort()#sorts the list in ascending order
print(list1)
list1.sort(reverse=True)#sorts the list in descending order
print(list1)
list1.clear()#clear all items in list
print(list1)

#TUPLE (value can't be changed)
tup1 = (1,2,3,4,5,6)
print(tup1)
print(tup1.count(1))#counts the occurance of 1 in tuple
print(tup1.index(3))#Returns the index of the first occurance 
"""
#wap to add items in tuple by converting the tuple to list use append to add the item the provide and value in table
tup2 = (1,2,3,4)
list2 = list(tup2)#converts tup2 in list
list2.append(5)
tup2 = tuple(list2)#converts list into tuple.
print(type(tup2), tup2)
for i in tup2:
    print(i)
for i in list2:
    print(i)

#set -> collection of unique value
set1 = {1,2,3,4,5,6,7,4,2,1}
print(set1)#duplicate value print gardaina

#methods in set
#add, remove, clear, pop, intersecion, difference
set1.add(11)#adds 11 in set
print(set1)
set1.remove(1)#remove 1 from set
print(set1)
set1.pop()#remove first index
print(set1)
set2 = {5,6,7,8,9}
set3 = set1.union(set2)#union of set1 and set2
print(set1)
set4 = set1.intersection(set2)#intersection of set1 and set2
print(set1)
set5 = set1.difference(set2)#difference of set1 and set2
print(set1)
set1.clear()
print(set1)
for i in set1:
    print(i)

#wap to print the unique item in the list using set 
list1 = [1,2,3,4,5,5,2]
set1 = set(list1)#converts list into set
set7 = set1.intersection(set1)
print(set7)









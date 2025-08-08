#with -> open and close
"""
with open("hello.txt","w+") as fs:
    for i in range(1,11):
        fs.write(f"7 * {i} = {7*i}\n")
    fs.seek(0)
    print(fs.read())
fs.close()

#wap to print the table for 0 to 10 in separate file usig file handling
for i in range (0,11):
    with open(f"file{i}.txt","w+") as fi:
        for j in range(0,11):
            fi.write(f"{i} * {j} = {i*j}\n")
        fi.seek(0)
        print(fi.read())
    fi.close()

"""

#__init__ -> constructor
#dunder function
#__str__ -> string representation(return is used always)
#__len__ -> length
#__add__ -> addition
#__sub__ -> subtraction
#__mul__ -> multiplication


class one:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
       return f"Name: {self.name}\n Age: {self.age}"
One = one("Anish",22)
print(One)









#File Handling -> create, update, delete and read file 
#mode -> r,w,a, r+ , w+, a+, b(binary)
#delete -> os -> modules import -> delete
#r -> read -> must be existing file
"""
ts = open("hello.txt",mode="r")
#read properties -> read(), readline(), readlines()
print(ts.read())
#print(ts.readline())
#print(ts.readlines())

ts.close()
"""

#w => write -> existing file not needed it can be created itself
fs = open("hello.txt",mode="w")
fs.write("Hello Dada!")
print("File is updated!")
fs.close()

#w+ => write and read -> existing file not needed it can be created itself
fs = open("hello.txt",mode="w+")
fs.write("Hello Everyone!")
print("File is updated!")
fs.seek(0)#cursor move into zero th index
one = fs.read()
print(one)
fs.close()

#a+ -> append mode
fs2 = open("hello.txt",mode="a+")
fs2.write("Aneesh")

#delete -> remove
import os
os.remove("hello.txt")#error occurs if no file is created

for i in range(0,11):
    f=open(f"file{i}.txt","w")


#wap to print the table of 7 using file handling
#wap to print the table for 0 to 10 in seprate file using file handling

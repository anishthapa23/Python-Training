# make a program using oop concept by create a class name Student and make a constructor and function base also need to ask input from the user with options like add new student,( update student and delete student ) using roll no, show all students and exit, also make a menu for the user and use while loop to call the function again and again until the user wants to exit need to record file in txt format and also need to save the data in the file and load the data from the file.

import os
class Studnet:
    def __init__(self,std_name,std_roll,std_age):
        self.std_name=std_name
        self.std_roll=std_roll
        self.std_age=std_age

    
    def updateNew(self):
        pass
    def deleteStd(self):
        os.remove("studnet.txt")
    def printDetails(self):
        try:
            with open("student.txt","r") as fs:
                print(fs.read)
            fs.close()
        except FileNotFoundError as e:
            print(e)

    def exit(self):
        print("Thank you for visiting!")
        exit

try:
    with open("student.txt","w") as fs:
        std_name = (input("Enter a name of student: "))
        std_roll = int(input("Enter roll no. : "))
        std_age = int(input("Enter age of student: "))
        fs.write(std_name,std_roll,std_age)

except Exception as e:
    print(e)
std = Studnet(std_name,std_roll,std_age)

print("Menu to modify: ")
print("1. Update")
print("2. Delete")
print("3. Print Details")
print("4. Exit")
choose = int(input("Enter your option: "))

match(choose):
    case 1:
       std.updateNew()
    case 2:
        std.deleteStd()
    case 3:
        std.printDetails()
    case 4:
        std.exit()

"""
# make a program using oop concpt by create a class name Student and make a constructor and function base also need to ask input from the user with options like add new student,( update student and delete student ) using roll no, show all students and exit, also make a menu for the user and use while loop to call the function again and again until the user wants to exit need to record file in txt format and also need to save the data in the file and load the data from the file
import os

class Student:
    def __init__(self, name, rollno, age, courses, marks):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.courses = courses
        self.marks = marks

    def __str__(self):
        return f"{self.name}, {self.rollno},{self.age},{self.courses},{self.marks}"
    
    def printDetails(self):
        return f"{self.name}, {self.rollno},{self.age},{self.courses},{self.marks}"
    
def addStudent():
    try:
        with open("student.txt", "a") as f:
            name = input("Enter student name: ")
            rollno = input("Enter student rollno: ")
            age = input("Enter student age: ")
            courses = input("Enter student courses: ")
            marks = input("Enter student marks: ")
            student = Student(name, rollno, age, courses, marks)
            f.write(student.printDetails())
            f.write("\n")
            
    except Exception as e:
        print(e)

def serchStudent():
    pass
def deleteStudent():
    pass
def updateStudent():
    pass
def showAllStudents():
    try:
        with open("student.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No students found.")


def menu():
    while True:
        print("----- Welcome to student management system -----")
        print("1. Add New Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Show All Students")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            addStudent()
        elif choice == 2:
            serchStudent()
        elif choice == 3:
            deleteStudent()
        elif choice == 4:
            updateStudent()
        elif choice == 5:
            showAllStudents()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

    print("----- Thank you for using student management system -----")

if __name__ == "__main__":
    menu()
"""
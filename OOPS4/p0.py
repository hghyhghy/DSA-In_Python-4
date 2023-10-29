

# python program to demonstrate the hybrid inhritance 

# creating a class 

class School:

    def func(self):

        print("This is the first function") 

class Student1(School):

    def func1(self):

        print("This is the second function")


class Student2(School):

    def func2(self):

        print("This is the  third function")

class Student3(Student1,School):

    def func3(self):

        print("This is the fourth function")


# the drivers code 

object=Student3()

object.func1()

object.func3()
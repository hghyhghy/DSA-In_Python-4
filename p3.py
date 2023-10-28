

# a simple inheritance program 

class Person():

    # the constructor

    def __init__(self, name):

        self.name=name

    # to get name 

    def getname(self):

        return self.name
    
    # to check wheather the person is an employee

    def isemployee(self):

        return False
    

# inheriting the class by another class 


class Employee(Person):

    # here we return true 

    def isemployee(self):

        return True
    

# the driver code 

emp=Person("Sub")

print(emp.getname(), emp.isemployee())
        
emp1=Employee("Subham")

print(emp1.getname(), emp1.isemployee())
 

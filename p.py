

# destructors in python 

# creating a class 

class Employee:

    # initializing the constructor 

    def __init__(self):

        print("The constructor is created ")

    # calling the destructor 

    def __del__(self):

        print("The mighty destructor is created")



# creating the object 

obj=Employee()

del obj
        
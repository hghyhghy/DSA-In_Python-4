

# python program to illustrate the destructor

# creating a class

class A:

    #the constructor 

    def __init__(self,bb):

        self.b=bb

#creating another class 
        
class B:
    # calling the constructor

    def __init__(self):

        self.a=A(self)

    # calling the destructor 

    def __del__(self):

        print("Your Computer Will Die ")


def fun():

    b=B()


fun()
        
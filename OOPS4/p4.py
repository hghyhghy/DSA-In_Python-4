

# python program to demonstarte instance of attributes 

# creating a class

class Emp:

    def __init__(self):


        self.name="Subham"

        self.salary=45000

    def show(self):

        print("His name is ", self.name)

        print("His salary is ", self.salary)



# creating one object 

e1=Emp()

print("Elements in dictionary form ", vars(e1))

# the vars function displays the attributes in dict form 

print(dir(e1)) # it shows more attribute than var func


        
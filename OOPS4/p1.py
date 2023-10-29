

# python program to demonstrate protected  member 

# creating a class 

class Base:

    # the constructor

    def __init__(self):

        #the protected member 

        self._a=2  # setting by an underscore



# creating a derived class 

class Derived(Base):

     # the constructor 

     def __init__(self):
         
         # calling the constructor of base class 

         Base.__init__(self)

         print("Calling the protected  member of the base class", self._a)

         # modifying the member 

         self._a=3

         print("Calling the protected  member of the base class", self._a)


# the driver code

# creating the object 

obj1=Derived()

obj2=Base()

print("Accessing the protected member of the base class",obj2._a)

print("Accessing the protected member of the derived class",obj1._a)

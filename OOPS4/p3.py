

# static variables of python 

# creating a class 

class CSSstudent:

    stream="CSE"  # class variable

    def __init__(self,name,roll):

        self.name=name

        self.roll=roll

# objects of the cse students 

a=CSSstudent("Subham",1)

b=CSSstudent("Bipasha",2)

# printing the elements 

print(a.stream)

print(b.stream)

print(a.name)

print(a.roll)

print(b.name)

print(b.roll)

# now changing the stream for element a 

a.stream="AEIE"

#printing the changes stream

print(a.stream)

        
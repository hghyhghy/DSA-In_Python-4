

# multilevel inheritance 

class Grandfather:

    # the constructor

    def __init__(self,grandfather):

        self.grandfather=grandfather

# intermediate class 

class Father(Grandfather):

    # the constructor 

    def __init__(self,fathername, grandfather):

        self.fathername=fathername

        # invoking the constructor of the grandfather

        Grandfather.__init__(self,grandfather)


# derived class 

class Son(Father):

    # the constructor 

    def __init__(self,sonname, fathername, grandfather):

        self.sonname=sonname

        # invoking the constructor of the father

        Father.__init__(self,fathername,grandfather)

    # displaying  the   elements 


    def ofshow(self):

        print("His grandfather name is", self.grandfather) 

        print("His father name is", self.fathername)   

        print("His name is", self.sonname)    


s1=Son("Subham","Goutam Sarkar","Khitibhusan Sarkar")

s1.ofshow()


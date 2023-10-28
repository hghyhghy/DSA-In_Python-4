

# example of multiple inheritance 

class Mother:

    Mothername=""

    def mother(self):

     print(self.Mothername)

# base class 2 

class Father:

    Fathername=""

    def father(self):
       
       print(self.Fathername)


# the child class 

class son(Mother,Father):
   
   def parents(self):
      
      print("Father name is ", self.Fathername)

      print("Mother name is ", self.Mothername)



# the driver code 

# creating the object 

s1=son()

s1.Fathername="Gautam Sarkar"

s1.Mothername="Gouri Sarkar"

s1.parents()
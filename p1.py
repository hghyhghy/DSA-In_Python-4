
# destruction in recursion

# creating a class 


class Recursive:


    def  __init__(self,n):

        self.n=n
        
        print("Recursive function initialized with ",n)

    def run(self,n=None):

        if n is None:

            n=self.n

        if n<=0:

            return

        print("Running recursive function  with ",n)

        self.run(n-1)

obj=Recursive(5)

obj.run()  

        
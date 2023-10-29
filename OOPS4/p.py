

# hierarchical inheritance 

# creating the parent class

class Parent:

    def func(self):

        print("This is the main function")


class Child1(Parent):

    def func1(self):

        print("This is the child 1")


class Child2(Parent):

    def func2(self):

        print("This is the child 2")


# drivers code 

# creating the objects 

obj1=Child1()

obj2=Child2()

obj1.func()

obj1.func1()

obj2.func2()



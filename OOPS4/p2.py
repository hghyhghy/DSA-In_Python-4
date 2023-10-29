

# one simple example of polymorphhism 

# creating a class 

class India():

    def capital(self):

        print("New Delhi is the capital of india")

    def language(self):

        print("Hindi is th most used language here")

    def countrytype(self):

        print("India is a developing country")

# creating another class 

class America():

    def capital(self):

        print("Washigton Dc is the capital of america")

    def language(self):

        print("English is th most used language here")

    def countrytype(self):

        print("America is a developed country")


# the driver code 

i=India()

a=America()

# accessing the element  using for loops

for ele in (i,a):

    ele.capital()

    ele.language()

    ele.countrytype()




class Person():
    
    def __init__(self , fname , lname):
        self.__firstName = fname
        self.__lastName = lname


a = Person("M Hashim" , "Khan")


# private access modifier cannot be accessed directly.
# print(a.__firstName)
# print(a.__lastName)

# accessed indirectly
print(a._Person__firstName)
print(a._Person__lastName)
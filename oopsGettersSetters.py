

class MyClass:

    def __init__(self , name):
        self.stuName = name

    @property
    def studentName(self):
        return f"Student name is {self.stuName}"
    
    @studentName.setter
    def studentName(self , name):
        print(f"{self.stuName} is now {name}")
        self.stuName = name


# /////////////////////// MyClass class end/////////////////////////
# ///////////////////////////////////////////////////////////


class Fruit():

    def __init__(self , fruitName):
        self.fruit = fruitName

    # getter method
    @property
    def fruitName(self):
        return self.fruit
    
    # setter method
    @fruitName.setter
    def fruitName(self ,fruitName):
        print(f"{self.fruit} is now {fruitName}")
        self.fruit = fruitName


# ////////////////////// Fruit class end ////////////////////
# ///////////////////////////////////////////////////////////



class Practice():

    def __init__(self , name):
        self.__name = name


    # getter method
    @property
    def myName(self):
        return self.__name


    #  setter method
    @myName.setter
    def myName(self , newName):
        print(f"{self.__name} is change to {newName}")
        self.__name = newName






# /////////////////////// Practice class end/////////////////
# ///////////////////////////////////////////////////////////



# object for MyClass

obj = MyClass("Hashim")
print(obj.studentName)
obj.studentName = "Hayan"

print('')

# Object for

banana = Fruit("banan")
print(banana.fruitName)
banana.fruitName = "Orange"
print(banana.fruitName)

print('')

# Object for Practice
pract = Practice("M Hashim")
print(pract.myName)
pract.myName = "Hayan"
print(pract.myName)
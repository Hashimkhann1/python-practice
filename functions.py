# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.

# Creating a Function
# In Python a function is defined using the (def) keyword:

def my_function():
    print("Hello from function");

def myName(name):
    print(f"My name is {name}")
    

def listOfFruits(fruits):
    for x in fruits:
        print(x)

fruits = ["apple", "banana", "cherry"]

# /////// Return Values ///////
def myFunction2():
    return 2 * 2;

# pass statement is used to avoid getting an error.

def passFunct():
    pass

# my_function()
# myName("M Hashim")
# listOfFruits(fruits)
# print(myFunction2());
passFunct()
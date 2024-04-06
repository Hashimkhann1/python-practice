

class MyInfo:
    name = "M Hashim"
    age = 21
    gender = "male"
    dateOfBirth = "8/1/2003"

class SmartPhone:
    name = 'phone'
    screen = 'lcd'
    camreas = 0

    def info(self):
        print(f"{self.name} Screes {self.screen} and {self.camreas} Camras") 

class Person:

    def __init__(self , name , occupation , gender):
        self.name = name
        self.occupation = occupation
        self.gender = gender


p1 = Person('M Hashim' , "Flutter Developer" , "Male")
print(p1.name)
print(p1.occupation)
print(p1.gender)

print('')

p2 = Person("Dayan" , "Student" , "male")
print(p2.name)
print(p2.occupation)
p2.occupation = "School sutdent"
print(p2.occupation)
print(p2.gender)

# del is use to delet object or oject properties
# delet object

# del p2
# print(p2.name); # giving me an errro

#  delete object properties  

# del p2.gender
# print(p2.gender)


# iphone = SmartPhone()
# iphone.name = 'iphone'
# iphone.camreas = 3
# iphone.screen = 'lcd'
# print(iphone.name);
# print(iphone.screen)
# print(iphone.camreas)

# iphone.info()

# hashimInfo = MyInfo()
# print(hashimInfo.name)
# print(hashimInfo.age)
# print(hashimInfo.gender)
# print(hashimInfo.dateOfBirth)
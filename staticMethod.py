


class Math():

    def __init__(self , num):
        self.num = num

    def addToNum(self , n):
        self.num = self.num + n

    # in static mathod we not user self parameter
    @staticmethod
    def add(a , b):
        return a + b
    
a = Math(8)

print(a.num)
a.addToNum(5)
print(a.num)
print(a.add(2,2))
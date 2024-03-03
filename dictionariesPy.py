myDist = {
    "name" : "M Hashim",
    "age" : 21,
    "address" : "Peshawar",
    "male" : True
}

print(myDist)
print(myDist["name"])
 
# Dictionary Length
print(len(myDist))
print(myDist.keys())
print(myDist.values())

# Change Values
myDist['age'] = 200
print(myDist)

myDist['color'] = 'blue'
print(myDist)

myDist.pop('color')
print(myDist)

# looping
for i in myDist:
    print(i,":",myDist[i])
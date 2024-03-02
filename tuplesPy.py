mytuple = ("apple", "banana", "cherry")

print(mytuple);
print(mytuple[0])

# update tuuple
upT = list(mytuple)
upT[1] = 'mango'
mytuple = tuple(upT)
print(mytuple)


# add items
addIT = list(mytuple)
addIT.append('mango')
mytuple = tuple(addIT)
print(mytuple)


# remove items
addIT = list(mytuple)
addIT.remove('mango')
mytuple = tuple(addIT)
print(mytuple)
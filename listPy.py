
myList = ["apple" , "banana" , "cherry"]
names = ["M Hashim" , "Sabir" , "Dayan" , "Hayan"]

print(myList)
print(names)
print()

# List Length
print(len(names))
print(len(myList))
print()


# Access Items
print(names[0])
print(names[1])
print()


# Change Item Value
myList[1] = "orange"
print(myList)
print()

# Append Items
# To add an item to the end of the list, use the append() method:
myList.append('banana')
print(myList)


# Insert Items
# To insert a list item at a specified index, use the insert() method.
myList.insert(1 , "graps")
print(myList)
print()

# Remove Specified Item
myList.remove('orange')

# Remove Specified Index
myList.pop(1)
print(myList)

# loop through a list
for i in names:
    print(i)

print()
names.sort()
print(names)

# clear list
myList.clear()
print(len(myList))
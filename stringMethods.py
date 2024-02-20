
name = "M Hashim"

# length of name
print(len(name))

# string array
print(name[0])
print(name[2])

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Looping Through a String
for i in name:
    print(i)

# Check String
if "Has" in name:
    print("Yes Has is present")

# Slicing
print(name[0:])
print(name[0:4])

# Upper Case
print(name.upper())

# Lower Case
print(name.lower())

# Replace
print(a.replace("L" , "D"))
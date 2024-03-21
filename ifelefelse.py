
# if elif else is conditions in python

a = 22;
b = 10

c = 20;
d = 20;

e = 1;
f = 3;

print(a , b)


# //////////////////////////////////////
#/////////// if else example ///////////
# /////////////////////////////////////

# if a > b:
#     print(str(a) + " is greather than " + str(b))
# else:
#     print(str(a) + " is less than " + str(b))

# ///////////////////////////////////////////////
#/////////// if elif and else example ///////////
# ///////////////////////////////////////////////

# if c > d:
#     print(str(c) + " is greather than " + str(d))
# elif(c == d):
#     print(f"{c} is equal to {d}")
# else:
#     print(str(c) + " is less than " + str(d))

# ///////////////////////////////////////////
#//////////// Short Hand If ////////////////
# /////////////////////////////////////////

if a > b: print(f"{a} is greather than {b}")


# ///////////////////////////////////////////
#//////////// Short Hand If else ////////////////
# /////////////////////////////////////////

print(f"{e} is greather than {f}") if e > f else print(f"{e} is less than {f}")


# ///////////////////////////////////////////
#//////////// and opreater ////////////////
# /////////////////////////////////////////

if a > b and c == d:
   print("both condition is true");


# ///////////////////////////////////////////
#//////////// or opreater ////////////////
# /////////////////////////////////////////

if a < b or c == d:
   print("one condition is true"); 


target = 2
nums = [1,3,5,6]

def check():
   if target in nums:
      for x in range(len(nums)):
          if(nums[x] == target):
            print(x)
   else:
      for x in range(len(nums)):
         if(target > nums[x] and target < nums[x]):
            print(x)


check()
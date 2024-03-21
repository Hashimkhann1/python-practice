
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# ////// for loop /////////


fruits = ["apple", "banana", "cherry"]
# for i in fruits:
#     print(i);

# /////// break Statement //////

# for x in fruits:
#     print(x);
#     if x == "banana":
#         break

# /////// continue Statement ////////

for x in fruits:
    if x == "banana":
        continue
    print(x)



# ///// for loop with range //////

# for i in range(10):
#     print(i)

# for i in range(2,10):
#     print(i)



# This is coding problem from gkg
# num = [1,2,3,4,5,6,7]
# k = 6

# if k not in num:
#     print(-1)
# else:
#     for x in range(len(num)):
#         if(num[x] == k):
#             print(x)
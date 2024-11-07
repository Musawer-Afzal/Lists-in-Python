# List is a data type where you can store multiple items under 1 name. 
# More technically, lists act like dynamic arrays which means
# you can add more items on the fly.
# Array VS List
# Pros:
# Fixed VS Dynamic Size
# Convience -> Hetrogenous Size(Can store multiple data types)
# Cons:
# Slow speed of Execution
#  More Memory required

# E.g: L = [19, "Hello", 3.14, [1, 2, 3]]

# ID or the memory address of a value can be found using
# Both will give the same address since a is pointing to 2
a = 2
print(id(2))
print(id(a))

# Now using List
L = [1,2,3]
print("ID of L: ", id(L))
# The address of L[0], L[1] and L[2] is same as the address of 1, 2, 3
# Why?? Because the array is storing the address of 1, 2, 3 and not the actual value
# as the actual value is stored in the memory somewhere else
print("ID of L[0]: ", id(L[0])) # 140717315852728
print("ID of L[1]: ", id(L[1])) # 140717315852760
print("ID of L[2]: ", id(L[2])) # 140717315852792
print(id(1))
print(id(2))
print(id(3))


# Characteristics of List
# 1. Ordered
L = [1,2,3]
L1 = [3,2,1]
L == L1 # False, the Values are same but the order is different

# 2. Mutable
L = [1,2,3]
L[0] = 5
print(L) # [5, 2, 3]

# 3. Hetrogenous
L = [1, "Hello", 3.14]
L[0] = 5
print(L) # [5, "Hello", 3.14]

# Can have duplicates
L = [1, 2, 3, 3, 3]
print(L) # [1, 2, 3, 3, 3] 

# Dynamic
L = [1,2,3]
L.append(4)
print(L) # [1, 2, 3, 4]

# Nested
L = [1,2,3, [4,5,6]]
print(L[3]) # [4, 5, 6]

# Items can be extracted
L = [1,2,3, [4,5,6]]
print(L[3][1]) # 5
print(L[1:4]) # [2, 3, [4, 5, 6]]

# Can contain any kind of objects in Python 



# Creating a List
# 1. Empty List
L = []
print(L) # []

# 2. 1D List
L = [1,2,3]
print(L) # [1, 2, 3]

# 3. 2D List
L = [[1,2,3], [4,5,6]]
print(L) # [[1, 2, 3], [4, 5, 6]]

# 4. 3D List
L = [[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]]
print(L) # [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

# 5. Heterogeneous List
L = [1, "Hello", 3.14]
print(L) # [1, "Hello", 3.14]

# Using Type Conversion
L = list("Hello")
print(L) # ['H', 'e', 'l', 'l', 'o']
print(list("Hello")) # ['H', 'e', 'l', 'l', 'o']



# Accessing Items from a List
L = [1,2,3,4,5]
print(L[0]) # 1, also called Positive Indexing
print(L[-1]) # 5, also called Negative Indexing

# Accessing an item in 2D List
L = [[1,2,3],[4,5]]
print(L[0][0]) # 1, We went to 0 index of 3rd index which was 4

# Accessing an item in 3D List
L = [[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]]
print(L[0]) # [[1, 2, 3], [4, 5, 6]]
print(L[0][1]) # [4, 5, 6]
print(L[0][1][1]) # 5



# Slicing
L = [1,2,3,4,5]
print(L[2:4]) # [3, 4]
print(L[::2]) # [1, 3, 5]
print(L[::-1]) # [5, 4, 3, 2, 1]




# Adding items to a List
# Append, it adds a single whole item
L = [1,2,3]
L.append(4)
L.append([5,6,7])
L.append("Country")
print(L) # [1, 2, 3, 4, [5, 6, 7], 'Country']

# Extend, it will try to add multiple items at the end of List
L = [1,2,3]
L.extend([4,5,6])
L.extend("Country")
print(L) # [1, 2, 3, 4, 5, 6, 'C', 'o', 'u', 'n', 't', 'r', 'y']

# Insert, to add an item in a desired locationn
L = [1,2,3]
L.insert(0, 4)
L.insert(3, "Country")
print(L) # [4, 1, 2,'Country', 3]
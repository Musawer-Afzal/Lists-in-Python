# List is a data type where you can store multiple items under 1 name. 
# More technically, lists act like dynamic arrays which means
# you can add more items on the fly.
# Array VS List
# Pros:
# Fixed VS Dynamic Size
# Convience -> Hetrogenous Size(Can store multiple data types)
# Cons:
# Slow speed of Execution
# More Memory required
# Risky usage

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
# You can even store internal function in a List
L = [1,2,print,type,input]
print(L) # [1, 2, <function print at 0x7f0c8c2e9c10>, <class 'function'>, <function input at 0x7f0c8c2e9c10>]


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


# Edit Items in a List
L = [1,2,3,4,5]
# Editing with Indexing
L[-1] = 500
print(L) # [1, 2, 3, 4, 500]
L = [1,2,3,4,5]
# Editing with Slicing
L[0:3] = [100, 200, 300]
print(L) # [100, 200, 300, 4, 5]


# Delete Items from a List
# 1. del
L = [1,2,3,4,5]
print(L)
del L[2]
print(L) # [1, 2, 4, 5]
del L[0:2]
print(L) # [5]
del L
#print(L) # Will throw an error since L is deleted

# 2. Remove, Remove a single item according to the value not the index
L = [1,2,3,4,5]
L.remove(3)
print(L) # [1, 2, 4, 5]
L.remove(5)
print(L) # [1, 2, 4]

# 3. Pop, Remove an item at a particular index
L = [1,2,3,4,5]
# if index is not provided then it will remove the last item
L.pop()
print(L) # [1, 2, 3, 4]
L.pop(1)
print(L) # [1, 3, 4]

# 4. clear, It makes an empty list deleting all the items
L = [1,2,3,4,5]
L.clear()
print(L) # []




# OPERATORS ON LISTS
# Arithmetic, Membership, Loop

# Arithmetic
L1 = [1,2,3,4]
L2 = [5,6,7,8]
# Concatenation
print(L1 + L2) # [1, 2, 3, 4, 5, 6, 7, 8]
print(L1 * 3) # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

# Membership
L = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]
print(1 in L) # True
print(10 in L) # False
print(10 not in L) # True
print(5 in L2) # False

# Loop
L = [1,2,3,4,5]
for i in L:
    print(i) # 1 2 3 4 5
L = [[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]]
for i in L:
    print(i) # [[1,2,3], [4,5,6]] [[7,8,9], [10,11,12]]




# FUNCTIONS  IN LISTS
# len, min, max, sum, sorted, count , index, reverse, sort(vs sorted), copy
L = [1,2,3,4,5]
print(len(L)) # 5
print(min(L)) # 1
print(max(L)) # 5
print(sum(L)) # 15
print(sorted(L)) # [1, 2, 3, 4, 5]
print(sorted(L, reverse = True)) # [5,4,3,2,1]

# Count, Will tell the frequency of an item
L = [1,2,3,4,5,1,4,7,8,6,4]
print(L.count(2)) # 1
print(L.count(4)) # 3

# Index, Tells the index position of an item
L = [1,2,3,4,5,1,4,5,7,5,8,4]
print(L.index(4)) # 3

# Reverse, it permanently reverses the list unlike using sorted
L = [1,2,3,4,5]
L.reverse()
print(L) # [5, 4, 3, 2, 1]

# Sort, it sorts the list permanently
L = [3,5,6,4,2,1,7]
print(sorted(L)) # [1, 2, 3, 4, 5, 6, 7]
print(sorted(L, reverse = True)) # [7, 6, 5, 4, 3, 2, 1]
print(L) # [3, 5, 6, 4, 2, 1, 7]
L.sort()
print(L) # [1,2,3,4,5,6,7]

# Copy, it creats a "Shallow copy" of the list in the memory
L = [1,2,3,4,5]
print(L)
print(id(L))
L1 = L.copy()
print(L)
print(id(L1))





# List Conprehension
# It provides a concise way to create lists
# General formula
# newlist = [expression for item in iterable if condition == True]
# Advantages
# 1. More time-efficient and space-efficient then loops
# 2. Require fewer lines of code
# 3. Transforms iterative statements into a formula

# Example 1
# Add 1 to 10 numbers to a list
L = []
for i in range(1,11):
    L.append(i)
print(L) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# the aboove written code can be written like this effeciently
L = [i for i in range(1,11)]
print(L)

# Scaler Multiplication on a vactor
v = [2,3,4]
s = -3
# Answer we want: [-6, -9,-12]
# Using Loops
x = []
for i in v:
    x.append(s * i)
print(x)
# Using List Comprehension
x = [s * i for i in v]
print(x)

# Example 2
# Add squares
L = [1,2,3,4,5]
# Expected answer: [1,4,9,16,25]
L1 = [i**2 for i in L]
print(L1)

# Example 3
# Print all numbers divisible by 5 in the range of 1 to 50
i = 0
L = [i for i in range(1, 51) if i%5 == 0]
print(L)

# Example 4
# Find languages which start with letter 'p'
languages = ['java', 'python', 'php', 'c', 'javascript']
p = [i for i in languages if i.startswith('p')]
print(p)

# Example 5, Using Nested If
basket = ['apple', 'guava', 'cherry', 'banana', 'annar']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana', 'annar']
# add the fruits present in my_fruits to a new list that start with "a" and are also present in basket
new_list = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith("a")]
print(new_list)

# Example 6, Print a (3*3) Matrix using list comprehension --> Nested List Comprehesion
M = [[i * j for j in range(1,4)]for i in range(1,4)]
print(M)

# Example 7, Cartesian Product --> List Comprehension on 2 lists together
L1 = [1,2,3,4]
L2 = [5,6,7,8]
L3 = [i * j for i in L1 for j in L2]
print(L3)




# 2 Ways to Traverse a List
# 1. Itemwise
L = [1,2,3,4]
for i in L:
    print(i)
# 2. Indexwise
L = [1,2,3,4]
for i in range(0, len(L)):
    print(i) # 0,1,2,3. These are index position of the items not the values
    print(L[i]) # 1,2,3,4. This will print the values of the items


# Zip function
# If you want to make a new list from already existing lists such that the 1st item of 
# the new list is the combination of the 1st items of the other 2 lists and 2nd item
# of the new list is the combination of the 2nd items of the other 2 lists and so on.
# The final item would ba a Tuple
L1 = [1,2,3,4]
L2 = [-1,-2,-3,-4]
L3 = zip(L1,L2)
print(list(L3))
# Now to add the items of the new list
# First the zip value is found, then the first value is assigned to "i" and 
# the 2nd to "j" and then the 2 values are added
L3 = [i+j for i,j in zip(L1,L2)]
print(L3)
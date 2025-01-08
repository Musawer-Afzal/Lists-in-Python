# Problem 3: Update number of items available
# Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

# i.e -
# candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
# no_of_items = [10,20,34,74,32]
# Write a program to show no. of items of each candy type.

# Output:
# Jelly Belly-10
# Kit Kat-20
# Double Bubble-34
# Milky Way-74
# Three Musketeers-32


candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]

for i in range(len(candy_list)):
    print(candy_list[i],"-", no_of_items[i])


# OR, use zip function

candy_list = ['Jelly Belly', 'Kit Kat', 'Double Bubble', 'Milky Way', 'Three Musketeers']
no_of_items = [10, 20, 34, 74, 32]

for candy, count in zip(candy_list, no_of_items):
    print(f"{candy}-{count}")
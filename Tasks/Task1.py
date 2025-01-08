# Problem 1: Combine two lists index-wise(columns wise)
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given List:
# list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an"]

# Output:
# [['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]


list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
list3 = []

for i in range(len(list1)):
    list3.append([list1[i], list2[i]])

print(list3)
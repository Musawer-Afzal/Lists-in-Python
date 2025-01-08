# Write a program that can find the max number of each row of a matrix
# Example:
# Input:
# [[1,2,3],[4,5,6],[7,8,9]]
# Output:
# [3,6,9]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
max_list = []

for elements in matrix:
    max_list.append(max(elements))

print(max_list)
# Write a list comprehension to print the following matrix
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
comp_matrix = [[i for i in range(3)] for j in range(3)]
print(comp_matrix)
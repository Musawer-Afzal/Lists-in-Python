# Write a list comprehension that can flatten a nested list
# Input
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]
# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]



matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

flatten_matrix = [row[i] for row in matrix for i in range(3)]
print(flatten_matrix)
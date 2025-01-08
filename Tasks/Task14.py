# Write a list comprehension that can transpose a given matrix
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]


matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

transposed_matrix =[[row[i] for row in matrix] for i in range(3)]
print(transposed_matrix)
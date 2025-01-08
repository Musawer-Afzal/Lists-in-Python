# Problem 6: Find list of common unique items from two list. and show in increasing order
# Input
# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]
# Output:
# [34, 67, 89]


num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]

result = []

for i in range(len(num1)):
    if num1[i] in num2 and num1[i] not in result:
        print(num1[i]) # To check the order of the list
        result.append(num1[i])

result.sort()
print(result)
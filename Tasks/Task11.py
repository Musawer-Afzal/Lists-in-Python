#  Write a program that can perform union operation on 2 lists
# Example:
# Input:
# [1,2,3,4,5,1]
# [2,3,5,7,8]
# Output:
# [1,2,3,4,5,7,8]


list1 =  [1,2,3,4,5,1]
list2 = [2,3,5,7,8]
union = []

for i in range(len(list1)):
    if list1[i] not in union:
        union.append(list1[i])

for i in range(len(list2)):
    if list2[i] not in union:
        union.append(list2[i])

# sort_union = union.sort()
print(sorted(union))
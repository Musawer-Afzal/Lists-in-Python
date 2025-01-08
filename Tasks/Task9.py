# Problem 9: Convert Character Matrix to single String using string comprehension.
# Example 1:
# Input:
# [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
# Output:
# campux is best channel


strings = [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
s = " ".join(["".join(i) for i in strings])
print(s)
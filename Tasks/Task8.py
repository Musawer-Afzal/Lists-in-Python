# Problem 8: Split String of list on K character.
# Example :
# Input:
# ['CampusX is a channel', 'for data-science', 'aspirants.']
# Output:
# ['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']


strings = ['CampusX is a channel', 'for data-science', 'aspirants.']
s = " ".join(strings)
print(s.split(" "))
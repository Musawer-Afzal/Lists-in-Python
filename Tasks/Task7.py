# Problem 7: Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
# Input:
# ['1ac21', '23fg', '456', '098d','1','kls']
# Output:
# ['456', '23fg', '1ac21', '1', 'kls', '098d']


strings = ['1ac21', '23fg', '456', '098d', '1', 'kls']

def calculate_product(s):
    """Calculate the product of numeric characters in the string."""
    product = 1
    found_numeric = False
    for char in s:
        if char.isdigit():
            product *= int(char)
            found_numeric = True
    return product if found_numeric else 1

# Sort the list based on the product value of numeric characters
sorted_strings = sorted(strings, key=calculate_product, reverse=True)

# Output the sorted list
print("Sorted list:", sorted_strings)
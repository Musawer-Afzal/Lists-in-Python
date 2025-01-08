# Problem 10: Add Space between Potential Words.
# Example:
# Input:
# ['campusxIs', 'bestFor', 'dataScientist']
# Output:
# ['campusx Is', 'best For', 'data Scientist']



strings = ['campusxIs', 'bestFor', 'dataScientist']
result = []

for i in strings:
    new_word = ''
    for word in range(len(i)):
        if i[word].isupper() and word > 0:
           new_word += " "
        new_word += i[word]
    
    result.append(new_word.title())

print(result)
import numpy as np

# Write a python function to swap two numbers. Identify variable assignment in your code.
day1 = 5
day2 = 564
print(day1,day2)
# write a python function to swap age with lowest age first
day1, day2 = day2, day1
print(day1, day2)


text = [ [1,2,3],[4,5,6],[7,8,9] ]
# convert to 3D list in-place
for i, data in enumerate(text):
    text[i] = [[data[0], data[1], data[2]]]

# utility for print a 3x3 matrix
def formatrix(label, matrix):
    indent = len(label)
    return '\n'.join((label + ', '.join(map(str, matrix[0])),
                      indent*' ' + ', '.join(map(str, matrix[1])),
                      indent*' ' + ', '.join(map(str, matrix[2]))))

# print each matrix in reformatted list
for i, matrix in enumerate(text):
    print(formatrix('text[%s]: ' % i, matrix))
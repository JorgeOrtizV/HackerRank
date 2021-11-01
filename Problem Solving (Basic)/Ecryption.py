# The goal of this program is to encrypt an english text. This encryption follows the
# next steps:
# Input:
# A line of text with spaces.
# Process
# Remove spaces to calculate length of the text L. Obtain sqrt(L), the floor of sqrt(L)
# will be the rows and ceil of sqrt(L) will be the column.
# Arrange the characters in rows and columns.
# Output:
# Output each column of the arrangement followed by an space.

import math


def Encryption(string, row, column):
    matrix = []
    encrypted = ""
    row_count = 0
    while len(string) > 0:
        if len(string) >= column:
            matrix.append(string[:column])
            string = string.replace(string[:column],"")
        else:
            matrix.append(string)
            string = string.replace(string[:len(string)], "")
        row_count += 1
    for i in range(column):
        for j in matrix:
            if len(j) > i:
                encrypted += j[i]
        encrypted += " "
    print(encrypted)

string = input()
string = string.replace(" ","")
L = len(string)
sqL = math.sqrt(L)
row = math.floor(sqL)
column = math.ceil(sqL)
Encryption(string, row, column)
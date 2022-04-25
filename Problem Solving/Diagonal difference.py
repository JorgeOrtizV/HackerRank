# This program receives as input a number n, which defines the size of a square matrix.
# Then it receives the elements per row in the matrix, size n x n.
# The goal is to calculate the absolute difference between: | (topleft to bottonright diagonal) - (topright to botton left diagonal)

def diagonal_difference(first_diag, sec_diag):
    first_diag_sum = sum(first_diag)
    sec_diag_sum = sum(sec_diag)
    result = abs(first_diag_sum-sec_diag_sum)
    return result

size = int(input())
first_diag = []
sec_diag = []
first_diag_index = 0
sec_diag_index = (size-1)

for i in range(size):
    row = input()
    row_list = row.split(" ")
    first_diag.append(int(row_list[first_diag_index]))
    sec_diag.append(int(row_list[sec_diag_index]))
    first_diag_index += 1
    sec_diag_index -= 1

difference = diagonal_difference(first_diag, sec_diag)
print(difference)
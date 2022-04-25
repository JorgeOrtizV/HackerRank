# A Magic Square is a n x n matrix, in which the sum of the digits in its rows, columns or diagonals are the same.
# In this problem we receive a 3 x 3 square in the following way:
# 4 9 2
# 3 5 7
# 8 1 5
# The goal is to compute the changes we must do to this square in order to make it a magic square. But this conversion
# should be done in minimal cost. Where the cost of one movement s is |previous number - new number|.

# This square just have numbers from 1 to 9, so we can get the sum of all digits:
# 1 + 2 + 3 + ... + 9 = 45. Therefore we can obtain the sum of each row/column, which is 45/3 = 15.
# We can also compute the value of the center, which is always 5 in a 3 x 3 square.
# In addition, if we know the center is 5, to sum 15 we can use just 4 pairs of numbers:
# 1 and 9, 2 and 8, 3 and 7, 4 and 6.
# Doing some math we know that we can use just 2 and 8, 4 and 6 for the corners.

def MagicSquare(row1, row2, row3):
    cost = 0
    available_corners = [2, 8, 4, 6]
    min_costs = []
    # Check the senter:
    if row2[1] != 5:
        cost += abs(row2[1] - 5)
        row2[1] = 5
    # Check the corners
    first_diagonal = [row1[0], row2[1], row3[2]]
    second_diagonal = [row3[0], row2[1], row1[2]]
    # First diagonal
    if sum(first_diagonal) != 15:
        if first_diagonal[0] in available_corners:
            cost += abs(first_diagonal[2] - (10-first_diagonal[0]))
            first_diagonal[2] = (10-first_diagonal[0])
            available_corners.remove(first_diagonal[0])
            available_corners.remove(first_diagonal[2])
            row3[2] = first_diagonal[2]

        elif first_diagonal[2] in available_corners:
            cost += abs(first_diagonal[0] - (10 - first_diagonal[2]))
            first_diagonal[0] = (10-first_diagonal[2])
            available_corners.remove(first_diagonal[0])
            available_corners.remove(first_diagonal[2])
            row1[0] = first_diagonal[0]
        else:
            for i in range(len(available_corners)):
                # First we check that number isn't in use in another corner:
                if (available_corners[i] != second_diagonal[0]) and (available_corners[i] != second_diagonal[2]):
                    min_costs.append(abs(first_diagonal[0]-available_corners[i]))
                else:
                    min_costs.append(1000000000)
            index = min_costs.index(min(min_costs))
            cost += abs(first_diagonal[0] - available_corners[index])
            first_diagonal[0] = available_corners[index]
            cost += abs(first_diagonal[2] - (10-first_diagonal[0]))
            first_diagonal[2] = (10-first_diagonal[0])
            available_corners.remove(first_diagonal[0])
            available_corners.remove(first_diagonal[2])
            row3[2] = first_diagonal[2]
            row1[0] = first_diagonal[0]
            min_costs = []
    else:
        available_corners.remove(first_diagonal[0])
        available_corners.remove(first_diagonal[2])

    # Second diagonal
    if sum(second_diagonal) != 15:
        if second_diagonal[0] in available_corners:
            cost += abs(second_diagonal[2] - (10 - second_diagonal[0]))
            second_diagonal[2] = (10 - second_diagonal[0])
            row1[2] = second_diagonal[2]
        elif second_diagonal[2] in available_corners:
            cost += abs(second_diagonal[0] - (10 - second_diagonal[2]))
            second_diagonal[0] = (10 - second_diagonal[2])
            row3[0] = second_diagonal[0]
        else:
            for i in range(len(available_corners)):
                min_costs.append(abs(second_diagonal[0] - available_corners[i]))
            index = min_costs.index(min(min_costs))
            cost += abs(second_diagonal[0] - available_corners[index])
            second_diagonal[0] = available_corners[index]
            cost += abs(second_diagonal[2] - (10 - second_diagonal[0]))
            second_diagonal[2] = (10 - second_diagonal[0])
            row3[0] = second_diagonal[0]
            row1[2] = second_diagonal[2]
    # check first row and last row
    if sum(row1) != 15:
        cost += abs(row1[1] - (15-(row1[0]+row1[2])))
        row1[1] = 15-(row1[0]+row1[2])
    if sum(row3) != 15:
        cost += abs(row3[1] - (15-(row3[0]+row3[2])))
        row3[1] = 15-(row3[0]+row3[2])
    # Check column 1 and column 3
    if (row1[0] + row2[0] + row3[0]) != 15:
        cost += abs(row2[0] - (15 - (row1[0] + row3[0])))
        row2[0] = 15 - (row1[0] + row3[0])
    if (row1[2] + row2[2] + row3[2]) != 15:
        cost += abs(row2[2] - (15 - (row1[2] + row3[2])))
        row2[2] = 15 - (row1[2] + row3[2])

    return cost


# Although the first function runs the code and build a magic square with the less changes as possible, the best code to
# compute the less cost is by comparing all costs of the 8 possible magic squares that exists. In this way we can
# choose the minimum cost as possible.

def Magic_Square_by_comparations(input_square):
    all_combinations = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    costs = []
    for square in all_combinations:
        actual_cost = 0
        for square_row, input_row in zip(square, input_square):
            for i, j in zip(square_row, input_row):
                if not i == j:
                    actual_cost += max([i, j]) - min([i, j])
        costs.append(actual_cost)
    return min(costs)



row1 = input().split(" ")
row1 = list(map(int, row1))
row2 = input().split(" ")
row2 = list(map(int, row2))
row3 = input().split(" ")
row3 = list(map(int, row3))
#result = MagicSquare(row1, row2, row3)
input_square = [row1, row2, row3]
result = Magic_Square_by_comparations(input_square)
print(result)

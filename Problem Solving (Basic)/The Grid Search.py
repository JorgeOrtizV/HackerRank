# This program identifies a string pattern in a bigger text.
# Inputs:
# First line -> int t, which is the number of test cases
# Do t times:
# Receive two integers R C, where R is the number of rows and C the number of columns
# R lines of length C -> which is the grid
# two integers r c, which is the columns and rows of the pattern.
# r lines of length c -> which is the pattern.


def PatternSearcher(grid, pattern, R, C, r, c):
    for i in grid:
        if pattern[0] in i:
            start_index = i.find(pattern[0])
            subgrid = i
            for j in range(1,r):




t = int(input())
for j in range(t):
    grid_constraints = input().split(" ")
    grid_constraints = list(map(int, grid_constraints))
    R = grid_constraints[0]
    C = grid_constraints[1]
    grid = []
    pattern = []
    for i in range(R):
        grid[i] = input()
    pattern_constraints = input().split(" ")
    pattern_constraints = list(map(int,pattern_constraints))
    r = pattern_constraints[0]
    c = pattern_constraints[1]
    for i in range(r):
        pattern[i] = input()
    PatternSearcher(grid, pattern, R, C, r, c)


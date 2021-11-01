# This program receives an input n, it output a right-alligned stair composed by # symbol with n levels.
# The last level has not white spaces.

def stair(n):
    blank_space = ' '
    stair_symbol = '#'
    for i in range(n):
        level = (blank_space*(n-1)) + (stair_symbol*(i+1))
        n -= 1
        print(level)

n = int(input())
stair(n)
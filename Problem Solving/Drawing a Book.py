# This program computes the minium amount of turns a student has to do to arrive an specific page.
# The book is organized the following way:
# null, 1, 2, 3,..., pre-last page, last page.
# The first line is an integer n, which is the number of pages.
# The second line is p, which is the goal page.

def turns_calculator(n, p):
    turns = min(p//2, (n//2) - (p//2))
    print(turns)


n = int(input())
p = int(input())
turns_calculator(n, p)
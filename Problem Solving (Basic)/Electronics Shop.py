# This program computes the bigger amount of money a client can spend. The inputs are:
# The first line -> b n m -> b is an integer, which indicates the budget the client has. m is an integer, which
# indicates the size of an array of prizes of product 1. n is an integer, which indicates the size of an array of
# prizes of product 2.

def maxium_combination(product1, product2, budget):
    max_prize = -1
    for i in product1:
        for j in product2:
            if (i+j) > budget:
                break
            if (i+j) > max_prize:
                max_prize = i+j
    print(max_prize)

constraints = input().split(" ")
constraints = list(map(int, constraints))
product1 = input().split(" ")
product1 = list(map(int, product1))
product2 = input().split(" ")
product2 = list(map(int, product2))
# We order product one in decreasing order, and product two in increasing order, in order to arrive the solution faster
# as possible.
product1.sort(reverse=True)
product2.sort()
maxium_combination(product1, product2, constraints[0])

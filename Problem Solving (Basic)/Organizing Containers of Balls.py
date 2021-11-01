# In this problem we have x containers, which contain x different types of
# balls. The goal is to determine if it is possible to put all the balls of
# the same type in the same container so that all the containers have just a
# type of ball.
# Inputs
# First line -> Integer q, which means number of queries.
# Second line -> Integer n, which means the number of containers and types of balls
# n lines -> Which means the arrangement of the matrix

# 1
# 3
# 0 2 1
# 1 1 1
# 2 0 0
#
# 1 1 1
# 0 2 1
# 2 0 0
#
# 3 0 0
# 0 2 1
# 0 1 1
#
# 3 0 0
# 0 3 0
# 0 0 2

# Output -> Possible

def Organizer(containers_size, type_balls):
    containers_size.sort()
    type_balls.sort()
    # As the type of balls size and containers size are equal, in order to achieve the result, we should have a container
    # of size x, to keep x balls of a type. So if we sort both arrays, and both are equal, then we can solve the problem
    # but if they are not equal it will be impossible.
    if containers_size == type_balls:
        print("Possible")
    else:
        print("Impossible")


q = int(input())
for i in range(q):
    n = int(input())
    type_balls = [0] * n      # Since n is equal to the type of balls, we create an empty list size n in order to keep the counting
                              # of how many balls are of each type
    containers_size = [0] * n # Since n is equal to the number of containers, we create an empty list size n in order to keep the counting
                              # of how many balls can each container handle
    for j in range(n):
        row = input().split(" ")
        row = list(map(int, row)) # Just read the line input
        size = sum(row) # As each line includes the information in each container, we can know its capacity by summing
                        # the amount of balls in it
        containers_size[j] = size
        for k in range(n):
            type_balls[k] += row[k] # Check how many balls of each type in each container
    Organizer(containers_size, type_balls)


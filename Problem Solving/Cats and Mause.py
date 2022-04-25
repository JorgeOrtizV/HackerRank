# This program computes which cat reaches first a mouse, the positions of the 3 animals are known.
# The inputs:
# First line -> Integer n, which means the number of queries
# n lines -> x y z -> x is the Cat A position, y is the Cat B position and z is the mouse position
# The output:
# n lines, in which the output is "Cat A" if the cat A arrives first. "Cat B" if cat b arrives first. "Mouse C" if both
# cats arrive the same time.

def Cat_and_Mouse(CatA, CatB, Mouse):
    distanceA = abs(CatA-Mouse)
    distanceB = abs(CatB-Mouse)
    if distanceA < distanceB:
        print("Cat A")
    elif distanceB < distanceA:
        print("Cat B")
    else:
        print("Mouse C")

n = int(input())
for i in range(n):
    positions = input().split()
    positions = list(map(int, positions))
    Cat_and_Mouse(positions[0], positions[1], positions[2])
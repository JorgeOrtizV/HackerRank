#########  Problem statement  ############################

# We need to calculate the surface area of an irregular figure. Which is placed in a HxW table.
# Each piece consists on a 1x1x1 square block.
# The inputs are:
#       First line: H W     Two integers containing the size of the table.
#       Next lines: H lines containing W elements, each elements represent the number of blocks in each space.

# https://www.hackerrank.com/challenges/3d-surface-area/problem

def surfaceArea(A, H, W):
    surface_area = 0
    for i in range(H):
        for j in range(W):
            if (i,j) == (0,0):
                surface_area += (6*A[i][j])-(2*(A[i][j]-1))
            elif i == 0 and j > 0:
                surface_area += (6*A[i][j])-(2*(A[i][j]-1))-(2*min(A[i][j-1], A[i][j]))
            elif i > 0 and j == 0:
                surface_area += (6*A[i][j])-(2*(A[i][j]-1))-(2*min(A[i-1][j], A[i][j]))
            else:
                surface_area += (6*A[i][j])-(2*(A[i][j]-1))-(2*min(A[i][j-1], A[i][j]))-(2*min(A[i-1][j], A[i][j]))
    print(surface_area)

if __name__ == '__main__':

    size = input().split()
    H = int(size[0])
    W = int(size[1])

    A = []
    for i in range(H):
        content = input().split()
        content = list(map(int, content))
        A.append(content)

    print(A)

    surfaceArea(A, H, W)

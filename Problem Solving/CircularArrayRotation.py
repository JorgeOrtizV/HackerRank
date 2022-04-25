from collections import deque

if __name__ == "__main__":
    elements, rotations, queries = list(map(int, input().split(' ')))
    array = deque(map(int, input().split(' ')))
    array.rotate(rotations)
    for i in range(queries):
        q = int(input())
        print(array[q])

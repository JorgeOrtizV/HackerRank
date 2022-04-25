# Given an array of integers determine the minimum number of elements
# to delete to leave only elements of equal value.

from statistics import mode

def reduce(size, array):
    most_repeated_element = mode(array)
    appearances = array.count(most_repeated_element)
    return size - appearances


if __name__ == "__main__":
    elements = int(input())
    array = input().split()
    array = list(map(int, array))
    result = reduce(elements, array)
    print(result)
    
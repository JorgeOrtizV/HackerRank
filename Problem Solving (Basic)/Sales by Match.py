# This program is a pair finder. It receives an input n, which means the size of an incoming array. In the next
# line the program receives n integers from 0 to 100.
# The program should compute how many pairs of these numbers exist in the array and output that number.

def pair_finder(numbers):
    num_pairs = 0
    while(len(numbers) > 1):
        if(numbers[0] == numbers[1]):
            num_pairs += 1
            numbers.pop(0)
            numbers.pop(0)
        else:
            numbers.pop(0)
    print(num_pairs)

n = int(input())
numbers = input().split(" ")
numbers = list(map(int, numbers))
numbers.sort()
pair_finder(numbers)

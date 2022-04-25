# Given an array of integers what is the length of the longest subarray containing
# no more than two diferent values, such that the values differ by no more than one
# The program receives n, which means the length of the array and many numbers in the following form:
# 5
# 2
# 9
# ...
# This are the members of the array.
# The output is the length of the maxium subarray. The maxium subarray length is 35.
# Constraints 1<n<10^5, 1<array[i]<10^9.

def subarray(numbers):
    max_length = 0
    second = 0
    count = 1
    prev = numbers[0]
    for i in numbers[1:]:
        if i == prev:
            count += 1
        elif (i == (prev+1)) and (second == 0):
            count += 1
            second = 1
        else:
            count = 1
            second = 0
        if count > max_length:
            max_length = count
        prev = i
    print(max_length)


n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
numbers.sort()
subarray(numbers)
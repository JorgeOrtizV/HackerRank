# This program receives an integer n, which is the length of an array. Then it receives integers m and k.
# m means the size of a sub array, k means the sum of the subarray.
# The goal is to compute how many different sub arrays can be formed, of size m, which all his elements sum up k

def sub_arrays(numbers, m, k):
    lower_limit = 0
    upper_limit = m
    count = 0
    while(upper_limit <= len(numbers)):
        sub_array = numbers[lower_limit:upper_limit]
        if (sum(sub_array) == k):
            count += 1
        lower_limit += 1
        upper_limit += 1
    if(len(numbers) == 1) and (m == 1):
        if numbers[0] == k:
            count = 1
    print(count)


n = int(input())
numbers = input().split(" ")
numbers = list(map(int, numbers))
constraints = input().split(" ")
constraints = list(map(int, constraints))
sub_arrays(numbers, constraints[1], constraints[0])
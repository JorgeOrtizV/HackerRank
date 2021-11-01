# Given two sets, calculate numbers between this sets that are multiples of the numbers in array number 1 and
# also factor of the numbers in the second array.
# First line contains two integers, which are the size of array1 and array2 respectively
# The following inputs are the arrays.


def numbers(array1, array2):
    breaked = 0
    count = 0
    nums = []
    for i in range(array1[-1], array2[0]+1):
        for j in array1:
            if (i % j) != 0:
                breaked = 1
                break
        if breaked == 0:
            nums.append(i)
        breaked = 0
    for k in nums:
        for m in array2:
            if(m % k) != 0:
                breaked = 1
                break
        if breaked == 0:
            count += 1
        breaked = 0
    print(count)


constraints = input().split(" ")
constraints = list(map(int, constraints))
array1 = input().split(" ")
array1 = list(map(int, array1))
array2 = input().split(" ")
array2 = list(map(int, array2))
numbers(array1, array2)

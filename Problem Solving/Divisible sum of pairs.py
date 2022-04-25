# This program receives a pair of integers m and n. M means the length of the array, n is the divisible number.
# Then it receives an array of positive integer numbers.
# The goal is to calculate how many pair of numbers are divisible by n.

def pairs(numbers, divisor, size):
    # # naive approach -> iterate through all pairs and see which ones are divisible
    # i = 0
    # counter = 0
    # while(i < (len(numbers))):
    #     for j in range(i+1, len(numbers)):
    #         if ((numbers[i] + numbers[j]) % divisor) == 0:
    #             counter += 1
    #     i += 1
    # print(counter)

    # However naive approach complexity is O(n^2), implementing an efficient algorithm would have a complexity of O(n)
    # Efficient algorithm -> Hashing

    freq = [0] * divisor # Array of the frequency in which modulus repeats in the array
    # Count occurrences of all remainders
    for i in range(size):
        freq[numbers[i] % divisor] += 1

    sum = freq[0] * ((freq[0] - 1) / 2)
    # count for all i and (k-i)
    # freq pairs
    i = 1
    while (i <= divisor// 2 and i != (divisor - i)):
        sum += freq[i] * freq[divisor - i]
        i += 1

    # If K is even
    if (divisor % 2 == 0):
        sum += (freq[divisor // 2] * (freq[divisor // 2] - 1) / 2)

    print(int(sum))


constraints = input().split(" ")
constraints = list(map(int, constraints))
numbers = input().split(" ")
numbers = list(map(int, numbers))
pairs(numbers, constraints[1], constraints[0])
# This program receives an array of 5 integer numbers, the output of the program is the maxium and minimum sum that can be obtained
# by summing exactly 4 numbers.

def min_max(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    result = []
    min_sum = (sum(numbers) - max_num)
    max_sum = (sum(numbers) - min_num)
    result.append(min_sum)
    result.append(max_sum)
    return result

numbers = input()
list_nums = numbers.split(" ")
list_nums = list(map(int,list_nums))
result = min_max(list_nums)
print("{} {}".format(result[0], result[1]))
# This program compute the sum of an array of numbers received as input

def sum(array):
    output = 0
    for i in array:
        output += i
    return output


quantity = int(input())
array = input()
list_nums = array.split(" ")
list_nums = list(map(int, list_nums))
result = sum(list_nums)

print(result)
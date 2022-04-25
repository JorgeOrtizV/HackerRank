# Suppose there are 2 trees, one gives apples, the other gives oranges. Sam wants to know how many apples and oranges
# fall in his house yard. The inputs are the following.
# Two integers separated by an space which means s and t. This are the limits of the backyard [s, t]
# Two integers separated by an space which means a and b. This numbers are the position of the apple tree (a) and the orange tree (b)
# Two integers separated by an space which means m and n. M means the number of fallen apples and n the number of fallen oranges
# A group of integers which mean the falling position of the apples.
# A group of integers which mean the falling position of the oranges.

# a<s<t<b -> Constraints rule
def fruits_in_backyard(limits, trees_position, apples, oranges):
    apples_count = 0
    oranges_count = 0
    result = []
    # Apples
    for i in range(len(apples)):
        falling_pos = trees_position[0] + apples[i]
        if(falling_pos >= limits[0]) and (falling_pos <= limits[1]):
            apples_count += 1
    for i in range(len(oranges)):
        falling_pos = trees_position[1] + oranges[i]
        if(falling_pos >= limits[0]) and (falling_pos <= limits[1]):
            oranges_count += 1
    result.append(apples_count)
    result.append(oranges_count)
    return result

limits = input()
limits = limits.split(" ")
limits = list(map(int, limits))
trees_position = input()
trees_position = trees_position.split(" ")
trees_position = list(map(int, trees_position))
number_of_fruits = input()
number_of_fruits = number_of_fruits.split(" ")
number_of_fruits = list(map(int, number_of_fruits))
apples = input()
apples = apples.split(" ")
apples = list(map(int, apples))
oranges = input()
oranges = oranges.split(" ")
oranges = list(map(int, oranges))

result = fruits_in_backyard(limits, trees_position, apples, oranges)
print(result[0])
print(result[1])
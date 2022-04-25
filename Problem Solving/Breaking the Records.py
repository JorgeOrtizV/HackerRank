# This program receives an input n, which means the number of scores the program will receive.
# The program will output a and b, a is the time the all-time highest score change. B means the times that the
# all-time lowest score has change.

def records(scores):
    highest = scores[0]
    lowest = scores[0]
    high_scores = 0
    low_scores = 0
    result = []
    for i in scores:
        if(i>highest):
            highest = i
            high_scores += 1
        if(i<lowest):
            lowest = i
            low_scores += 1
    result.append(high_scores)
    result.append(low_scores)
    return result

n = int(input())
numbers = input().split(" ")
numbers = list(map(int, numbers))
result = records(numbers)
print("{} {}".format(result[0], result[1]))
# This program receives an array of numbers positives, negatives or zeros.
# Returns the percentage of positives numbers, negatives and zeros. In that order

def percentage(list_nums, quantity):
    negatives = 0
    positives = 0
    zeros = 0
    result = []
    for i in list_nums:
        if i == 0:
            zeros+=1
        elif i < 0:
            negatives += 1
        else:
            positives += 1
    negatives = round(float(negatives/quantity), 6)
    positives = round(float(positives / quantity), 6)
    zeros = round(float(zeros / quantity), 6)
    result.append(positives)
    result.append(negatives)
    result.append(zeros)

    return result

quantity = int(input())
array = input()
list_nums = array.split(" ")
list_nums = list(map(int, list_nums))
result = percentage(list_nums, quantity)
for i in result:
    print(i)
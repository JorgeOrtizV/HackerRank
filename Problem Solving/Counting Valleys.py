# This problems receives an integer n, which means the number of steps that a hiker made. The receives an array composed
# by letters U and D. U means the hiker did a step up, D means the hiker did a step down. The hiker always begin and
# end at sea leve. A valley is a consecutive amount of steps that begin one value under sea level and end one value
# above sea level. The goal is to compute the number of valleys the hiker walked through.

def valleys(steps):
    height = 0
    num_valleys = 0
    valley_begin = 0
    for i in steps:
        if i == 'U':
            height += 1
        else:
            height -= 1
        if height == -1:
            valley_begin = 1
        if valley_begin == 1 and height == 0:
            num_valleys += 1
            valley_begin = 0
    print(num_valleys)


n = int(input())
steps = input()
valleys(steps)
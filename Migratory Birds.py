# The integer n means the number of inputs. The following line contains n integers. The goal is to compute the most
# spotted number. In case of a tie, return the smaller number of the most spotted.


from statistics import mode


n = int(input())
numbers = input().split(" ")
numbers = list(map(int, numbers))
try:
    print(mode(numbers))
except:
    indexes = [0] * n
    for i in numbers:
        indexes[i-1] += 1
    max_num = max(indexes)
    print(indexes.index(max_num)+1)


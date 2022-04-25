# This program receives a leaderboard, in which there are several scores sorted from highest to lowest scores.
# Then it receives a list of new scores, the goal is to return the place that those new scores will be in the leaderboard.
# new scores are given in ascending order.
# Equal scores have the same position, for example 100 -> 1, 80 -> 2, 80 -> 2, 70 -> 3 .....
# Inputs:
# First line: Integer l, which means number of scores in the leaderboard.
# Second line: l integers, which belong to the leaderboard.
# Third line: Integer s, which means the number of new scores
# Fourth line: s integers, which belong to the new scores array.
# Outputs:
# s lines, where the i-th line is the place of the i-th element of new scores array

# First approach, first of all get off of repetitions in leaderboard by creating a dict, and then turn it into a list.
# So we can know the place of the worst score in our leaderboard. Then while our new scores list isnt empty, we compare
# the last element of our leaderboard with the first in our new scores. if leaderboard[-1] is greater, then we append to our
# leaderboard a new position (l+1). If are the same, the new element has the same position than the previous last element (l)
# if it is bigger, just increase l, which is the position.
# if at the end of our comparisons new_scores isnt empty, just print n ones, where n is the current size of new_scores,
# because they are guaranteed to be bigger as leaderboard[0]


def scoreboard(leaderboard, new_scores, l):
    result = []
    while len(new_scores) > 0:
        if leaderboard[l-1] > new_scores[0]:
            result.append(l+1)
            new_scores.pop(0)
        elif leaderboard[-1] == new_scores[0]:
            result.append(l)
            new_scores.pop(0)
        else:
            l -= 1

        if (l == 0) and (len(new_scores) > 0):
            for i in new_scores:
                result.append(1)
            new_scores.clear()
    return result



l = int(input())
leaderboard = input().split(" ")
leaderboard = list(map(int, leaderboard))
s = int(input())
new_scores = input().split(" ")
new_scores = list(map(int, new_scores))
# First approach
leaderboard = list(dict.fromkeys(leaderboard))
l = len(leaderboard)
results = scoreboard(leaderboard, new_scores, l)
for i in results:
    print(i)



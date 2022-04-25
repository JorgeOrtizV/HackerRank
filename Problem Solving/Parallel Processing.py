# A computer has an specific amount of cores, each line of code is processed in time x.
# Each line takes one second. It could happen that the computer can use all its cores to
# divide the taken time between the number of cores, just if (number of lines % numCores ==0)
# There is also a limit in which we can use all the cores
# input:
# n -> length of files
# n integers per line, which represents the number of lines in each code
# numCores
# limit
# Output:
# Compute the minimal time to process all the code.

def minTime(files, numCores, limit):
    time = 0
    files.sort()
    files.reverse()
    for i in files:
        if limit > 0 and (i%numCores == 0):
            time += i/numCores
            limit -= 1
        else:
            time += i
    return int(time)

n = int(input())
files = []
for i in range(n):
    files.append(int(input()))
numCores = int(input())
limit = int(input())
result = minTime(files, numCores, limit)
print(result)
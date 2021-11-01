# A company wants to know how many of its customers visit the store the most.
# The program receive a integer number n, which means the lines of inputs.
# In the following lines the output is the name of the customers of the store.
# Each time the name appears means one visit.
# The output should be the customers who visited the store more at least 5% of
# the total amount of visits. The output should be in alphabetical order and line
# per line.


def traders(names, n):
    common_customers = []
    for key,val in names.items():
        percentage = (val/float(n)) * 100
        if percentage >= 5:
            common_customers.append(key)
    common_customers.sort()
    for i in common_customers:
        print(i)


n = int(input())
names = {}
temp = ""
for i in range(n):
    temp = input()
    if temp not in names:
        names[temp] = 1
    else:
        names[temp] += 1
traders(names, n)

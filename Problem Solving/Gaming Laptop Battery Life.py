# Suppose you have a laptop charged to 50%. You receive an integer n which
# means the number of events. Then consecutive integers in the following order:
# 5
# 2
# 9
# ...
# A positive integer means a minute that the battery is charged, a negative integer
# means a minute the laptop is used. Each minute is equal to a +-1% of battery.
# The program outputs the current amount of battery.

def battery(numbers):
    current_bat = 50
    for i in numbers:
        current_bat += i
        if current_bat > 100:
            current_bat = 100
        elif current_bat < 0:
            current_bat = 0
    print(current_bat)

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
battery(numbers)

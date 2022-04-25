# A widget manufacturer has an unexpected amount of work. He wants to know which is the
# maxium amount of orders he can do.
# The input n is the number of orders. Then the inputs are integers numbers, one per line
# Which means how many widgets require the order.
# Then the input is an integer k, which means the available amount of widgets.
# Return an integer, which means the maxium amount of orders the manufacturer can accomplish.

def filledOrders(orders, k):
    orders.sort()
    count = 0
    for i in orders:
        if i <= k:
            k -= i
            count += 1
    print(count)

n = int(input())
orders = []
for i in range(n):
    orders.append(int(input()))
k = int(input())
filledOrders(orders, k)
def chocolateCalculator(price, money, wraps):
    chocolates = money//price
    changable_wraps = chocolates
    while changable_wraps >= wraps:
        new_chocolates = changable_wraps//wraps
        chocolates += new_chocolates
        changable_wraps -= (new_chocolates*wraps)
        changable_wraps += new_chocolates
    return chocolates

if __name__ == "__main__":
    tests = int(input())
    for i in range(tests):
        money, price, wraps = list(map(int, input().split(' ')))
        result = chocolateCalculator(price, money, wraps)
        print(result)
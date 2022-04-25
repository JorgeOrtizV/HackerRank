# Given a lower limit and an upper limit, a and b respectively, determine
# the number of square digits between these limits.
import math

def num_squares(a,b):
    square_numbers = 0
    x = math.ceil(math.sqrt(a))
    while(x*x <= b):
        square_numbers+=1
        x+=1
    return square_numbers

if __name__ == "__main__":
    tests=int(input())
    for i in range(tests):
        a, b = list(map(int, input().split()))
        result = num_squares(a, b)
        print(result)
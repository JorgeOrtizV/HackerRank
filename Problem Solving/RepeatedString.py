# There is a string, s , of lowercase English letters that is repeated infinitely many times. Given an integer n , find and print the number of letter 
# a's in the first n letters of the infinite string s.
import math

def num_a(s,n):
    length=len(s)
    if length>n:
        return s[:n].count('a')
    else:
        repetitions = s.count('a')
        multiplier = math.floor(n/length)
        total = repetitions*multiplier
        remaining = n-length*multiplier
        if remaining>0:
            total += s[:remaining].count('a')
        return total

if __name__ == "__main__":
    s = input()
    n = int(input())
    result = num_a(s,n)
    print(result)
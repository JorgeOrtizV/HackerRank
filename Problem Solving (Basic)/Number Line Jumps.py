# Two kangaroos start in a position x and x2 respectively. Each kangaroo jump y amount of meters each time it moves.
# The goal is to calculate if it es possible that both kangaroos land in the same position at the same time.
# The program outputs "YES" if it is or "NO" if it isn't.
# Input: x1 v1 x2 v2.
# v -> meters per jump

def jumps(inputs):
    x1 = inputs[0]
    v1 = inputs[1]
    x2 = inputs[2]
    v2 = inputs[3]
    count = 0

    if ((x1 > x2) and (v1 > v2)) or ((x2 > x1) and (v2 > v1)):
        print("NO")
        return
    else:
        if(((x1-x2) % (v2-v1)) == 0) and ((v2-v1) != 0):
            print("YES")
            return
        else:
            print("NO")
            return

inputs = input().split(" ")
inputs = list(map(int, inputs))
jumps(inputs)
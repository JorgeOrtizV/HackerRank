from itertools import filterfalse

def stick_cutter(array, size):
    #import pdb; pdb.set_trace()
    sizes = []
    while(len(array)>0):
        sizes.append(size)
        smaller_stick = min(array)
        array = list(map(lambda x: x-smaller_stick, array))
        array = list(filterfalse(lambda x: x==0, array))
        size = len(array)
        
    return sizes


if __name__ == "__main__":
    size = int(input())
    array = list(map(int, input().split()))
    result = stick_cutter(array, size)
    for i in result:
        print(i)


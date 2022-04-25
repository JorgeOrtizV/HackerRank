def jumper(size, clouds):
    current_cloud = 0
    jumps=0
    while current_cloud != size-1:
        try:
            if clouds[current_cloud+2]==0:
                current_cloud+=2
            else:
                current_cloud+=1
        except:
            current_cloud+=1
        jumps+=1
    return jumps

if __name__ == "__main__":
    size = int(input())
    clouds = list(map(int, input().split(' ')))
    result = jumper(size, clouds)
    print(result)
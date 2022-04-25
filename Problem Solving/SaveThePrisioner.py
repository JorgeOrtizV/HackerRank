def candy_sorter(starting_chair, sweets, prisioners):
    return (sweets-1+starting_chair)%prisioners or prisioners

if __name__ == "__main__":
    tests = int(input())
    for i in range(tests):
        prisioners, sweets, starting_chair = list(map(int, input().split(' ')))
        result = candy_sorter(starting_chair, sweets, prisioners)
        print(result)

def energy_calculator(clouds, size, jump):
    energy = 100
    index = 0
    while (energy>0):
        if (index + jump) == size:
            if clouds[0] == 1:
                energy -= 3
            else:
                energy -= 1
            break
        index = (index+jump) % size
        if clouds[index] == 1:
            energy -= 3
        else:
            energy -= 1
    return energy


if __name__ == "__main__":
    size, jump = list(map(int, input().split()))
    clouds = list(map(int, input().split()))
    result = energy_calculator(clouds, size, jump)
    print(result)
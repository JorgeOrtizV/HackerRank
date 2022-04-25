def entire_divisor(number_string, number):
    count = 0
    for i in range(len(number_string)):
        try:
            if number%int(number_string[i]) == 0:
                count += 1
            else:
                pass
        except:
            pass
    return count



if __name__ == "__main__":
    tests = int(input())
    for i in range(tests):
        number_string = input()
        number = int(number_string)
        result = entire_divisor(number_string, number)
        print(result)

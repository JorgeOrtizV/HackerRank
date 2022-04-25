def kaprekarNumberCalculator(low_limit, up_limit):
    kaprekarNumbers = []
    while low_limit != (up_limit+1):
        #import pdb; pdb.set_trace()
        digits = len(str(low_limit))
        digits_neg = digits*-1
        str_square = str(low_limit**2)
        digits_square = len(str_square)
        if digits_square != 2*digits and digits_square != ((2*digits)-1):
            continue
        right_part = int(str_square[digits_neg:])
        try:
            left_part = int(str_square[:digits_neg])
        except:
            left_part = 0
        if (right_part+left_part) == low_limit:
            kaprekarNumbers.append(low_limit)
        low_limit+=1
    return kaprekarNumbers



if __name__ == "__main__":
    low_limit = int(input())
    up_limit = int(input())
    result = kaprekarNumberCalculator(low_limit, up_limit)
    if len(result) == 0:
        result_str = 'INVALID RANGE'
    else:
        result_str = list(map(str, result))
        result_str = " ".join(result_str)
    print(result_str)
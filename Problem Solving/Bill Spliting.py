# Two friends go and have dinner together. The want to split bills, but just pay for the elements the ate.
# The first input are integers n and k. N means the size of an array that includes the prices. k means the element of
# that prices array that friend number 2 clams he didn't ate from. All the other prices are splited.
# The last input is an integer b, which means the amount that friend 1 charge to friend 2.
# The program outputs "Bon Appetit" if the bills are properly splitted, or an integer x, which is the amount of money that
# friend 1 should give to friend 2 as change.

def bill_splitter(prizes, k, charge):
    deleted_prize = prizes[k]
    prizes.pop(k)
    splitted = sum(prizes)/2
    if(splitted == charge):
        print("Bon Appetit")
    else:
        print(int(charge - splitted))

constraints = input().split(" ")
constraints = list(map(int, constraints))
numbers = input().split(" ")
numbers = list(map(int, numbers))
charge = int(input())
bill_splitter(numbers, constraints[1], charge)
from math import comb

def BracketCombinations(num):
    if num == 0:
        return 1

    if num < 3:
        return num

    return comb(2 * num, num) // (num + 1)


# keep this function call here 
print(BracketCombinations(input()))

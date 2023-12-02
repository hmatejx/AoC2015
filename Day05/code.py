def isnice1(str):
    vowels = 0         # check for vowels
    for c in str:
        if c in ('a','e','i','o','u'):
            vowels += 1
    double = False     # check for duplicates
    for i in range(0, len(str)-1):
        if str[i+1] == str[i]:
            double = True
            break
    absent = True      # check for absence of ab, cd, pq, xy
    for bad in ('ab', 'cd', 'pq', 'xy'):
        if bad in str:
            absent = False
            break
    return vowels > 2 and double and absent

def isnice2(str):
    pairs = False      # check for pairs
    for i in range(0, len(str) - 1):
        pair = str[i:i+2]
        if pair in str[i+2:]:
            pairs = True
            break
    repeats = False    # check for repeats
    for i in range(0, len(str) - 2):
        if str[i+2] == str[i]:
            repeats = True
            break
    return pairs and repeats

c1, c2 = 0, 0
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
    for str in lines:
        if isnice1(str): c1 += 1
        if isnice2(str): c2 += 1

print("Part 1: {}".format(c1))
print("Part 1: {}".format(c2))

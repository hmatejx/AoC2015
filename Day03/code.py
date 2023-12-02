def give(i, j):
    pos = '{},{}'.format(i, j)
    house[pos] = house[pos] + 1 if house.get(pos) else 1

def update(i, j, move):
    if move == '<':
        i = i - 1
    elif move == '>':
        i = i + 1
    elif move == '^':
        j = j + 1
    else:
        j = j - 1
    return(i, j)

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        i, j = 0, 0
        house = {}
        give(i, j)
        for k in range(0, len(line)):
            i, j = update(i, j, line[k])
            give(i, j)
        print("Part 1: {}".format(len(house)))

    for line in lines:
        i1, j1, i2, j2 = [0]*4
        house = {}
        give(i1, j1)
        for k in range(0, len(line)):
            if k % 2 == 0:
                i1, j1 = update(i1, j1, line[k])
                give(i1, j1)
            else:
                i2, j2 = update(i2, j2, line[k])
                give(i2, j2)
        print("Part 2: {}".format(len(house)))

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

val = {'(': 1, ')': -1}

for line in lines:
    shifts = [val[p] for p in line]
    floor = [sum(shifts[0:i]) for i in range(1, len(line)+1)]
    for i in range(0, len(floor)):
        if floor[i] < 0:
            break
    print("Part 1: {}".format(sum(val[p] for p in line)))
    print("Part 2: {}".format(i + 1))

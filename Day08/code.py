with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
    res1 = res2 = 0
    for line in lines:
        exec('inmem=' + line)
        res1 += len(line) - len(inmem)
        line2 = '\"' + ''.join('\\' + c if c in ('"', '\\') else c for c in line) + '\"'
        res2 += len(line2) - len(line)

print("Part 1: {}".format(res1))
print("Part 2: {}".format(res2))

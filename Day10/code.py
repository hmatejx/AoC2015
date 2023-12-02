def look_and_say(seq):
    i = 0
    res = ''
    while i < len(seq):
        c = seq[i]
        j = 0
        while i + j < len(seq) and seq[i + j] == c:
            j += 1
        res += str(j) + c
        i += j
    return res

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        res = line
        for i in range(40):
            res = look_and_say(res)
        print("Part 1: {}".format(len(res)))
        for i in range(10):
            res = look_and_say(res)
        print("Part 2: {}".format(len(res)))

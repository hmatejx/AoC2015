lights1 = [[0]*1000 for i in range(0, 1000)]
lights2 = [[0]*1000 for i in range(0, 1000)]

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        cmd = line.replace(',', ' ').split(' ')
        if cmd[0] == 'turn':
            del cmd[0]
        x0, y0, x1, y1 = [int(xy) for xy in [cmd[i] for i in [1, 2, 4, 5]]]
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if cmd[0] == 'on':
                    lights1[y][x] = 1
                    lights2[y][x] += 1
                elif cmd[0] == 'off':
                    lights1[y][x] = 0
                    lights2[y][x] = max(0, lights2[y][x] - 1)
                else:
                    lights1[y][x] = 0 if lights1[y][x] else 1
                    lights2[y][x] += 2

print('Part 1: {}'.format(sum(list(map(sum, lights1)))))
print('Part 2: {}'.format(sum(list(map(sum, lights2)))))

from itertools import permutations

with open('input.txt') as file:
    dist = {}
    lines = [line.rstrip().split() for line in file]
    for line in lines:
        dist[line[0]] = dict()
        dist[line[2]] = dict()
    for line in lines:
        dist[line[2]][line[0]] = int(line[4])
        dist[line[0]][line[2]] = int(line[4])

# check all permutations
perm = list(permutations(dist.keys()))
perm = perm[0:len(perm) // 2]
walk = []
for p in perm:
    walk.append(sum(dist[p[i]][p[i + 1]] for i in range(len(p) - 1)))
print("Part 1: {}".format(min(walk)))
print("Part 2: {}".format(max(walk)))

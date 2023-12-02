from itertools import permutations

with open('input.txt') as file:
    dist = {}
    lines = [line.rstrip().split() for line in file]
    for line in lines:
        dist[line[0]] = dict()
    for line in lines:
        dist[line[0]][line[-1][:-1]] = (-1 if line[2] == 'lose' else 1) * int(line[3])

def max_score(d):
    n = len(d)
    perm = list(permutations(d.keys())) # check all cyclic permutations
    perm = perm[0:(len(perm) // n - 1)]
    score = [sum(d[p[i]][p[(i + 1) % n]] + d[p[i]][p[(i - 1) % n]] for i in range(n)) for p in perm]
    return max(score)

print("Part 1: {}".format(max_score(dist)))

# insert myself
dist['Me'] = dict()
for name in list(dist.keys()):
    dist['Me'][name] = 0
    dist[name]['Me'] = 0
print("Part 2: {}".format(max_score(dist)))

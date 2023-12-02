def dist(r, time=1000):
    speed, endurance, rest = r[1:]
    cycles = time // (endurance + rest)
    dist = speed * endurance * cycles
    t = (endurance + rest) * cycles
    remaining = time - t
    if remaining >= endurance:
        dist += speed*endurance
    else:
        dist += speed*remaining
    return dist

def score(reindeer, time=1000):
    dist = [0] * len(reindeer)
    timer  = dist.copy()
    resting = dist.copy()
    score = dist.copy()
    for t in range(time):
        for i in range(len(reindeer)):
            speed, endurance, rest = reindeer[i][1:]
            timer[i] += 1
            if not resting[i]:
                dist[i] += speed
                if timer[i] == endurance:
                    resting[i] = 1
                    timer[i] = 0
            else:
                if timer[i] == rest:
                    resting[i] = 0
                    timer[i] = 0
        for i in range(len(reindeer)):
            if dist[i] == max(dist):
                score[i] += 1
    return score

with open('input.txt') as file:
    lines = [line.rstrip().split() for line in file]
    reindeer = [[l[0], int(l[3]), int(l[6]), int(l[-2])] for l in lines]
    dist = [dist(r, 2503) for r in reindeer]

print("Part 1: {}".format(max(dist)))
print("Part 2: {}".format(max(score(reindeer, 2503))))

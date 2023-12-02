with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
    containers = [int(lines[i]) for i in range(len(lines))]

def next_steps(s):
    return [[s[0] - containers[i], s[1] + [i]] for i in range(len(containers)) if i not in s[1]]

def bfs(remaining=150):
    res = set()
    explored = set()
    front = [[remaining, []]]
    best = remaining
    while front:
        state = front.pop(0)
        for s in next_steps(state):
            ordered = tuple(sorted(s[1]))
            if ordered not in explored:
                explored.add(ordered)
                if s[0] > 0:
                    front.append(s)
                if s[0] == 0:
                    res.add(ordered)
    return res

res1 = bfs()
print("Part 1: {}".format(len(res1)))

minimum = min(map(len, res1))
print("Part 2: {}".format(len([r for r in res1 if len(r) == minimum])))

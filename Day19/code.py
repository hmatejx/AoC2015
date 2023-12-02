from random import shuffle

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
    rules, rules_reverse = {}, {}
    for line in [l.split() for l in lines[:-2]]:
        fr, to = line[0], line[2]
        if rules.get(fr):
            rules[fr].append(to)
        else:
            rules[fr] = [to]
        rules_reverse[to] = fr
    molecule = lines[-1]

def fission(current):
    res = set()
    for rule in rules.keys():
        i = 0
        d = len(rule)
        while True:
            if i >= len(current):
                break
            if (d == 1 and current[i] == rule) or (d == 2 and current[i] == rule[0] and current[i + 1] == rule[1]):
                for m in rules[rule]:
                    res.add(current[0:i] + m + current[i + d:])
            i += 1
    return res

def fusion(current):
    for k in greedy:
        i = current.rfind(k)
        if i >= 0:
            return(current[0:i] + rules_reverse[k] + current[i+len(k):])

print("Part 1: {}".format(len(fission(molecule))))

current = molecule
greedy = list(rules_reverse.keys())
greedy.sort(key=lambda x: -len(x))
greedy = [g for g in greedy if g[0:2] != 'CR']
i = 0
while current != 'e':
    i += 1
    new = fusion(current)
    if new is None: # dead-end, try again...
        shuffle(greedy)
        current = molecule
        i = 0
    else:
        current = new
print("Part 2: {}".format(i))

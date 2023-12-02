from sortedcontainers import SortedSet
from copy import deepcopy
from alive_progress import alive_bar
from math import prod

with open('input.txt') as file:
    items = [int(line.rstrip()) for line in file]
    items.sort(reverse=True)
    n = len(items)

def next_step(state, target, limit):
    new = []
    # first fill passenger compartment (take from right)
    if sum(state['p']) < target and len(state['p']) < limit:
        for item in state['i']:
            if (state['p'] and item > min(state['p'])) or sum(state['p']) + item > target:
                continue
            newstate = deepcopy(state)
            newstate['p'].append(item)
            newstate['i'].remove(item)
            new.append(newstate)
    return new

def balance(target, sizelimit):
    best = sizelimit
    with alive_bar() as bar:
        sols = []
        front = [{'p': [], 'i': items}]
        while front:
            state = front.pop()
            new_states = next_step(state, target, best)
            for new in new_states:
                if sum(new['p']) == target:
                    sols.append(new['p'])
                    if len(new['p']) < best:
                        best = len(new['p'])
                        print("new best: {}".format(best))
                front.append(new)
            bar()
    return sols

sols = balance(sum(items)/3, n//3)
res = [[len(sol), prod(sol)] for sol in sols]
minlen = min(res, key=lambda x: x[0])[0]
print("Part 2: {}".format(min([r for r in res if r[0] == minlen])[1]))

sols = balance(sum(items)/4, n//3)
res = [[len(sol), prod(sol)] for sol in sols]
minlen = min(res, key=lambda x: x[0])[0]
print("Part 2: {}".format(min([r for r in res if r[0] == minlen])[1]))

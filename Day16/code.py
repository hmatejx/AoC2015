result = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
          'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

with open('input.txt') as file:
    lines = [line.rstrip().replace(':', '').replace(',', '').split() for line in file]
    aunts = {}
    for l in lines:
        aunts[int(l[1])] = {l[2]: int(l[3]), l[4]: int(l[5]), l[6]: int(l[7])}

for i in range(500):
    sue = aunts[i + 1]
    candidate1 = candidate2 = True
    for item in sue.keys():
        candidate1 = result[item] == sue[item]
        if not candidate1: break
    for item in sue.keys():
        candidate2 = result[item] < sue[item] if item in ('cats', 'trees') else \
                     ( result[item] > sue[item] if item in ('pomeranians', 'goldfish') else \
                       result[item] == sue[item] )
        if not candidate2: break
    if candidate1:
        print("Part 1: {}".format(i + 1))
    if candidate2:
        print("Part 2: {}".format(i + 1))

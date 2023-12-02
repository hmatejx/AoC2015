import math

with open('input.txt') as file:
    input = file.read().split('\n\n')
    boss = input[0].split()
    boss = {'hp': int(boss[2]), 'damage': int(boss[4]), 'armor': int(boss[6])}

    def parse(shop):
        items = {}
        for line in shop.split('\n')[1:]:
            ls = line.split()
            if len(ls) > 4:
                ls = [ls[0] + ls[1]] + ls[2:]
            items[ls[0]] = {'cost': int(ls[1]), 'damage': int(ls[2]), 'armor': int(ls[3])}
        return items
    weapons = parse(input[1])
    armor = parse(input[2])
    rings = parse(input[3])
    armor[''] = {'cost': 0, 'damage': 0, 'armor': 0} # armor and ring are optional,
    rings[''] = {'cost': 0, 'damage': 0, 'armor': 0} # here hacked by a dummy item entry

def game(player, boss):
    player_dmg = max(1, player['damage'] - boss['armor'])
    boss_dmg = max(1, boss['damage'] - player['armor'])
    player_win = int(math.ceil(boss['hp'] / player_dmg))
    boss_win = int(math.ceil(player['hp'] / boss_dmg))
    return player_win <= boss_win

# part 1
scenarios = []
for w in weapons.keys():
    for a in list(armor.keys()):
        for r1 in list(rings.keys()):
            for r2 in list(rings.keys()):
                dam = weapons[w]['damage'] + rings[r1]['damage'] + rings[r2]['damage']
                ar = armor[a]['armor'] + rings[r1]['armor'] + rings[r2]['armor']
                cost = weapons[w]['cost'] +  armor[a]['cost'] + rings[r1]['cost'] +  rings[r2]['cost']
                scenarios.append({'hp': 100, 'damage': dam, 'armor': ar, 'cost': cost})
res1 = min([me['cost'] for me in scenarios if game(me, boss)])

# part 2
scenarios = []
for w in weapons.keys():
    for a in list(armor.keys()):
        for r1 in list(rings.keys()):
            for r2 in list(rings.keys()):
                if r2 == r1: continue # now the shopkeeper only has one of each items
                dam = weapons[w]['damage'] + rings[r1]['damage'] + rings[r2]['damage']
                ar = armor[a]['armor'] + rings[r1]['armor'] + rings[r2]['armor']
                cost = weapons[w]['cost'] +  armor[a]['cost'] + rings[r1]['cost'] +  rings[r2]['cost']
                scenarios.append({'hp': 100, 'damage': dam, 'armor': ar, 'cost': cost})
res2 = max([me['cost'] for me in scenarios if not game(me, boss)])

print("Part 1: {}".format(res1))
print("Part 2: {}".format(res2))

import math

with open('input.txt') as file:
    lines = [line.rstrip().split(': ') for line in file]
    boss = {'hp': int(lines[0][1]), 'damage': int(lines[1][1])}
    spells = {'recharge': {'cost': 229, 'mana': 101, 'turns': 5},
              'shield': {'cost': 113, 'armor': 7, 'turns': 6},
              'poison': {'cost': 173, 'damage': 3, 'turns': 6},
              'drain': {'cost': 73, 'damage': 2, 'heal': 2},
              'missile': {'cost': 53, 'damage': 4}}
    player = {'hp': 50, 'mana': 500}

def next_step(state, hard=False):
    new = []
    for s in spells.keys():
        boss, player, effects = state['boss'].copy(), state['player'].copy(), state['effects'].copy()
        # check if can't cast this spell
        if (state['effects'].get(s) and state['effects'][s] > 1):
            continue
        # *** PLAYER turn ***
        turn = 1
        if hard:
            player['hp'] -= 1
            # stop here if player dead
            if player['hp'] <= 0:
                continue
        # apply recharge effect to player
        if effects.get('recharge'):
            player['mana'] += spells['recharge']['mana']
        # check if the player can cast this spell
        if player['mana'] < spells[s]['cost']:
            continue
        # apply poison effect to boss
        if effects.get('poison'):
            boss['hp'] -= spells['poison']['damage']
        # update timers on effects and remove those that are worn off
        for e in list(effects.keys()):
            effects[e] -= 1
            if effects[e] == 0:
                del effects[e]
        # cast spell only if boss still alive
        if boss['hp'] > 0:
            player['mana'] -= spells[s]['cost']
            if s in ('missile', 'drain'):
                boss['hp'] -= spells[s]['damage']
                if s == 'drain':
                    player['hp'] += spells['drain']['heal']
            else:
                effects[s] = spells[s]['turns']
        # *** BOSS turn ***
        # only if alive, of course
        if boss['hp'] > 0:
            turn += 1
            # apply poison effect to boss
            if effects.get('poison'):
                boss['hp'] -= spells['poison']['damage']
            # apply recharge effect to player
            if effects.get('recharge'):
                player['mana'] += spells['recharge']['mana']
            # update timers on effects and remove those that are worn off
            for e in list(effects.keys()):
                effects[e] -= 1
                if effects[e] == 0:
                    del effects[e]
            # boss hit, only if still alive
            if boss['hp'] > 0:
                armor = spells['shield']['armor'] if effects.get('shield') else 0
                player['hp'] -= max(1, boss['damage'] - armor)
                # stop here if player dead
                if player['hp'] <= 0:
                    continue
            new.append({'player': player, 'boss': boss, 'effects': effects,
                        'turns': state['turns'] + turn, 'spells': state['spells'] + [s],
                        'mana_spent': state['mana_spent'] + spells[s]['cost']})
    return new

def game(hard=False):
    best = 100000000
    front = [{'player': player, 'boss': boss, 'effects': {}, 'turns': 0, 'spells': [], 'mana_spent': 0}]
    while front:
        state = front.pop()
        for n in next_step(state, hard):
            if n['boss']['hp'] <= 0 and n['mana_spent'] < best:
                best = n['mana_spent']
                continue
            # only continue with this state only if it makes sense
            if n['mana_spent'] < best:
                front.append(n)
    return best

print("Part 1: {}".format(game()))
print("Part 1: {}".format(game(hard=True)))

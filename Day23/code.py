from alive_progress import alive_bar

with open('input.txt') as file:
    lines = [line.rstrip().split() for line in file]
    commands = []
    for line in lines:
        if len(line) == 2:
            commands.append([line[0], int(line[1]) if len(line[1])> 1 else line[1]])
        else:
            commands.append([line[0], line[1][:-1], int(line[2])])

def cpu(a=0):
    regs = {'a': a, 'b': 0}
    with alive_bar() as bar:
        i = 0
        while i < len(commands) and i >= 0:
            c = commands[i]
            if c[0] == 'inc':
                regs[c[1]] += 1
                i += 1
            elif c[0] == 'hlf':
                regs[c[1]] //= 2
                i += 1
            elif c[0] == 'tpl':
                regs[c[1]] *= 3
                i += 1
            elif c[0] == 'jmp':
                i += c[1]
            elif c[0] == 'jie':
                if regs[c[1]] % 2 == 0:
                    i += c[2]
                else:
                    i += 1
            elif c[0] == 'jio':
                if regs[c[1]] == 1:
                    i += c[2]
                else:
                    i += 1
            bar()
    return regs

print("Part1: {}".format(cpu()['b']))
print("Part2: {}".format(cpu(a=1)['b']))

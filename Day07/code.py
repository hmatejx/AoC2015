# a dictionary to hold the results of already executed functions (caching)
variables = dict()

def setup(filename):
    # transform input lines into valid python code defining cached functions
    with open('input.txt') as file:
        variables.clear()
        lines = [line.rstrip().split() for line in file]
        for line in lines:
            l = '_' + line[-1]
            s = 'global ' + l + '\ndef '+ l + '():\n\tr=variables.get(\'' + l + '\')\n\tif r: return r\n\telse:\n\t\tres='
            if len(line) == 3:     # single value
                s += '_' + line[0] + '()' if not line[0].isnumeric() else line[0]
            elif len(line) == 4:   # NOT
                s += '(1 << 16) - 1 - ' + ('_' if not line[1].isnumeric() else '') + line[1] + '()'
            else:                  # AND OR LSHIFT RSHIFT
                c = line[1][0]
                op = ' & ' if c == 'A' else (' | ' if c == 'O' else (' << ' if c == 'L' else ' >> '))
                s += ('_' + line[0] + '()' if not line[0].isnumeric() else line[0]) + op + \
                     ('_' + line[2] + '()' if not line[2].isnumeric() else line[2])
            s += '\n\t\tvariables[\'' + l + '\']=res\n\t\treturn res'
            exec(s)

setup('input.txt')
res1 = _a()
print("Part 1: {}".format(res1))

setup('input.txt')
def _b(): return res1   # patch the value of wire b
print("Part 1: {}".format(_a()))

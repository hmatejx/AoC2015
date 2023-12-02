import re

def exclude_red(obj):
    if type(obj) == list:
        return sum(exclude_red(obj[i]) for i in range(len(obj)))
    elif type(obj) == dict:
        if "red" in obj.values():
            return 0
        else:
            return sum(exclude_red(item) for item in obj.values())
    elif type(obj) == int:
        return obj
    else:
        return 0

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        clean = re.sub(r'(\[|\]|\"|\:|\{|\}|[a-z])', '', line).split(',')
        print("Part 1: {}".format(sum(int(c) for c in clean if c != '')))
    for line in lines:
        exec('json=' + line)
        print("Part 2: {}".format(exclude_red(json)))

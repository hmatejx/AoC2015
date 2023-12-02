from hashlib import md5
from alive_progress import alive_bar

with open('input.txt') as file:
    s = file.readline().rstrip()
    i = 0
    with alive_bar() as bar:
        while True:
            i += 1
            ts = s + str(i)
            r = md5(ts.encode()).hexdigest()
            if r[0:5] == '00000':
                print('Part 1: {}'.format(i))
            if r[0:6] == '000000':
                print('Part 2: {}'.format(i))
                break
            bar()

from alive_progress import alive_bar

def setup(filename):
    with open(filename) as file:
        lights = [list(line.rstrip()) for line in file]
        nx, ny = len(lights[0]), len(lights)
    return lights, nx, ny

def neighbors(state, x, y):
    n = 0
    for i in range(max(0, x - 1), min(x + 2, nx)):
        for j in range(max(0, y - 1), min(y + 2, ny)):
            if state[j][i] == '#':
                n += 1
    return n - (state[y][x] == '#')

def life(lights, niter, corners=False):
    res = [line.copy() for line in lights]
    with alive_bar(niter) as bar:
        for i in range(niter):
            new = [line.copy() for line in res]
            for x in range(nx):
                for y in range(ny):
                    if corners and ((x == 0 and (y == 0 or y == ny - 1)) or (x == nx - 1 and (y == 0 or y == ny - 1))):
                        continue
                    n = neighbors(res, x, y)
                    if res[y][x] == '#' and (n < 2 or n > 3):
                        new[y][x] = '.'
                    if res[y][x] == '.' and n == 3:
                        new[y][x] = '#'
            res = new
            bar()
    return res

lights, nx, ny = setup('input.txt')
res1 = life(lights, 100)
print("Part 1: {}".format(sum(len([1 for l in line if l == '#']) for line in res1)))

lights, nx, ny = setup('input.txt')
# patch corners
lights[0][0] = lights[ny-1][0] = lights[0][nx-1] = lights[ny-1][nx-1] = '#'
res2 = life(lights, 100, corners=True)
print("Part 2: {}".format(sum(len([1 for l in line if l == '#']) for line in res2)))

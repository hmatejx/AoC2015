wrap = 0
ribbon = 0
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        dims = [int(d) for d in line.split('x')]
        dims.sort()
        l, w, h = dims
        wrap1 = 2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)
        wrap += wrap1
        ribbon1 = 2*sum(dims[0:2]) + dims[0]*dims[1]*dims[2]
        ribbon += ribbon1

print("Part 1: {}".format(wrap))
print("Part 2: {}".format(ribbon))

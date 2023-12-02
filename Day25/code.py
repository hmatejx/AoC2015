# input
row = 2981
col = 3075

idx = col + (row + col - 1) * (row + col - 2) // 2

x = 20151125
a = 252533
b = 33554393

for i in range(idx - 1):
    x = (x * a) % b
print(x)

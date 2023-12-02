with open('input.txt') as file:
    lines = [line.rstrip().replace(',', '').split() for line in file]
    ingredients = [[l[0][:-1]] + [int(l[i]) for i in (2, 4, 6, 8, 10)] for l in lines]
    print(ingredients)

score = []
for i in range(101):
    for j in range(0, 101 - i):
        for k in range(0, 101 - i - j):
            l = 100 - i - j - k
            capacity =   max(0, i*ingredients[0][1] + j*ingredients[1][1] + k*ingredients[2][1] + l*ingredients[3][1])
            durability = max(0, i*ingredients[0][2] + j*ingredients[1][2] + k*ingredients[2][2] + l*ingredients[3][2])
            flavor =     max(0, i*ingredients[0][3] + j*ingredients[1][3] + k*ingredients[2][3] + l*ingredients[3][3])
            texture =    max(0, i*ingredients[0][4] + j*ingredients[1][4] + k*ingredients[2][4] + l*ingredients[3][4])
            calories =   max(0, i*ingredients[0][5] + j*ingredients[1][5] + k*ingredients[2][5] + l*ingredients[3][5])
            score.append([[i, j, k, l], capacity*durability*flavor*texture, calories])

print("Part 1: {}".format(max(score, key=lambda x: x[1])))
print("Part 1: {}".format(max([s for s in score if s[2] == 500], key=lambda x: x[1])))

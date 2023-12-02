import math

input = 33100000

def factors(n):
    res = set([1, n])
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return res

# handles both parts (not optimal, but fast enough)
def presents(n, part=1):
    if part == 1:
        return sum([10*f for f in factors(n)])
    else:
        return sum([11*f for f in factors(n) if n/f <= 50])

# build highly composite numbers (will have a lot of factors and hence are good candidates)
front = set(((2,),))
primes = (2, 3, 5, 7, 11, 13, 17) # empirical...
i = 0
res1 = res2 = input // 10
while front:
    i += 1
    rep = list(front.pop())
    num = math.prod(rep)
    if presents(num) > input and num < res1:
        res1 = num
    if presents(num, 11) > input and num < res2:
        res2 = num
    for p in primes:
        new = rep + [p]
        new.sort()
        new = tuple(new)
        if new not in front and math.prod(new) < max(res1, res2):
            front.add(new)

print("Part 1: {}".format(res1))
print("Part 2: {}".format(res2))

import random
from dist_utils import dist
import math

def gen_planets(x1, x2, y1, y2, r, i):
    positions = [[0, 0]]
    for j in range(0, 2000):
        while True:
            pos = [random.randint(x1, x2), random.randint(y1, y2)]
            dists = [dist(pos, pos2) for pos2 in positions]
            if any(k < r for k in dists):
                continue
            #calc odds of success / i
            m = min(dists)
            d = i - abs(i-m)
            #odds ~= m / i
            if random.randint(0, 10000) / 10000 < d / i:
                break
        positions.append(pos)
    return positions

x1 = -100
x2 = 100
y1 = -100
y2 = 100
r = 1
i = 10

for y in range(y1, y2+1):
    for x in range(x1, x2+1):
        if [x, y] in gen_planets(x1, x2, y1, y2, r, i):
            print('#', end='')
        else:
            print('.', end='')
    print()
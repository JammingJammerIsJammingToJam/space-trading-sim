import random
from dist_utils import dist
from dist_utils import dijkstra
import math

def gen_planets(x1, x2, y1, y2, r, i, p):
    positions = [[0, 0]]
    for j in range(0, p):
        while True:
            pos = [random.randint(x1, x2), random.randint(y1, y2)]
            dists = [dist(pos, pos2) for pos2 in positions]
            if any(k <= r for k in dists):
                continue
            #calc odds of success / i
            m = min(dists)
            d = i - abs(i-m)
            #odds ~= m / i
            if random.randint(0, 10000) / 10000 < d / i:
                break
        positions.append(pos)
    return positions

def planet_names(positions):
    names = []
    for _ in range(len(positions)):
        syllables = ['ka', 'ke', 'ku', 'ko', 'ki',
            'sha', 'shi', 'su', 'se', 'so',
            'ha', 'hi', 'hu', 'he', 'ho',
            'ta', 'te', 'tu', 'ti', 'to',
            'ya', 'ye', 'yu', 'yo', 'yi',
            'tha', 'the', 'thi', 'thu', 'thi', 'thro',
            'xi', 'xu', 'xe', 'xa', 'xo',
            'da', 'di', 'du', 'de', 'do',
            'ja', 'ji', 'ju', 'je', 'jo',
            'za', 'ze', 'zu', 'zi', 'zo',
            "'l", 'la', 'li', 'lu', 'le', 'lo',
            'fa', 'fe', 'fu', 'fi', 'fo',
            'cha', 'chi', 'chu', 'che', 'cho'
        ]
        name = ''
        n_words = random.randint(1, 2)
        if n_words == 2:
            for i in range(0, random.randint(2, 5)):
                name += random.choice(syllables)
            name += ' '
        for i in range(0, random.randint(2, 5)):
            name += random.choice(syllables)
        name = ' '.join([part.capitalize() for part in name.split(' ')])
        if name not in names:
            names.append(name)
    return names


        


x1 = -100
x2 = 100
y1 = -100
y2 = 100
r = 2
i = 30
p = 100
print('     '.join(planet_names(gen_planets(x1, x2, y1, y2, r, i, p))))
"""
planets = gen_planets(x1, x2, y1, y2, r, i, p)
for y in range(y1, y2+1):
    for x in range(x1, x2+1):
        if [x, y] in planets:
            print('#', end='')
        else:
            print('.', end='')
    print()
"""
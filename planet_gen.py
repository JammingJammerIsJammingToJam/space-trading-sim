import random
from dist_utils import dist
from dist_utils import dijkstra
import math

def gen_system_positions(x1, x2, y1, y2, r, i, p):
    positions = [[0, 0]]
    for j in range(0, p-1):
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
    i = 0
    while i < len(positions):
        syllables = ['ka', 'ke', 'ku', 'ko', 'ki',
            'sha', 'shi', 'su', 'se', 'so',
            'ha', 'hi', 'hu', 'he', 'ho',
            'ta', 'te', 'tu', 'ti', 'to',
            'the', 'thi', 'thu','thro',
            'xi', 'xu', 'xe', 'xa', 'xo',
            'da', 'di', 'du', 'de', 'do',
            'ja', 'ji', 'ju', 'je', 'jo',
            'za', 'ze', 'zu', 'zi', 'zo',
            'la', 'li', 'lu', 'le', 'lo',
            'fe', 'fu', 'fi',
            'cha', 'chi', 'chu', 'che', 'cho',
            'ya', 'yu', 'yo', 'yi',
        ]
        name = ''
        n_words = random.randint(1, 2)
        if n_words == 2:
            for _ in range(0, random.randint(2, 5)):
                name += random.choice(syllables)
            name += ' '
        for _ in range(0, random.randint(2, 5)):
            name += random.choice(syllables)
        name = ' '.join([part.capitalize() for part in name.split(' ')])
        if name not in names:
            names.append(name)
            i += 1
    return names

def gen_systems(x1, x2, y1, y2, r, i, p):
    positions = gen_system_positions(x1, x2, y1, y2, r, i, p)
    names = planet_names(positions)
    systems = []
    for i in range(len(positions)):
        name = names[i]
        x = positions[i][0]
        y = positions[i][1]
        faction = random.randint(1, 4)
        
        planets = []
        planet_number = random.randint(1, 10)
        system_resource = random.randint(0, 5)
        for j in range(planet_number):
            planet = [0 for _ in range(6)]
            planet_resource = random.randint(0, 5)
            total = random.randint(61, 128)
            if random.randint(0, 100) > 95:
                total = random.randint(128, 320)
            planet[system_resource] += random.randint(10, 25)
            planet[planet_resource] += random.randint(10, 35)
            for k in range(total - sum(planet)):
                n = random.randint(0, 5)
                planet[n] += 1
                if planet[n] > 61:
                    planet[n] = 61
            planets.append(planet)
        system = [name, x, y, faction]
        for planet in planets:
            system.append(planet)
        systems.append(system)
    return systems
           

            




x1 = 0
x2 = 3843
y1 = 0
y2 = 3843
r = 2
i = 30
p = 1000

#print(gen_systems(x1, x2, y1, y2, r, i, p))
"""
print('     '.join(planet_names(gen_systems(x1, x2, y1, y2, r, i, p))))

planets = gen_systems(x1, x2, y1, y2, r, i, p)
for y in range(y1, y2+1):
    for x in range(x1, x2+1):
        if [x, y] in planets:
            print('#', end='')
        else:
            print('.', end='')
    print()
"""
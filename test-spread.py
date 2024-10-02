from random import randint
from math import sqrt
systems = open("systems.txt", "w")
systems.close()
s = open("systems.txt", "a")
def abc():
  a = random.randint(0, x)
  b = random.randint(0, y)
  c = random.randint(0, z)
def gen_points(x, y, z, ptotal, mindis, maxdis):
  abc()
  s.write(a, "\n", b, "\n", c)
  for i in range(0, ptotal):
    done = 0
    while done != 1
      abc()
      f = open("systems.txt", "r")
      g = f.readlines
      shortestdist = maxdis + 1
      for item in range(1, len(g) + 1, 3):
        x1 = g[item]
        y1 = g[item + 1]
        z1 = g[item + 2]
        dist = sqrt((a - x1)**2 + (b - y1)**2 + (c - z1)**2)
        if dist < mindis:
          continue
      s.write("\n", a, "\n", b, "\n", c)
      done = 1
gen_points(100, 100, 100, 10, 5, 10
s.close()
s = open("systems.txt", "r")
print(s.readlines())

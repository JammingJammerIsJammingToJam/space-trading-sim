from random import randint
from math import sqrt
systems = open("systems.txt", "w")
systems.close()
s = open("systems.txt", "a")
  
def gen_points(x, y, z, ptotal, mindis, maxdis):
  a = randint(0, x)
  b = randint(0, y)
  c = randint(0, z)
  s.write(str(a) + "\n")
  s.write(str(b) + "\n")
  s.write(str(c))
  for i in range(0, ptotal):
    done = 0
    while done != 1:
      a = randint(0, x)
      b = randint(0, y)
      c = randint(0, z)
      f = open("systems.txt", "r")
      g = f.readlines()
      shortestdist = maxdis + 1
      for item in range(1, len(g) + 1, 3):
        x1 = g[item]
        y1 = g[item + 1]
        z1 = g[item + 2]
        dist = sqrt((a - x1)**2 + (b - y1)**2 + (c - z1)**2)
        if dist < mindis:
          continue
      s.write("\n" + str(a))
      s.write("\n" + str(b))
      s.write("\n" + str(c))
      done = 1
gen_points(100, 100, 100, 10, 5, 10)
s.close()
s = open("systems.txt", "r")
for item in s.readlines():
  print(item)

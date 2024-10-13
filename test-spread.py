from random import randint
from math import sqrt
from namegenerator import *
import os
def checkSave(file):
  if os.path.isfile(file):
    return open(file, "a")
  else:
    j = open(file, "w")
    j.close()
    return open(file, "a")  
s = checkSave("systems.txt")
def gen_points(x, y, z, ptotal, mindis, maxdis):
  a = randint(0, x)
  b = randint(0, y)
  c = randint(0, z)
  s.write(gen_name(4) + "\n")
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
      # shortestdist = maxdis + 1
      for item in range(1, len(g) + 1, 4):
        x1 = g[item + 1]
        y1 = g[item + 2]
        z1 = g[item + 3]
        dist = sqrt((a - x1)**2 + (b - y1)**2 + (c - z1)**2)
        if dist < mindis:
          continue
      k = 0
      while k != 1:
        name = gen_name(4)
        for jail in range(1, len(g) + 1, 4):
          if g[jail] == name:
            continue
        k = 1
      s.write("\n" + name)
      s.write("\n" + str(a))
      s.write("\n" + str(b))
      s.write("\n" + str(c))
      done = 1
    cyclone = open("systems.txt", "r")
    plasma = checkSave("planets.txt")
    for item in cyclone.readlines():
      k = 0
      while k != 1:
        name = gen_name(5)
        for jail in range(1, len(cyclone) + 1):
          if cyclone[jail] == name:
            continue
        k = 1
      plasma.write(name)
    plasma.close()
gen_points(100, 100, 100, 10, 5, 10)
s.close()
s = open("systems.txt", "r")
for item in s.readlines():
  print(item)
jailbreaker = open("planets.txt", "r")
for item in jailbreaker.readlines():
  print(item)

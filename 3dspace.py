from math import *
playerx = 0
playery = 0
playerz = 0
corners = [1, 1, 1, 2, 2, 2]
raysy = [-45, -30, -15, 15, 30, 45]
raysx = [-45, -30, -15, 15, 30, 45]
def isAngleInRange(ymax, ymin, xmax, xmin, x1, y1, z1, x2, y2, z2):
  distance = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
  ydif = y1-y2
  yang = degrees(asin(ydif/distance))
  if yang < ymin or yang > ymax:
    return False
  zdif = z1-z2
  xdif = x1-x2
  yin = degrees(atan(xdif/zdif))
  if yin < xmin or yin > xmax:
    return False
  return True
for i in range(0, 4, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            for l in range(0, 3):
                for q in range(0, 5):
                    for w in range(0, 5):
                        if isAngleInRange(raysy[q]+10, raysy[q]-10, raysx[w]+10, raysx[w]-10, playerx, playery, playerz, corners[i]+j, corners[i+1]+k, corners[i+2]+l) == True:
                          print(raysy[q], raysx[w])

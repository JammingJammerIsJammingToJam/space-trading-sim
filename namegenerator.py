import random
sylib = ["to","cha","ven","pol","sin","ka","yo","lu","cam","pin","ma","nur","jin","gon","ho","bu","quan","xi","zha","ju"]
def gen_name(connum):
  text = ""
  for i in range(0, connum):
    text += sylib[random.randint(0, 19)]
  return str.capitalize(text)

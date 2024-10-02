import os 
def insert_data(filename, position, data_to_insert):
  with open(filename, 'r') as f:
    lines = f.readlines()
  lines.insert(position - 1, data_to_insert + '\n')  
  with open(filename, 'w') as f:
    f.writelines(lines)
def checkSave():
  if os.path.isfile("save.txt"):
    return open("save.txt", "r")
  else:
    j = open("save.txt", "w")
    j.close()
    return open("save.txt", "r")
def nameCheck():
  s = open("save.txt", "r")
  j = s.readline()
  if j == "":
    insert_data("save.txt", 1, input("What Is Your Name Space Cadet? "))
    s = open("save.txt", "r")
    return s.readline()
  else:
    return j

import os
""" PARTE COMUNE  """
f = open((os.path.dirname(__file__) + '\day3_input'), 'r')
inputNum = []
temp = f.read()
temp = temp.split("\n")
f.close()

""" PARTE UNO """
pos = 0
countAlberi = 0
X_OFFSET = 3
for i in temp:
    if i[pos] == '#':
        countAlberi += 1
    pos = (pos+X_OFFSET)%len(i)
print("Totale alberi incontrati: " + str(countAlberi))
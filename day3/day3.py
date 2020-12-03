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


""" PARTE DUE """
countAlberi = [0,0,0,0,0]
X_OFFSET = 1
for j in range (4):
    pos = 0
    for i in temp:
        if i[pos] == '#':
            countAlberi[j] += 1
        pos = (pos+X_OFFSET)%len(i)
    X_OFFSET += 2

even = 1
for i in temp:
    X_OFFSET = 1
    if(even%2):
        if i[pos] == '#':
            countAlberi[4] += 1
        pos = (pos+X_OFFSET)%len(i)
    even += 1

print("Totale alberi incontrati: " + str(countAlberi[0]*countAlberi[1]*countAlberi[2]*countAlberi[3]*countAlberi[4]))
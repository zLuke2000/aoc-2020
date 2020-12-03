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
for i in temp:
    if i[pos] == '#':
        print("Sentiero: "+ i + "Trovato un albero in posizione: " + str(pos))
        countAlberi += 1
    else:
        print("Sentiero: "+ i + "Nessun albero in posizione: " + str(pos))
    pos = (pos+3)%33
print("Totale alberi incontrati: " + str(countAlberi))
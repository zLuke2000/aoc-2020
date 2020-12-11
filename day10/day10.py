import os
from collections import defaultdict
""" PARTE COMUNE """
f = open((os.path.dirname(__file__) + '\day10_input'), 'r')
temp = f.read()
temp = temp.split("\n")
f.close()

#conversione String -> Int
for i in range(0, len(temp)): 
    temp[i] = int(temp[i])

""" PARTE UNO """
Jolts = 0
diffOf1, diffOf3 = 0,0
temp = set(temp)
for i in temp:
    diff = i - Jolts
    if diff == 1:
        diffOf1 += 1
        Jolts += 1
    elif diff == 3:
        diffOf3 += 1
        Jolts += 3
diffOf3 += 1
print("DIFF 1:", diffOf1, "DIFF 3:", diffOf3, "--->", "Soluzione:", diffOf1*diffOf3)

""" PARTE DUE """
temp2 = sorted(temp)
possibilita = {0: 1}

for i in temp2:
    count = 0
    for j in range(1, 4):
        if (i-j) in possibilita:
            count += possibilita[i-j]
    possibilita[i] = count

print("Numero di possibili soluzioni:", possibilita[temp2[-1]])
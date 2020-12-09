import os
""" PARTE UNO """
f = open((os.path.dirname(__file__) + '\day9_input'), 'r')
temp = f.read()
temp = temp.split("\n")
f.close()
for i in range(0, len(temp)): 
    temp[i] = int(temp[i])

""" PARTE DUE """
numCorrente = 0
for i in range(25,len(temp)):
    sommePossibili = []
    numCorrente = temp[i]
    for j in range(i-25,i):
        for k in range(i-25,i):
            if temp[j] != temp[k]:
                sommePossibili.append(temp[j]+temp[k])
    if numCorrente not in sommePossibili:
        print("Numero:", numCorrente)
        break

""" PARTE DUE """
for i in range(len(temp)):
    somma = 0
    numeri = []
    for j in range(i, len(temp)):
        numeri.append(temp[j])
        somma += temp[j]
        if somma > numCorrente:
            break
        if somma == numCorrente:
            print("Min + Max dei numeri:", min(numeri)+max(numeri))
            break
    break
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
            sommePossibili.append(temp[j]+temp[k])
    if numCorrente not in sommePossibili:
        print("Numero:", numCorrente)
        break

""" PARTE DUE """
for i in range(len(temp)-3):
    somma = temp[i] + temp[i+1] + temp[i+2] + temp[i+3]
    if somma == numCorrente:
        print("Min + Max dei 4 numeri:", (min(temp[i], temp[i+1], temp[i+2], temp[i+3]) + min(temp[i], temp[i+1], temp[i+2], temp[i+3])))
        break
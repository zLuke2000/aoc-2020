import os
""" PARTE UNO """
f = open((os.path.dirname(__file__) + '\day6_input'), 'r')
temp = f.read()
temp = temp.split("\n")
f.close()
temp.append('')

tempString = ""
risposte = 0
for i in temp:
    if i != '':
        tempString += i
    else:
        risposte += len(set(tempString))
        tempString = ""
print("Totale risposte:", risposte)

""" PARTE DUE """
temp.pop() #rimuove l'elemento vuoto inserito alla riga 7 per risolvere il probelma 1

group = []
risposte = 0
for i in temp:
    i = i.strip()
    if i == "":
        risposte += len(set.intersection(*group))
        group = []
        continue  
    group.append(set([j for j in i]))
risposte += len(set.intersection(*group))
print("Totale risposte:", risposte)
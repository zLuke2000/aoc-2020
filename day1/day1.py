import os

""" PARTE COMUNE  """
f = open((os.path.dirname(__file__) + '\day1_input'), 'r')
inputNum = []
temp = f.read()
temp = temp.split("\n")
f.close()

""" PARTE UNO """
again = True

for i in temp:
    if(again):
        for j in temp:  
            if(again):
                tempI = int(i)
                tempJ = int(j)
                if(tempI + tempJ == 2020):
                    print(tempI*tempJ)
                    again = False

""" PARTE DUE """
again = True

for i in temp:
    if(again):
        for j in temp:  
            if(again):
                for k in temp:
                    if(again):
                        tempI = int(i)
                        tempJ = int(j)
                        tempK = int(k)
                        if(tempI + tempJ + tempK == 2020):
                            print(tempI*tempJ*tempK)
                            again = False
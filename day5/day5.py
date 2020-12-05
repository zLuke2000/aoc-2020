import os
""" PARTE COMUNE  """
f = open((os.path.dirname(__file__) + '\day5_input'), 'r')
inputNum = []
temp = f.read()
temp = temp.split("\n")
f.close()

""" PARTE UNO """
seatID = []
for i in temp:
    seatX = [0,127]
    seatY = [0,7]
    seatXY = [0,0]
    currentChar = 0
    for index in i:
        currentChar += 1
        if(index == 'F'):
            if(currentChar == 7):
                seatXY[0] = seatX[0]
            else:
                seatX[1] -= int(((seatX[1]-seatX[0])/2)+0.5)
        if(index == 'B'):
            if(currentChar == 7):
                seatXY[0] = seatX[1]
            else:
                seatX[0] += int(((seatX[1]-seatX[0])/2)+0.5)
        if(index == 'R'):
            if(currentChar == 10):
                seatXY[1] = seatY[1]
            else:
                seatY[0] += int(((seatY[1]-seatY[0])/2)+0.5)
        if(index == 'L'):
            if(currentChar == 10):
                seatXY[1] = seatY[0]
            else:
                seatY[1] -= int(((seatY[1]-seatY[0])/2)+0.5)
    seatID.append(seatXY[0]*8+seatXY[1])
print("SeatID più alto:", max(seatID))

""" PARTE DUE """
seatID = sorted(seatID)
j = min(seatID)
for i in seatID:
    if i != j:
        print("SeatID mancante:", i)
        break
    j += 1
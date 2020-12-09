import os
""" PARTE UNO """
f = open((os.path.dirname(__file__) + '\day8_input'), 'r')
temp = f.read()
temp = temp.split("\n")
f.close()

""" PARTE UNO """
pc = 0
acc = 0
istruzione = ""
instHistory = []
while(True):
    istruzione = temp[pc].split()
    istruzione[1] = int(istruzione[1])
    if pc in instHistory:
        break
    else:
        instHistory.append(pc)
        if istruzione[0] == "acc":
            acc += istruzione[1]
            pc +=1
        elif istruzione[0] == "jmp":
            pc += istruzione[1]
        elif istruzione[0] == "nop":
            pc += 1
print("ACC:", acc)

""" PARTE DUE """

for i in range(len(temp)):
    tempSplit = temp.copy()
    if "jmp" in tempSplit[i] or "nop" in tempSplit[i]:
        tempSplit[i] = tempSplit[i].split()
        if tempSplit[i][0] == "jmp":
            tempSplit[i][0] = "nop "
        elif tempSplit[i][0] == "nop":
            tempSplit[i][0] = "jmp "
        tempSplit[i] = tempSplit[i][0]+tempSplit[i][1]

        pc = 0
        acc = 0
        istruzione = ""
        instHistory = []
        while(True):
            istruzione = tempSplit[pc].split()
            istruzione[1] = int(istruzione[1])
            if pc in instHistory:
                break
            elif pc == len(tempSplit)-1:
                print("Programma completato! ACC:", acc)
                break
            else:
                instHistory.append(pc)
            if istruzione[0] == "acc":
                acc += istruzione[1]
                pc +=1
            elif istruzione[0] == "jmp":
                pc += istruzione[1]
            elif istruzione[0] == "nop":
                pc += 1
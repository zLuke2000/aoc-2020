import os
""" PARTE COMUNE  """
f = open((os.path.dirname(__file__) + '\day2_input'), 'r')
inputNum = []
temp = f.read()
temp = temp.split("\n")
f.close()

""" PARTE UNO """
countTrue = 0
for i in temp:
    minChar = i.split('-', 1)
    minChar = int(minChar[0])
    maxChar = i.split('-', 1)
    maxChar = maxChar[1].split(None, 1)
    maxChar = int(maxChar[0])
    currentChar = i.split(None, 1)
    currentChar = currentChar[1].split(':', 1)
    currentChar = str(currentChar[0])
    password =  i.split()
    password = str(password[2])

    count = password.count(currentChar)
    if  count >= minChar and count <= maxChar:
        countTrue +=1
print("Password corrette: " + str(countTrue))

""" PARTE DUE """
countTrue = 0
for i in temp:
    minChar = i.split('-', 1)
    minChar = int(minChar[0])
    maxChar = i.split('-', 1)
    maxChar = maxChar[1].split(None, 1)
    maxChar = int(maxChar[0])
    currentChar = i.split(None, 1)
    currentChar = currentChar[1].split(':', 1)
    currentChar = str(currentChar[0])
    password =  i.split()
    password = str(password[2])

    if password[minChar-1] == currentChar:
        if not password[maxChar-1] == currentChar:
            countTrue += 1
    else:
        if password[maxChar-1] == currentChar:
            countTrue += 1
print("Password corrette: " + str(countTrue))

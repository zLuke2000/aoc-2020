import os
""" PARTE COMUNE  """
f = open((os.path.dirname(__file__) + '\day4_input'), 'r')
inputNum = []
temp = f.read()
f.close()
temp = temp.split("\n\n")
i = 0 
for x in temp:
    temp[i] = x.replace("\n", " ")
    i += 1

""" PARTE UNO """
count = 0
for x in temp:
    valido = True
    if "byr:" not in x:
        valido = False
    if "iyr:" not in x:
        valido = False
    if "eyr:" not in x:
        valido = False
    if "hgt:" not in x:
        valido = False
    if "hcl:" not in x:
        valido = False
    if "ecl:" not in x:
        valido = False
    if "pid:" not in x:
        valido = False
    if(valido):
        count += 1
print("Passaporti validi:", count)

""" PARTE DUE """
count = 0
for x in temp:
    valido = True
    if "byr:" in x:
        byr = x.split("byr:")
        byr = byr[1].split()
        byr = int(byr[0])
        if byr < 1920 or byr > 2002:
            valido = False
    else:
        valido = False
    if "iyr:" in x:
        iyr = x.split("iyr:")
        iyr = iyr[1].split()
        iyr = int(iyr[0])
        if iyr < 2010 or iyr > 2020:
            valido = False
    else:
        valido = False
    if "eyr:" in x:
        eyr = x.split("eyr:")
        eyr = eyr[1].split()
        eyr = int(eyr[0])
        if eyr < 2020 or eyr > 2030:
            valido = False
    else:
        valido = False
    if "hgt:" in x:
        hgt = x.split("hgt:")
        hgt = hgt[1].split()
        if 'cm' in hgt[0]:
            hgt = hgt[0].split("cm")
            hgt = int(hgt[0])
            if hgt < 150 or hgt > 193:
                valido = False
        elif "in" in hgt[0]:
            hgt = hgt[0].split("in")
            hgt = int(hgt[0])
            if hgt < 59 or hgt > 76:
                valido = False
        else:
            valido = False
    else:
        valido = False
    if "hcl:" in x:
        hcl = x.split("hcl:")
        hcl = hcl[1].split()
        if '#' in hcl[0] and len(hcl[0]) == 7:
            pass
        else:
            valido = False
    else:
        valido = False
    if "ecl:" in x:
        ecl = x.split("ecl:")
        ecl = ecl[1].split()
        ecl = ecl[0]
        if ecl == "amb" or ecl == "blu" or ecl ==  "brn" or ecl ==  "gry" or ecl ==  "grn" or ecl ==  "hzl" or ecl == "oth":
            pass
        else:
            valido = False
    else:
        valido = False
    if "pid:" in x:
        pid = x.split("pid:")
        pid = pid[1].split()
        pid = pid[0]
        if len(pid) == 9:
            pass
        else:
            valido = False
    else:
        valido = False
    if(valido):
        count += 1
print("Passaporti validi:", count)
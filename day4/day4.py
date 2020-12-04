import os
""" PARTE COMUNE  """
f = open((os.path.dirname(__file__) + '\day4_input'), 'r')
inputNum = []
temp = f.read()
temp = temp.split("\n\n")
"""
for i in temp:
    temp = temp.replace("\n", " ")
    """
print(temp)
f.close()
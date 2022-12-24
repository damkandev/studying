entrada = str(input("")).split()
pajaros = str(input("")).split()
canastas = str(input("")).split()

pArr = [];
cArr = [];
rArr = [];

for p in range(len(pajaros)):
    #Pajaro Rojo - 1 C
    if(int(pajaros[p]) == 1):
        pArr.append(1)
    #Pajaro Amarillo - 2 C
    elif(int(pajaros[p]) == 2):
        pArr.append(2)

for c in range(len(canastas)):
    if(int(canastas[c]) == 1):
        cArr.append(1)
    elif(int(canastas[c]) == 2):
        cArr.append(2)

if len(pArr) > len(cArr):
    for x in range(len(pArr)):
        try:
            r = pArr[x] + cArr[x]
        except:
            cArr.insert(x, 0)

if len(cArr) > len(pArr):
    for x in range(len(cArr)):
        try:
            r = cArr[x] + pArr[x]
        except:
            pArr.insert(x, 0)

for r in range(len(cArr)):
    rArr.append(pArr[r] - cArr[r])


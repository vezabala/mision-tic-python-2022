# 11.Del conjunto de datos [20, 21, 30, 40,41, 50, 51,201] mostrar en pantalla los que no terminan en uno.
l = [20, 21, 30, 40, 41, 50, 51, 201]
cantidadL = len(l)
l2 = []
l3 = []
lResult = []
posicion = 0
contador = 1
for i in range(1, 210, 10):
    l2.append(i)
for j in l:
    for j2 in l2:
        if j == j2:
            l3.append(j)
while contador <= cantidadL:
    if len(l3) == 0:
        for b in l:
            lResult.append(b)
            contador += 1
    for h in l3:
        for n in l:
            if h != n:
                lResult.append(n)
                l.pop(posicion)
                break
            else:
                l.pop(posicion)
                l3.pop(posicion)
                break
        break
    contador += 1
print(lResult)

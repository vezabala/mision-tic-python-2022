# 17.Construir un programa python que calcule la suma de todos los números comprendidos entre 1 y 1000.
resultado = 0
l= []
posicion = 1
for i in range(1, 1001):
    l.append(i)
for j in l:
    if j + l[posicion] == 3:
        resultado = j + l[posicion]
    elif j == l[posicion]:
        resultado = resultado
    else:
        resultado += j
print(f'La suma de los número comprendidos entre 1 y 1000 es = {resultado}')
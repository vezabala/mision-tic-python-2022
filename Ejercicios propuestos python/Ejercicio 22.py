# 22.Mostrar los números pares comprendidos entre 1 y 20, al final mostrar la suma de los números pares.
l = []
posicion = 1
resultado = 0
for i in range(1, 21):
    if i % 2 == 0:
        l.append(i)
for j in l:
    if j + l[posicion] == 6:
        resultado = j + l[posicion]
    elif j == l[posicion]:
        resultado = resultado
    else:
        resultado += j
print(f'{l} el resultado de su suma es {resultado}')

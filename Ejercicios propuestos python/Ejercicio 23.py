# 23.Leer una frase y determinar cuantas vocales tiene.
vocales = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
letrasFra = []
vocalesFra = []
print('Escribe una frase')
frase = input()
for i in frase:
    letrasFra.append(i)
for j in vocales:
    for k in letrasFra:
        if j == k:
            vocalesFra.append(k)
print(f'la frase "{frase}" tiene {len(vocalesFra)} vocales')


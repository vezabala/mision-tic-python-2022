# 18.Mostrar los mĂșltiplos de 5 comprendidos entre 13 y 48.
l= []
for i in range(13, 49):
    if i % 5 == 0:
        l.append(i)
print(f'los mĂșltiplos de 5 comprendidos entre 13 y 48 son {l}')

"""------------------Tuplas------------"""
#
'''tupla = (0, 1, 2, 'hola,True')
print(tupla[3])
print(tupla[-1])
print(tupla[-3])
print(tupla[1:3])  # 1,2
print(tupla[0:3])  # 0,1,2
print(tupla[:3])
print(tupla[3:])
print(tupla[:])
print(tupla[1:-1])'''
'''verduras = ('col', 'lechuga', 'repollo', 'brocoli')
print(len(verduras))
for i in verduras:
    print(i)
# verduras[0]='esparrago' las tupplas son inmutables no se puede
print(verduras)

listaVerduras = list(verduras)
print(listaVerduras)
listaVerduras[0] = 'esparrago'
print(listaVerduras)
verduras = tuple(listaVerduras)
print(verduras)'''
x = (10, 9, 6, 4, 3, 2, 6, 10, 21, 6)
print(x.count(10))
print(x.count(6))
print(x.count(100))

tupla = (13, 1, 8, 5, 2, 13, 21)
lista1 = []
lista2 = []
for i in tupla:
    if i < 5:
        lista1.append(i)
    else:
        lista2.append(i)
print(lista1)
print(lista2)

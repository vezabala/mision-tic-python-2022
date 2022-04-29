# Listas en Phyton

'''a = [3, 4, 45, 6, 45, 34, 8]
b = ['hola', 'mundo']
c = ['esneyder', 3.5, True]

print("la lista de numeros es: ", a)

# Lista dentro de otra
coordenadas = [[65, 132342], [-16.523453]]
print(coordenadas)

x = ['colombia', [30, 34, 123], ' putumayo', [1, 2, 3]]
print(type(x))'''

'''lista1 = list(range(10))
print(lista1)
a = [3, 4, 5, 6, 1, 2]
b = sorted(a)  # metodo sorted ordena la lista
print(b)'''

'''lista1 = list(range(4,15))
print(lista1)'''

'''lista1 = list(range(15,4,-1))
print(lista1)'''

'''lista1 = list(range(4, 15))
print(len(lista1))  # len es el tamaño de la lista'''

'''a = ['c', [1, 2], 'a']  # la lista interna lo toma como un solo objeto
print(len(a[1]))'''

'''notas = ['pepíto perez', [3.0, 5.0, 3.5, 4.0, 4.0], 'fulanito peres', [3.5, 4.5, 4.5, 3.0, 3.0]]
pPepito = (notas[1][0] + notas[1][1] + notas[1][2] + notas[1][3] + notas[1][4]) / 5
pFulanito = (notas[3][0] + notas[3][1] + notas[3][2] + notas[3][3] + notas[3][4]) / 5
print('tripulante\tpromedio')
print(notas[0], '\t', pPepito)
print(notas[2], '\t', pFulanito)'''

'''n = [67, 45, 3, 8, 99, 110, 1]
#    -7  -6  -5 -4 -3 -2   -1
print(n[-1])'''

'''n = [67, 45, 3, 8, 99, 110, 1]
print(n)
n[2] = 3.8
print(n)
n[2] = [3, 8, 0]
print(n)'''

'''---------------------Sublistas------------------------'''
# nombre[a:b]
'''n = [67, 45, 3, 8, 99, 110, 1]
subl1 = n[2:4]
print(subl1)'''

'''dias = ['lunes', 'martes', 'miercoles', 'jueves']
subl = dias[2:3]
print(subl)
subl = dias[:3]
print(subl)
subl = dias[1:]
print(subl)
subl = dias[:]
print(subl)'''

'''n = [67, 45, 3, 8, 99, 110, 1]
dias = ['lunes', 'martes', 'miercoles', 'jueves']
l = n + dias
print(l)'''

n = [67, 45, 3, 8, 99, 110, 1]
# l = n + 5 <---- ERROR
l = n + [5]  # Debe ser el mismo tipo de variable en este caso lista
print(l)

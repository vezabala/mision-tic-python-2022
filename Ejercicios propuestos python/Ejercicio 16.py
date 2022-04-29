# 16.Leer una cadena y determinar cuántas veces dicha cadena contiene la letra A mayúscula.
print('Escribe una palabra')
entrada = input()
cantidad = 0
for i in entrada:
    if i == 'A':
        cantidad += 1
print(f'La palabra {entrada} tiene {cantidad} A')

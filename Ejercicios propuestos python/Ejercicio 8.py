# 8.Construir un programa que lea un número entero y determine si el resultado es sumar sus dos últimos dígitos es un número de un dígito.
print('Escriba un numero \n')
entrada = input()
l = []
for i in entrada:
    l.append(i)
ultimoNum = int(l[len(l) - 1])
penultimoNum = int(l[len(l) - 2])
if -10 < ultimoNum + penultimoNum < 10:
    print(f'La suma de los ultimos 2 digitos su resultado es de un digito')
else:
    print(f'La suma de los ultimos 2 digitos su resultado no es de un digito')

#5.Construir un programa que lea un número entero y determine si la suma de sus dos últimos dígitos es un número par.
print('Escriba un numero \n')
entrada = input()
l = []
for i in entrada:
    l.append(i)
ultimoNum = int(l[len(l) - 1])
penultimoNum = int(l[len(l) - 2])
if ultimoNum + penultimoNum % 2 == 0:
    print(f'La suma de los ultimos 2 digitos el resultado es {ultimoNum + penultimoNum} y es un numero par')
else:
    print(f'La suma de los ultimos 2 digitos el resultado es {ultimoNum + penultimoNum} y es un numero inpar')

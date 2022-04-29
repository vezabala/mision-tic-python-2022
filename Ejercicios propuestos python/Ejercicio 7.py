# 7.Construir un programa que lea un número entero y determine si la suma de sus dos últimos dígitos es igual a siete.
print('Escriba un numero \n')
entrada = input()
l = []
for i in entrada:
    l.append(i)
ultimoNum = int(l[len(l) - 1])
penultimoNum = int(l[len(l) - 2])
if ultimoNum + penultimoNum == 7:
    print(f'La suma de los ultimos 2 digitos es igual a 7')
else:
    print(f'La suma de los ultimos 2 digitos es diferente a 7')
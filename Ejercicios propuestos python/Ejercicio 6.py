# 6.Construir un programa que lea un número entero y determine si sus dos últimos dígitos son iguales.
print('Escriba un numero \n')
entrada = input()
l = []
for i in entrada:
    l.append(i)
ultimoNum = int(l[len(l) - 1])
penultimoNum = int(l[len(l) - 2])
if ultimoNum == penultimoNum:
    print('los dos ultimos digitos son iguales')
else:
    print('Los dos ultimos digitos no son iguales')

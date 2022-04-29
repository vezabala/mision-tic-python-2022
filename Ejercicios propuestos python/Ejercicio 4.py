# 4.Construir un programa que lea un número entero y determine si su último dígito es un dígito par.
print('Escriba un numero \n')
entrada = input()
l = []
for i in entrada:
    l.append(i)
ultimoNum = int(l[len(l) - 1])
if ultimoNum % 2 == 0:
    print(f'El ultimo digito que es {ultimoNum} es un numero par')
else:
    print(f'El ultimo digito que es {ultimoNum} es un numero inpar')

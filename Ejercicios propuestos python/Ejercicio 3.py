# 3.Construir un programa que lea un número entero y determine si es un número impar.
print('Escriba un numero \n')
entrada= input()
numero = int(entrada)
if numero%2 != 0:
    print(f'el numero {numero} es un numero inpar')
else:
    print(f'el numero {numero} es un numero par')
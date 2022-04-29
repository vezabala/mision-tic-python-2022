# 2.Construir un programa que lea un número entero y determine si es un número par.
print('Escriba un numero \n')
entrada= input()
numero = int(entrada)
if numero%2 == 0:
    print(f'el numero {numero} es un numero par')

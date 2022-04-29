# 1.Construir un programa que lea un número entero y determine si es un número positivo de cuatro dígitos.
print('Escriba un numero \n')
entrada= input()
numero = int(entrada)
if numero > 0:
    print(f'el numero {numero} es un numero positivo')
else:
    print(f'el numero {numero} es un numero negativo')

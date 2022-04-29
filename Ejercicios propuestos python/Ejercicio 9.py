# 9.Construir un programa que lea dos números enteros y determine si el primer número es mayor que el segundo.
print('Escriba un numero \n')
entrada1= input()
print('Escriba otro numero \n')
entrada2= input()
numero1 = int(entrada1)
numero2 = int(entrada2)
if numero1 > numero2:
    print(f'El primer numero ({numero1}) es mayor que es segundo numero ({numero2})')
else:
    print(f'El primer numero ({numero1}) es menor que es segundo numero ({numero2})')

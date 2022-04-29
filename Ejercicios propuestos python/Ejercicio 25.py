# 25.Leer una palabra y determinar cuántas sílabas simples tienen.
print('Escribe una palabra')
palabra = input()
contador = 0
for i in palabra:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' \
            or i == 'U':
        contador += 1
print(f'El numero de silabas simples en la palabra son {contador}')

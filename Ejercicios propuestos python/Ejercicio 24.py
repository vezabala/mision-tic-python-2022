# 24.Leer una frase y determinar cuántas palabras tiene.
print('Escribe una frase')
frase = input()
l1 = []
for i in frase.split():
    l1.append(i)
print(f'la frase "{frase}" tiene {len(l1)} palabras')


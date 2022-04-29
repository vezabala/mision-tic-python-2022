# 21.Mostrar los enteros comprendidos entre 1 y 30 exceptuando los múltiplos de 3
l = []
for i in range(1, 31):
    if i % 3 != 0:
        l.append(i)
print(l)

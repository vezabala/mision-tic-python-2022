# 10.Construir un programa que lea dos números enteros y determinar si el último dígito del primer número es par y al
# tiempo si el penúltimo dígito del segundo número es impar.
print('Escriba un numero \n')
entrada1 = input()
print('Escriba otro numero \n')
entrada2 = input()
l1 = []
l2 = []
for i in entrada1:
    l1.append(i)
for j in entrada2:
    l2.append(j)
numeroUlt1 = int(l1[len(l1) - 1])
numeroPen2 = int(l2[len(l2) - 2])
if numeroUlt1 % 2 == 0 and numeroPen2 % 2 != 0:
    print(f'El ultimo digito del primer numero ({numeroUlt1}) es par y el penultimo digito del segundo numero ({numeroPen2}) es inpar')
elif numeroUlt1 % 2 == 0 and numeroPen2 % 2 == 0:
    print(f'El ultimo digito del primer numero ({numeroUlt1}) es par y el penultimo digito del segundo numero ({numeroPen2}) es par')
elif numeroUlt1 % 2 != 0 and numeroPen2 % 2 != 0:
    print(f'El ultimo digito del primer numero ({numeroUlt1}) es inpar y el penultimo digito del segundo numero ({numeroPen2}) es inpar')
else:
    print(f'El ultimo digito del primer numero ({numeroUlt1}) es inpar y el penultimo digito del segundo numero ({numeroPen2}) es par')



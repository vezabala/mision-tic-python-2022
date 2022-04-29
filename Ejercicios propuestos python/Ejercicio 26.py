# 26.Generar un programa que cuando detecte numeros hasta 2 cifras con el 7 o multiplo de 7
# escriba "pum", cuando tenga mas de 2 cifras escriba 'pum pum' si contiene el con el 7 o
# multiplo de 7.
print('Escribe un numero')
numero = input()
l = []
lTem = []
cantidad = 0
numInt: 0
msj = ''
cont = 1
for i in numero:
    l.append(i)
for j in l:
    if len(l) <= 2 and j == '7':
        msj = 'pum'
    elif len(l) == 2 and l[1] != '7':
        numInt = int(numero)
        if numInt % 7 == 0:
            msj = 'pum'
    elif len(l) > 2:
        for h in l:
            lTem.append(h)
        cantidad = len(lTem)
        while cont <= cantidad:
            for hj in lTem:
                if hj != '7':
                    lTem.pop(0)
                    break
                else:
                    msj = 'pum pum'
                    cont = cantidad + 1
                    break
            cont += 1
        if len(lTem) == 0:
            numInt = int(numero)
            if numInt % 7 == 0:
                msj = 'pum pum'
        break
print(msj)
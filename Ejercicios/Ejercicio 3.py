# Nombre ---- Edad -------- Hijos
# Omar         54           4
# Luis         35           1
l = ['Omar', 54, 4, 'Luis', 35, 1, 'Maira', 32 , 2]
i = 0
msj = ''
print('Nombre\tEdad\tHijos')
for x in l:
    if i % 3 == 2:
        msj = msj + f'{x}' + '\n'
        i = i + 1
    else:
        msj = msj + f'{x}  ' + '\t'
        i = i + 1
print(msj)

# 14.El conjunto de datos ['omar', 50, 4, 'luis', 40, 5, 'juan', 30, 1]
# mostrar en pantalla los datos organizados de
# tres columnas que tengan por título nombre edad hijos.
l = ['omar', 50, 4, 'luis', 40, 5, 'juan', 30, 1]
i = 1
msj = ''
print('Nombre\tEdad\tHijos')
for x in l:
    if i % 3 == 0:
        msj = msj + f'{x}' + '\n'
        i = i + 1
    else:
        msj = msj + f'{x}  ' + '\t'
        i = i + 1
print(msj)

# 20.Mostrar los nombres completos de los meses y al frente la cantidad de letras que tiene cada nombre.
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre',
         'Diciembre']
posicion = 0
mes = []
for i in meses:
    for j in i:
        mes.append(j)
    print(f'{meses[posicion]} tiene {len(mes)} letras')
    posicion += 1
    mes = []

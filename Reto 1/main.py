print('¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.')
nombre = input('Por favor ingrese su nombre: ').lower().capitalize()
materia = input('Ingrese el nombre de la material: ').capitalize()
nota = 0
porcentaje = 0
condicion = 0
notasList = []
condicion2 = 0
operacion = 0
acumulador = 0
cantidadList = 0
contador = 0
nota_acumulada = 0
acumulacionPorcent = 0
aprobacion = ''
notaAcumLis = []
notaAcumText = ''
while condicion == 0:
    notaIn = input('Ingrese la nota obtenida: ')
    porcentajeIn = input('Inglese el porcentaje de la nota: ')
    nota = float(notaIn)
    porcentaje = int(porcentajeIn)
    acumulacionPorcent += porcentaje
    if acumulacionPorcent <= 100:
        notasList.append(nota)
        notasList.append(porcentaje)
        if condicion2 != 0:
            condicion = 1
        elif acumulacionPorcent == 100:
            condicion = 1
        else:
            respuesta = input('Faltan añadir notas S/N ')
            if respuesta == 'N':
                condicion = 1
    else:
        print('El porcentaje evaluado de una materia no puede ser mayor a 100')
        acumulacionPorcent -= porcentaje
        condicion2 = 1
cantidadList = len(notasList)
while contador <= cantidadList:
    for i in range(0, len(notasList)):
        for j in range(1, len(notasList)):
            operacion = notasList[i] * notasList[j]
            acumulador += operacion
            notasList.pop(j)
            break
        notasList.pop(i)
        break
    contador += 1
nota_acumulada = acumulador / 100
if nota_acumulada >= 3:
    aprobacion = 'aprobado'
else:
    aprobacion = 'reprobado'
nota_acumulada = "{0:.3f}".format(nota_acumulada)
for notAcu in str(nota_acumulada):
    notaAcumLis.append(notAcu)
if int(notaAcumLis[4]) >= 0:
    notaAcumLis.pop(4)
    for nat in range(0, len(notaAcumLis)):
        notaAcumText = notaAcumText + f'{notaAcumLis[nat]}'
nota_acumulada = float(notaAcumText)
print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada} resultando en {aprobacion}')
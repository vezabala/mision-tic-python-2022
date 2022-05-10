# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN

# NO MODIFICAR LOS NOMBRES, PARÁMETROS DE ENTRADA NI RETORNOS DE LAS FUNCIONES
# USE LOS MISMOS NOMBRES DE LOS RETORNOS PARA NOMBRAR LOS RESULTADOS QUE SU FUNCIÓN DEBE GENERAR
def metodoPrin():
    nombres = ['Martín', 'Milú', 'Anastasia', 'Lupita', 'Tomasa', 'Pelusa', 'Genoveva', 'Motita']
    tipos = ['canino', 'canino', 'felino', 'felino', 'felino', 'canino', 'bovino', 'roedor']
    edades = [12, 9, 10, 8, 9, 2, 14, 1]
    pesos = [33, 26, 4, 5, 5, 6, 106.4, 0.34]
    veterinaria(nombres, tipos, edades, pesos)


def veterinaria(nombres, tipos, edades, pesos):
    contador = 1
    contador_equ_bov = 1
    edades_can_fel = []
    edades_equ_bov = []
    diccionario = {}
    diccionario2 = {}
    beneficiarios_can_fel = {}
    beneficiarios_equ_bov = {}
    promedio_can_fel = 0
    promedio_equ_bov = 0
    for n, t, e, p in zip(nombres, tipos, edades, pesos):
        diccionario[str(contador)] = [n, t, e, p]
        contador += 1
    contador = 1
    for n, t, e, p in zip(nombres, tipos, edades, pesos):
        diccionario2[str(contador)] = [n, t, e, p]
        contador += 1
    contador = 1
    for clave in diccionario2:
        for i in diccionario2[clave]:
            if i == 'canino' or i == 'felino':
                if diccionario2[clave][2] >= 9:
                    edades_can_fel.append(diccionario2[clave][2])
                    diccionario2[clave].pop(2)
                    beneficiarios_can_fel[str(contador)] = diccionario2[clave]
                    contador += 1
            if i == 'equino' or i == 'bovino':
                if diccionario2[clave][2] >= 16:
                    edades_equ_bov.append(diccionario2[clave][2])
                    diccionario2[clave].pop(2)
                    beneficiarios_equ_bov[str(contador_equ_bov)] = diccionario2[clave]
                    contador_equ_bov += 1
    for edad_can_fel in edades_can_fel:
        promedio_can_fel += edad_can_fel
    if promedio_can_fel > 0:
        promedio_can_fel = promedio_can_fel / len(edades_can_fel)
    else:
        promedio_can_fel = None
    for edad_equ_bov in edades_equ_bov:
        promedio_equ_bov += edad_equ_bov
    if promedio_equ_bov > 0:
        promedio_equ_bov = promedio_equ_bov / len(edades_equ_bov)
    else:
        promedio_equ_bov = None
    print('Diccionario: ', diccionario)
    print('benefi can fel: ', beneficiarios_can_fel)
    print('benefi equ bov: ', beneficiarios_equ_bov)
    print('promedio can fel: ', promedio_can_fel)
    print('promedio equ bov: ', promedio_equ_bov)
    return diccionario, beneficiarios_can_fel, beneficiarios_equ_bov, promedio_can_fel, promedio_equ_bov


metodoPrin()

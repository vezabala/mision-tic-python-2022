import csv, json
import pandas as pd


def crear_diccionario(fila):
    diccionario = {'Fecha': '', 'Comportamiento de la accion': '', 'Punto medio HIGH-LOW': 0}
    abrir = 0
    cerrar = 0
    high = 0
    low = 0
    for i in fila:
        if i == 'Date':
            diccionario['Fecha'] = fila[i]
        if i == 'Close':
            cerrar = float(fila[i])
        if i == 'Open':
            abrir = float(fila[i])
        if abrir != 0 and cerrar != 0:
            if cerrar - abrir > 0:
                diccionario['Comportamiento de la accion'] = 'SUBE'
            if cerrar - abrir < 0:
                diccionario['Comportamiento de la accion'] = 'BAJA'
            if cerrar - abrir == 0:
                diccionario['Comportamiento de la accion'] = 'ESTABLE'
        if i == 'High':
            high = float(fila[i])
        if i == 'Low':
            low = float(fila[i])
        if high != 0 and low != 0:
            diccionario['Punto medio HIGH-LOW'] = (high - low) / 2
    return diccionario


def crear_csv(lista_diccionarios):
    header_list = ['Fecha', 'Comportamiento de la accion', 'Punto medio HIGH-LOW']
    with open('analisis_archivo.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter='\t', fieldnames=header_list)
        writer.writeheader()
        for i in lista_diccionarios:
            writer.writerow(i)
    file_contenido = pd.read_csv('analisis_archivo.csv')
    return file_contenido


def leer_Globan_csv():
    lista_diccionarios = []
    with open('GLOBANT.csv') as globant:
        archivo = csv.DictReader(globant)
        for row in archivo:
            diccionario = crear_diccionario(row)
            lista_diccionarios.append(diccionario)
    crear_csv(lista_diccionarios)
    return lista_diccionarios


def datos_para_json():
    precios_bajos = []
    precios_altos = []
    lista_diccionarios_completos = []
    fecha_del_mas_bajo = ''
    fecha_del_mas_alto = ''
    lista_analisis = leer_Globan_csv()
    cantidad_sube = 0
    cantidad_baja = 0
    cantidad_estable = 0
    with open('GLOBANT.csv') as globant:
        archivo = csv.DictReader(globant)
        for row in archivo:
            for i in row:
                if i == 'Low':
                    precios_bajos.append(row[i])
                if i == 'High':
                    precios_altos.append(row[i])
                lista_diccionarios_completos.append(row)
    precios_bajos.sort()
    for diccionario in lista_diccionarios_completos:
        if diccionario['Low'] == precios_bajos[0]:
            fecha_del_mas_bajo = diccionario['Date']
    precios_altos.sort(reverse=True)
    for diccionario in lista_diccionarios_completos:
        if diccionario['High'] == precios_altos[0]:
            fecha_del_mas_alto = diccionario['Date']
    for lia in lista_analisis:
        if lia['Comportamiento de la accion'] == 'SUBE':
            cantidad_sube += 1
        if lia['Comportamiento de la accion'] == 'BAJA':
            cantidad_baja += 1
        if lia['Comportamiento de la accion'] == 'ESTABLE':
            cantidad_estable += 1
    crear_json(fecha_del_mas_bajo, precios_bajos[0], fecha_del_mas_alto, precios_altos[0], cantidad_sube, cantidad_baja,
               cantidad_estable)


def crear_json(fecha_bajo, precio_bajo, fecha_alto, precio_alto, cantidad_sube, cantidad_baja, cantidad_estable):
    data = {
        'date_lowest_price': fecha_bajo,
        'lowest_price': float(precio_bajo),
        'date_highest_price': fecha_alto,
        'highest_price': float(precio_alto),
        'cantidad_veces_sube': cantidad_sube,
        'cantidad_veces_baja': cantidad_baja,
        'cantidad_veces_estable': cantidad_estable
    }
    with open('detalles.json', 'w') as archivo:
        json.dump(data, archivo, indent=4)


def solucion():
    leer_Globan_csv()
    datos_para_json()


if __name__ == '__main__':
    solucion()

import numpy as np
import random


def encriptado(texto):
    cantidad_text = round(pow(len(texto), 0.5))
    while pow(cantidad_text, 2) < len(texto):
        cantidad_text += 1
    if len(texto) < pow(cantidad_text, 2):
        while len(texto) < pow(cantidad_text, 2):
            texto = texto + '_'
    lista_text = []
    lista_text_desor = []
    lista_codigo_uni = []
    clave = []
    for j in texto:
        lista_text.append(j)
    for i in range(0, len(lista_text)):
        clave.append(i)
    clave = random.sample(clave, len(clave))
    for j in clave:
        lista_text_desor.append(lista_text[j])
    for i in lista_text_desor:
        lista_codigo_uni.append(ord(i))
    array_final = np.zeros((cantidad_text, cantidad_text))
    for columna in range(len(array_final[0])):
        for fila in range(len(array_final)):
            for i in lista_codigo_uni:
                array_final[columna, fila] = i
                lista_codigo_uni.pop(0)
                break
    print(array_final, '\n\n', clave, '\n')
    print(desencriptado(array_final, clave))
    return array_final, clave


def desencriptado(array_encriptado, clave):
    array_int = np.asarray(array_encriptado, dtype=int)
    lista_arraen = []
    lista_desimpcriptado = []
    lista_array_or = []
    texto = ''
    for columna in range(len(array_int[0])):
        for fila in range(len(array_int)):
            lista_arraen.append(array_int[columna, fila])
    for i in lista_arraen:
        lista_desimpcriptado.append(chr(i))
    lista_numeros = []
    for num in range(0, 1000):
        lista_numeros.append(num)
    for nm in lista_numeros:
        for cl, li in zip(clave, lista_desimpcriptado):
            if nm == cl:
                lista_array_or.append(li)
    for li in lista_array_or:
        if li != '_':
            texto = texto + li
    return texto


if __name__ == '__main__':
    encriptado('Today is Caturday!')

# Diccionarios
#         valor   clave
"""
datos = {'jose': 34, 'manuel': 56}
print(datos)
"""
'''datos = {10: 'messi', 23: 'arquero', 4: 'adriana'}
print(datos[23])'''

'''colores = {'blanco': 'white', 'rosa': 'pink'}
print(colores['rosa'])
colores['rojo'] = 'red'
print(colores)
colores['rojo'] = 123
print(colores)
b = {'aleja': {22, 1, 80}}
b = {'aleja': {'edad':22,'altura':1.80}}
print(b)'''
'''colores = {'blanco': 'white', 'rosa': 'pink'}
colores.update({'blanco': 'red', 'white': 'luna'})  # update actualiza diccionario
print(colores)
print(colores.get('azul', 'no existe ese color'))  # .get obtener
print('rosa' in colores)
print(colores.values())  # salta llaves muestra valores
print(colores.keys())  # muestra llaves
print(colores.items())
x = colores.pop('white')
colores['moon'] = x
print(colores)'''

'''contacto = {'nombre': 'jhon', 'edad': 30, 'rango': 'jefe area'}
print(len(contacto))
print(len(contacto.keys()))
print(contacto.values())'''
# pprint organiza la info en json

'''import pprint, json

contacto = {'nombre': 'juan',
            'edad': 30,
            'rango': 'jefe area',
            'direccion': {
                'calle:': 'NQS',
                'CIUDAD': 'MADRID',
                'pais': 'india'
            }
            }
print(len(contacto))
# print(len(contacto['direccion']))
# contacto.clear()
pprint.pprint(contacto)
print(json.dumps(contacto, sort_keys=False, indent=4))  # dumps organiza los datos {diccionario. la forma , identacion(separacion)'''

'''moneda = {'Euro': 't', 'Dolar': 'US$', 'Yen': 'Y'}
x= input('Ingrese una divisa ya sea Euro, dolar o Yen').capitalize() # convierte la primera letra en mayus

if x=='Euro':
    print(moneda[x])
elif x== 'Dolar':
    print(moneda[x])
elif x=='Yen':
    print(moneda[x])
else:
    print('esa moneda no esta la lista')'''

agenda = {'nombre': '', 'edad': '', 'direccion': '', 'telefono': ''}
agenda['nombre'] = input('Ingrese nombre')
agenda['edad'] = input('Ingrese edad')
agenda['direccion'] = input('Ingrese direccion')
agenda['telefono'] = input('Ingrese telefono')
print('hola soy ', agenda['nombre'], 'tengo ', agenda['edad'], 'años mi telefono es ', agenda['telefono'])

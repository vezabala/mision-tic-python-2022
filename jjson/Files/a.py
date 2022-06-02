from csv import writer, reader, DictWriter,DictReader
from email import header

with open('TA_PRECO_MEDICAMENTO.csv') as f:
    r= reader(f)
    d=list(r)
    for i in d:
        print(i)
'''with open('users.csv') as f:
    r= reader(f)
    d=list(r)
    for i in d:
        print(i)


with open('users.csv','a') as f:
    csv_w=DictWriter(
        f,
        fieldnames=('username','firstname','lastname','password'),
        lineterminator='\n'
        )
    d=[
    {'username':'xxxx','firstname':'ana maria','lastname':'xyz','password':'xxxxx'},
    {'username':'xxx','firstname':'jaime','lastname':'barajas','password':'xxxx'}
    ]
    csv_w.writerows(d)
    
with open('users.csv','a') as f:
    header=('Nombre','Apellido','Edad')
    c=DictWriter(
        f,
        fieldnames=header,
        lineterminator='\n'
    )
    d=[
    {'Nombre':'ana maria','Apellido':'xyz','Edad':34},
    {'Nombre':'maria','Apellido':'zxy','Edad':34},
    {'Nombre':'ana','Apellido':'algo','Edad':34},
    {'Nombre':'mary','Apellido':'otro','Edad':34},
    {'Nombre':'anita','Apellido':'z','Edad':34}
    ]
    c.writeheader()
    c.writerows(d)

with open('users.csv') as f:
    c=DictReader(f)
    d=list(c)
    for i in d:
        print(i)
#hacer un cambio en un registro
from tempfile import NamedTemporaryFile #temporales
import shutil #archivos a alto nivel

with open('users.csv') as f:#abrimos el archivo
    c=DictReader(f)#lo leemos
    d=list(c)#convertimos en lista
with NamedTemporaryFile(mode='w',delete=False) as fl:#temporalidad en modo escritura 'w', eliminacion no
    header=('Nombre','Apellido','Edad')#el emcabexzado
    c=DictWriter(#lectura como diccionario
        fl,
        fieldnames=header,
        lineterminator='\n'
        
    )
    c.writeheader()#escribir el encabezado
    for i in d:#recorrido de los datos optenidos como lista en d=list(c)
        if i['Nombre']=='anita':
            i={'Nombre':'anita','Apellido':'xxxxxxxxx','Edad':34}
        c.writerow(i)#escritura del dato a actualizar
    
    print(fl.name)#impresion de donde esta el archivo temporal
shutil.move(fl.name,'users.csv')#escrotura del emporal en el archivo pricipal


import os

os.remove('users.csv')'''

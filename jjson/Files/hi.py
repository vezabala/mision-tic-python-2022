import csv
from termios import TIOCGICOUNT
'''
with open('persona.csv') as f:
    r=csv.DictReader(f)
    for i in r:
        print(i)

cabecera=['nombre','telefono']
fila=[
    ['jairo',123],
    ['jairo',124],
    ['jairo',125]
]

with open('persona.csv','w',newline='') as f:
    c=csv.writer(f)
    c.writerow(cabecera)
    c.writerows(fila)'''
    

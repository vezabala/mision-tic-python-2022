import csv

'''heade = ['nombre', 'edad']
fila = [['dario', 34], ['daniela', 23], ['marcela', 19]]
with open('personas.csv', 'w') as f:
    c = csv.writer(f)
    c.writerow(heade)
    c.writerow(fila)

with open('personas.csv') as csvF:
    r = csv.reader(csvF)
    for i in r:
        print(i)

with open('personas.csv') as f:
    r = csv.DictReader(f)  # leer como si fuera un diccionario
    for i in r:
        print(i) '''
import pandas as pd

'''nombre = ['a', 'b']
materia = ['M', 'F']
nota = [4, 5]
d = {'n': nombre, 'm': materia, 'no': nota}
dt = pd.DataFrame(d)
dt.to_csv('personas.csv')


f = pd.read_csv('personas.csv')
lista = f.values.tolist()
print(lista)
df = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], index=['a', 'b', 'c'], columns=['a', 'b', 'c', 'd']

                  )

df.to_excel('pandas.xlsx')

df = pd.read_excel('pandas.xlsx')
print(df)'''
import requests

url = 'https://jsonplaceholder.typicode.com/todos'
r = requests.get(url)
print(r)
df = pd.read_json(url)
print(df)

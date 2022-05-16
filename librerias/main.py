import numpy as np

'''matriz = np.arange(6).reshape(3, 2, -1)
print(matriz)'''
'''a = np.array([[1, 2], [3, 4]])
b = np.array([[10, 12], [30, 40]])
c = a + b
d = np.add(a, b)
resta = np.subtract(a, b)
multi = np.multiply(a, b)
divi = np.divide(a, b)
print(c)
print(d)
print(resta)
print(multi)
print(divi)'''
'''x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
r = np.dot(x, y)  # 1*4 + 2*5 + 3*6
print(r)'''
'''x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[4, 5], [6, 7], [8, 9]])
r = np.dot(x, y)  
print(r)'''
# es una multiplicacion de matrices

'''a = np.array([1, 2, 3, 4, 5])
b = np.array([(1, 2), (3, 4)])
c = np.zeros((3, 4))
d = np.arange(10)
e = np.arange(1, 10, 2)
f = np.ones((2, 3))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(len(a))
print(f.ndim)
print(b.shape)'''
'''x = np.array([1, 4, 5, 3, 4, 9, 1, 0])
print(x)
print(np.sort(x))
y = np.array([[-2, 1, 0, -3], [5, 7, 0, 0]])
print(y)
print(np.sort(y, None))'''  # convierte la matriz en un array y lo ordena
'''y = np.array([[2, 1, 0, -3], [-5, 7, 0, 0]])
print(np.sort(y))
print(np.sort(y, axis=0))  # cada columna la ordena
print(np.sort(y, axis=1))'''  # cada fila la ordena
'''b = np.array([[3, 2, -4], [4, -1, -1]])
print(-b)
b.sort(1)
print(b)'''

# ufunc funciones universales
'''a = np.array([1, 2, 3])
b = np.array([2, 3, 2])
print(np.multiply(a, b))'''

# casting
'''a = np.arange(6).reshape(2, -1)
b = np.array([2, 3, 2])
print(a)
c = np.add(a, b)
print(c)
d = np.multiply(a, b)
print(d)
e = np.power(a, b)  # lo eleva segun b
print(e)
f = np.rint(b)  # round(a,2) quita los decimales y aproxima
print(f)'''

"""z = np.array([3, 4, -3, 5, -7])
print(np.sign(z))  # positivo lo convierte en 1 y negativo a -1
"""
'''z = np.array([-1, 0, 1, 2, -3])
print(np.exp(z))'''
'''z = np.array([1, 1, 2, 3])
print(np.log(z))'''

"""z = np.array([12, 8, 64])
print(np.sqrt(z))  # raiz cuadrada
"""

''''z = np.array([12, 8, 64])
print(np.square(z))  # lo eleva al cuadrado'''
'''z = np.array([12, 8, 64])
print(np.power(z, 3))  # lo eleva a mas de una potencia'''

'''z = np.array([12, 8, 64])
c = np.array([2, 2, 4])
print(np.gcd(z, c))  # maximo como un divisor
print(np.lcm(z, c))  # minimo como un divisor'''

'''# Funciones trigonometricas
c = np.array([1.07, -0.35, 0.67, 1.67])
d = np.array([-1, 0, 0.5])
print(np.sin(c))  # saca el seno
print(np.cos(c))  # saca el coseno
print(np.tan(c))  # saca el tangente
print(np.arcsin(d))  # saca coseno
print(np.arccos(d))
print(np.arctan(d))'''

# funciones de conjunto
'''a = np.random.randint(0, 10, size=(4, 4))
print(a)
print(np.unique(a))  # extrae los datos unicos'''

'''a = np.random.randint(0, 10, size=(4, 4))
b = np.random.randint(0, 10, size=(4, 4))
print(a)
print(b)
print(np.union1d(a, b))  # devuelve un array con los elementos resultandes de unir las matrices
print(np.intersect1d(a, b))
print(np.setdiff1d(a, b))'''

# algebra lineal
'''b = np.random.randint(0, 10, size=(4, 4))
print(np.linalg.qr(b))  # factoriza la matriz'''

'''b = np.random.randint(0, 10, size=(4, 4))
print(np.linalg.inv(b))  # inversa de b'''

x = np.array([1, 3, 5])
y = np.array([2, 4, 6])
z = [True, False, False]
print(np.where(z, y, x))

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

a = np.array([1, 2, 3, 4, 5])
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
print(b.shape)
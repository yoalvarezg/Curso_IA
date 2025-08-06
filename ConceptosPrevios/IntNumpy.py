import numpy as np
import matplotlib.pyplot as plt

# Matriz de 2X4 de ceros
a=np.zeros((2,4))
print(a)

# Matriz de 2X4 de unos
b=np.ones((2,4))
print(b)

# Imprimir las dimensiones de las matrices
print("Dimensiones de a:",a.shape)
print("Dimensiones de b:",b.shape)
# Imprimir numero de dimensiones de las matrices
print("Numero de dimensiones de a:",a.ndim)
print("Numero de dimensiones de b:",b.ndim)
# Imprimir el tamaño de las matrices
print("Tamaño de a:",a.size)
print("Tamaño de b:",b.size)

"""
Array o matriz cuyos valores son todos el valor 
indicado como segundo parametros de la funcion
"""
c=np.full((2,3,4),8)
print(c)

"""
Inicializa los valores del Array con lo que 
tenga en memoria en el momento
El llenado del empty es aleatorio
"""
d=np.empty((2,3,9))
#print(d)

# Inicializacion del array usando uno de python 
d=np.array([[1,2,3],[4,5,6]])
print(d)

"""
Creacion del array utilizando una funcion basada 
en rangos (minimo,maximo,numero de elementos del array)
"""
print(np.linspace(0,6,10))

# Inicializacion del Array con valores aleatorios
e=np.random.rand(2,3,4)
print(e)

"""
Inicializacion del Array con valores aleatorios 
conforme a una distribucion normal
"""
f=np.random.rand(2,4)
print(f)

"""
Histograma de valores aleatorios
"""
g=np.random.rand(100)

plt.hist(g,bins=100)
#plt.show()

"""
Histograma con valores personalizados
"""
h=np.array([1,2,3,2,2,2,4,5,6,7,8])
plt.hist(h,bins=20)
#plt.show()

#Inicializacion de un Array/Matriz usando una funcion
def func(x,y):
    return x+2*y
i=np.fromfunction(func,(3,5))
print(i)

# Acceso a los elementos de un Array
# Array unidimensional
array_uni = np.array([1,3,5,7,9,11,13])
print("Shape:",array_uni.shape)
print("array_uni:",array_uni)
# Accediendo al 5to elemento del Array
print(array_uni[4])
# Accediendo a los elementos de 2 en 2
print(array_uni[0::2])

# Array multidimensional
array_multi = np.array([[1,2,3,4],[5,6,7,8]])
print("Shape:",array_multi.shape)
print("array_multi:",array_multi)
# Accediendo al 4to elemento del Array multidimensional
print(array_multi[0,3])
# Accediendo a los datos de la 2da fila
print(array_multi[1,:])

# Accediendo al tercer elemento de las dos filas
print((array_multi[0:2,2]))
# Modificacion de un Array/Matriz
"""
Crear un Array unidimensional inicializando un 
rango de elementosdel 0 al 27
"""
array1=np.arange(24)
print("Shape:",array1.shape)
print("Array 1:",array1)
# Cambiar las dimensiones del Array y sus longitudes
array2=np.arange(25)
array2=array1.reshape=(6,4)
print("Shape:",array2.shape)
print("Array 2:",array2)
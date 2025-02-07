# Función que recibe una lista y devuelve otra eliminando sus duplicados (función y pruebas)
# def eliminarDuplicados(lista):
#     auxLista = lista.copy()
#     for i in range(len(lista)):
#         if lista.count(lista[i]) > 1:
#             for j in range((len(auxLista) - 1), 0, -1):
#                 if auxLista.count(lista[i]) <= 1:
#                     break
#                 if auxLista[j] == lista[i]:
#                     auxLista.pop(j)
#     return auxLista

# def eliminarDuplicados(lista):
#     auxLista = []
#     for elemento in lista:
#         if elemento not in auxLista:
#             auxLista.append(elemento)
#     return auxLista

# def eliminarDuplicados(lista):
#     return set(lista)


# print(eliminarDuplicados([1,2,3,4,5,2,3,4,5,3,4,5,4,5,5]))
# print(eliminarDuplicados(['gato', 'pez', 'perro', 'pez', 'perro', 'gallina', 'perro']))


# Función que recibe una matriz (una lista de listas) y devuelve otra eliminando sus duplicados
# Sin elementos repetidos en las filas
# def eliminarDuplicadosMatriz1(matriz):
#     aux = []
#     for fila in matriz:
#         aux.append(set(fila))
#     return aux

# Sin elementos repetidos en toda la matriz
# def eliminarDuplicadosMatriz2(matriz):
#     aux = []
#     for fila in matriz:
#         for elemento in fila:
#             if elemento not in aux:
#                 aux.append(elemento)
#     return aux

# #Esto no funciona
# def eliminarDuplicadosMatriz3(matriz):
#     aux = []
#     return [aux.append(elemento) for fila in matriz for elemento in fila if elemento not in aux]

# print(eliminarDuplicadosMatriz1([[1,2,3],[4,5,2],[3,4,5],[3,4,5],[4,5,5]]))
# print(eliminarDuplicadosMatriz1([['gato', 'pez', 'perro'], ['pez', 'perro', 'gallina'], ['perro', 'gaviota', 'gato']])) 

# print(eliminarDuplicadosMatriz2([[1,2,3],[4,5,2],[3,4,5],[3,4,5],[4,5,5]]))
# print(eliminarDuplicadosMatriz2([['gato', 'pez', 'perro'], ['pez', 'perro', 'gallina'], ['perro', 'gaviota', 'gato']])) 

# print(eliminarDuplicadosMatriz3([[1,2,3],[4,5,2],[3,4,5],[3,4,5],[4,5,5]]))
# print(eliminarDuplicadosMatriz3([['gato', 'pez', 'perro'], ['pez', 'perro', 'gallina'], ['perro', 'gaviota', 'gato']])) 


# Función que recibe una lista y devuelve un diccionario con el número de veces que aparece cada elemento 
# (las claves del diccionario deben ser los elementos de la lista y los valores deben ser el número de veces que aparece 
# dicho elemento en la lista)

# def contarElementos(lista):
#     diccionario = {}
#     for elemento in lista:
#         if elemento not in diccionario:
#             diccionario.update({elemento:lista.count(elemento)})
#     return diccionario

# print(contarElementos([1,2,3,4,5,2,3,4,5,3,4,5,4,5,5]))
# print(contarElementos(['gato', 'pez', 'perro', 'pez', 'perro', 'gallina', 'perro']))


# Función que recibe dos matrices cuadradas (NxN) y devuelve una tercera matriz que contiene el valor 1 en las posiciones en que el valor de A y B coinciden y 0 en caso contrario.
# def valores_iguales_matriz(matriz1, matriz2):
#     matriz = [[0 for j in range(len(matriz1))] for i in range(len(matriz1))]
#     for i in range (len(matriz1)):
#         for j in range (len(matriz1[i])):
#             if matriz1[i][j] == matriz2[i][j]:
#                 matriz[i][j] = 1
#             else:
#                 matriz[i][j] = 0
#     return matriz

# # Tests
# matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3
# matriz2 = [[1, 5, 6], [7, 5, 9], [1, 2, 9]] # Matriz 3x3
# print(valores_iguales_matriz(matriz1, matriz2)) # Debería mostrar una matriz identidad
# assert valores_iguales_matriz(matriz1, matriz2) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


# def hallarPSilla(matriz):
#     puntosSilla = []
#     traspuesta =  [[None] * len(matriz) for i in range(len(matriz[0]))]
#     for fila in range(len(matriz)):
#         for columna in  range(len(matriz[fila])):
#             traspuesta[columna][fila] = matriz[fila][columna]
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             if (matriz[i][j] == min(matriz[i]) and matriz[i][j] == max(traspuesta[j])) or (matriz[i][j] == max(matriz[i]) and matriz[i][j] == min(traspuesta[j])):
#                 puntosSilla.append((i, j))

#     return puntosSilla

# print(hallarPSilla([[1,2,3],
#                     [4,5,2],
#                     [3,4,5],
#                     [3,4,5],
#                     [4,5,5]]))
# print(hallarPSilla([[1,4,3,3,4],
#                     [2,5,4,4,5],
#                     [3,2,5,5,5]]))



# # La mas sencilla e intuitiva
# matriz = []
# numero_filas = 4
# numero_columnas = 5
# for i in range(numero_filas):
#     matriz.append([])
#     for j in range(numero_columnas):
#         matriz[i].append(None)

# print(matriz)

# # Menos intuitiva pero mas eficiente
# matriz = [None] * numero_filas
# for i in range(numero_filas):
#     matriz[i] = [None] * numero_columnas
# print(matriz)

# # Versión mas compacta
# matriz = [range(numero_columnas) for i in range(numero_filas)]
# print(matriz)

# # Variación de la anterior
# matriz = [[None] * numero_columnas for i in range(numero_filas)]
# print(matriz)      


# import numpy as np

# def contarElementos(lista):
#     diccionario = {}
#     aux = np.array(lista)
#     elemento, indice, veces = np.unique(aux, return_index=True, return_counts=True)
#     print(elemento)
#     for indice in range(len(elemento)):
        
#         if elemento[indice] not in diccionario:
#             diccionario.update({elemento[indice]:veces[indice]})
#     return diccionario

# print(contarElementos([1,2,3,4,5,2,3,4,5,3,4,5,4,5,5]))
# print(contarElementos(['gato', 'pez', 'perro', 'pez', 'perro', 'gallina', 'perro']))


# import numpy as np

# def valores_iguales_matriz(matriz1, matriz2):
#     aux = np.zeros((len(matriz1), len(matriz1)))
#     aux = np.where(np.array(matriz1) == np.array(matriz2), 1, aux)
#     return aux

# # Tests
# matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3
# matriz2 = [[1, 5, 6], [7, 5, 9], [1, 2, 9]] # Matriz 3x3
# print(valores_iguales_matriz(matriz1, matriz2))


import numpy as np

# def hallarPSilla(matriz):
#     puntosSilla = []
#     aux = np.array(matriz)
#     for fila in range(aux.shape[0]):
#         for columna in range(aux.shape[1]):
#             if (aux[fila,columna] == np.min(aux[fila,:]) and aux[fila,columna] == np.max(aux[:,columna])) or (
#                 aux[fila,columna] == np.max(aux[fila,:]) and aux[fila,columna] == np.min(aux[:,columna])):
#                 puntosSilla.append((fila,columna))
#     return puntosSilla

# print(hallarPSilla([[1,2,3],
#                     [4,5,2],
#                     [3,4,5],
#                     [3,4,5],
#                     [4,5,5]]))
# print(hallarPSilla([[1,4,3,3,4],
#                     [2,5,4,4,5],
#                     [3,2,5,5,5]]))
# print(hallarPSilla([[1,2,6],
#                     [4,5,5],
#                     [3,4,5],
#                     [3,4,5],
#                     [4,5,5]]))
# print(hallarPSilla([[1,4,3,3,4],
#                     [2,5,4,4,5],
#                     [6,5,5,5,5]]))
import pandas as pd

# Crear un DataFrame a partir de un diccionario
# data = {
#     'Nombre': ['Ana', 'Juan', 'Carlos', 'Marta'],
#     'Edad': [34, 27, 45, 19]
# }

# df = pd.DataFrame(data)

# print(data)
# print(df)

myarray = np.array([[10,30,20], [50,40,60],[1000,2000,3000]])
rownames = ['lentejas', 'espinacas', 'cerveza']
colnames = ['enero', 'febrero', 'marzo']
mydf = pd.DataFrame(myarray, index=rownames, columns=colnames)
print("Compras:")
print(mydf)
print(mydf.T)

print("Compras de enero:")
print(mydf['enero'])
print("mydf['enero']['lentejas']")
print(mydf['enero']['lentejas'])
print("mydf.loc['lentejas', 'enero']")
print(mydf.loc['lentejas', 'enero'])
print("mydf.loc['lentejas']")
print(mydf.loc['lentejas'])
print("mydf.loc['lentejas'].sum()")
print(mydf.loc['lentejas'].sum())


#NO SE PUEDE
# print("mydf['lentejas']")
# print(mydf['lentejas'])
# print("mydf['lentejas'].sum()")
# print(mydf['lentejas'].sum())


mydf.plot()


from matplotlib import pyplot as plt
years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]

plt.plot(years,gdp,color='green',marker='o',linestyle='solid')
plt.title("Nominal GDP")

plt.ylabel("Billions of $")

plt.plot(years,gdp,color='green',marker='o',linestyle='solid')
plt.title("Nominal GDP")

plt.ylabel("Billions of $")

plt.style.use('ggplot')

plt.plot(years,gdp,color='red',marker='^', markersize=12,linestyle='dashed')
plt.title("Nominal GDP")

plt.ylabel("Billions of $")
plt.show()

plt.style.available
plt.style.use('default')

plt.plot(years,gdp,'bo',linestyle='solid')
plt.title("Nominal GDP")

plt.ylabel("Billions of $")
plt.show()

#solo jupiter
#%matplotlib inline

plt.plot(years,gdp,'bo',linestyle='solid')
plt.title("Nominal GDP")

plt.ylabel("Billions of $")

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]

xs = [i for i, _ in enumerate(variance)]

# We can make multiple calls to plt.plot
# to show multiple series on the same chart

plt.plot(xs, variance, 'g-', label='variance') # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2') # red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line

# Because we've assigned labels to each series,
# we can get a legend for free (loc=9 means "top center")

plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# Pasa valores para x generados por range y calcula los de y con la expresión cuadrática
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=10)

ax.set_title("Square Numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14)

# Fijamos el rango de los ejes
ax.axis([0, 1100, 0, 1100000]) 

plt.show()

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# Pasamos los valores de y a c
# Con cmap, indicamos que queremos un "colormap" e indicamos el patrón Blues

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14)

ax.axis([0, 1100, 0, 1100000]) 

plt.show()
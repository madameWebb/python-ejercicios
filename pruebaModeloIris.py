# # Importamos las bibliotecas necesarias
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score

# # Cargamos el conjunto de datos
# iris = load_iris()

# # Creamos las etiquetas de clase para la clasificación binaria
# # Si iris.target == 2 (Iris-Virginica), la etiqueta de clase es 1, y 0 en caso contrario
# y = (iris.target == 2).astype(int)

# # Seleccionamos la longitud del pétalo (columna 2 de iris.data) como nuestra característica
# X = iris.data[:, 2].reshape(-1, 1)

# # Dividimos los datos en conjuntos de entrenamiento y prueba
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Creamos el modelo de Regresión Logística
# model = LogisticRegression()

# # Entrenamos el modelo
# model.fit(X_train, y_train)

# # Hacemos predicciones con el conjunto de prueba
# predictions = model.predict(X_test)

# # Calculamos la precisión del modelo
# accuracy = accuracy_score(y_test, predictions)

# print(f'La precisión del modelo de Regresión Logística es: {accuracy}')


# Importamos las bibliotecas necesarias
# import numpy as np #
# import matplotlib.pyplot as plt #
# from sklearn.datasets import load_iris #
# from sklearn.model_selection import train_test_split #
# from sklearn.linear_model import LogisticRegression #

# # Cargamos el conjunto de datos
# iris = load_iris() #

# # Creamos las etiquetas de clase para la clasificación binaria
# y = (iris.target == 2).astype(int)

# # Seleccionamos la longitud del pétalo (columna 2 de iris.data) como nuestra característica
# X = iris.data[:, 2].reshape(-1, 1)

# # Dividimos los datos en conjuntos de entrenamiento y prueba
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Creamos el modelo de Regresión Logística
# model = LogisticRegression()

# # Entrenamos el modelo
# model.fit(X_train, y_train)

# # Creamos un array con valores equiespaciados entre el mínimo y el máximo de X_train
# X_values = np.linspace(X_train.min(), X_train.max(), 100).reshape(-1, 1)

# # Predecimos las probabilidades para X_values
# y_probs = model.predict_proba(X_values)

# # Dibujamos los datos de entrenamiento
# plt.scatter(X_train, y_train, color='blue', label='Datos de entrenamiento')

# # Dibujamos la línea de decisión del modelo
# plt.plot(X_values, y_probs[:, 1], color='red', label='Línea de decisión')

# # Añadimos la leyenda y los nombres de los ejes
# plt.legend()
# plt.xlabel('Longitud del pétalo')
# plt.ylabel('Clase (1 = Iris-Virginica, 0 = No Iris-Virginica)')

# # Mostramos el gráfico
# plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

from sklearn.datasets import load_iris
iris = load_iris()


# El conjunto de datos ya se cargó previamente (iris = load_iris())
#Se convierte a dataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# print(df.columns)
df['esVirginica'] = (iris.target == 2).astype(int) 
# print(X)
# Se crea el modelo
modeloViginica = LogisticRegression().fit(df[["petal length (cm)"]], df['esVirginica']) #Se entrena el modelo con los datos que ya tenemos
# #modeloViginica = LogisticRegression().fit(df[X], df['esVirginica']) #Se entrena el modelo con los datos que ya tenemos

df.plot(kind='scatter', # Create a scatter plot
        x='petal length (cm)',       # with 'exam1' on the x-axis
        xlabel='Longitud pétalo',
        y='esVirginica',    # and 'admitted' on the y-axis
        ylabel='Viginica',
        figsize=(8, 4),  # Reduce the vertical size since there are only two values on the y-axis
        title='Es de la clase Virginica en función de la longitud del pétalo', 
        label="Virginica")
x_sigmoide = np.linspace(0, 8, 1000) # Array de 1000 valores entre 30 y 100 (límites de x que estamos usando)
df_sigmoide = pd.DataFrame({'petal length (cm)': x_sigmoide}) # Creamos un nuevo DataFrame esas hipotéticas notas
y_sigmoide = modeloViginica.predict_proba(df_sigmoide[['petal length (cm)']]) # Calculamos los valores de y para esas notas
plt.plot(x_sigmoide, y_sigmoide[:, 1], 'r-', label='Probabilidad de ser Virginica')
new_grades = pd.DataFrame({'petal length (cm)': [5]}) # Creamos un nuevo DataFrame con dos notas
plt.scatter(new_grades, modeloViginica.predict(new_grades), color='orange', marker='X', s=200)
plt.legend()
plt.show()
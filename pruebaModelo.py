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
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Cargamos el conjunto de datos
iris = load_iris()

# Creamos las etiquetas de clase para la clasificación binaria
y = (iris.target == 2).astype(int)

# Seleccionamos la longitud del pétalo (columna 2 de iris.data) como nuestra característica
X = iris.data[:, 2].reshape(-1, 1)

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos el modelo de Regresión Logística
model = LogisticRegression()

# Entrenamos el modelo
model.fit(X_train, y_train)

# Creamos un array con valores equiespaciados entre el mínimo y el máximo de X_train
X_values = np.linspace(X_train.min(), X_train.max(), 100).reshape(-1, 1)

# Predecimos las probabilidades para X_values
y_probs = model.predict_proba(X_values)

# Dibujamos los datos de entrenamiento
plt.scatter(X_train, y_train, color='blue', label='Datos de entrenamiento')

# Dibujamos la línea de decisión del modelo
plt.plot(X_values, y_probs[:, 1], color='red', label='Línea de decisión')

# Añadimos la leyenda y los nombres de los ejes
plt.legend()
plt.xlabel('Longitud del pétalo')
plt.ylabel('Clase (1 = Iris-Virginica, 0 = No Iris-Virginica)')

# Mostramos el gráfico
plt.show()
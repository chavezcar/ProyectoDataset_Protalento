from datasets import load_dataset
import numpy as np
import pandas as pd

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

#'data' es el objeto Dataset y 'age' es la característica de las edades
edades = np.array(data["age"])

# Calcular el promedio de edad
promedio_edad = np.mean(edades)

print("\nEl promedio de edad de las personas participantes en el estudio es:", promedio_edad)

# Convertir el Dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Separar el DataFrame en dos según el valor de 'is_dead'
df_fallecidos = df[df['is_dead'] == 1]
df_sobrevivientes = df[df['is_dead'] == 0]

# Calcular los promedios de las edades de cada dataset
promedio_edad_fallecidos = df_fallecidos['age'].mean()
promedio_edad_sobrevivientes = df_sobrevivientes['age'].mean()

# Imprimir los promedios de edad
print("\nPromedio de edad de fallecidos:", promedio_edad_fallecidos)
print("Promedio de edad de sobrevivientes:", promedio_edad_sobrevivientes)

# Verificar los tipos de datos en cada columna
tipos_de_datos = df.dtypes
print("\nTipos de datos en cada columna:")
print(tipos_de_datos)

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras
cantidad_hombres_fumadores = df[(df['is_male'] == 1) & (df['is_smoker'] == 1)].shape[0]
cantidad_mujeres_fumadoras = df[(df['is_male'] == 0) & (df['is_smoker'] == 1)].shape[0]

print("\nCantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)

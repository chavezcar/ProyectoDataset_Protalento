from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

#'data' es el objeto Dataset y 'age' es la característica de las edades
edades = np.array(data["age"])

# Calcular el promedio de edad
promedio_edad = np.mean(edades)

print("El promedio de edad de las personas participantes en el estudio es:", promedio_edad)
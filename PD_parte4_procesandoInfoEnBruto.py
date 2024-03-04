import requests
import os

def descargar_datos_csv(url: str) -> None:
    # Implementación de la función para descargar datos desde una URL y guardarlos como archivo CSV
    response = requests.get(url)
    response.raise_for_status()  # Verificar que la respuesta no tenga errores

    carpeta_actual = os.path.dirname(os.path.realpath(__file__))
    archivo_salida = os.path.join(carpeta_actual, "ResultadoConsulta.csv")

    with open(archivo_salida, "w", newline="") as csvfile:
        csvfile.write(response.text)

# Ejecuatndo la función:
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

descargar_datos_csv(url)
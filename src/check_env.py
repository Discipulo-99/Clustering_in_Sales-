import pandas as pd
import numpy as np
import sklearn

print(f"Pandas versión: {pd.__version__}")
print(f"Scikit-learn versión: {sklearn.__version__}")

path_data = r"C:\Users\Highlightning\Documents\Ciencia de Datos\Proyectos\Clustering (Customer Segmentation & Persona Profiling)\data\raw\Online Retail.xlsx"

try:
    print("Cargando dataset")
    df = pd.read_excel(path_data)
    print("¡Dataset cargado con éxito!")
    print(f"Dimensiones del dataset: {df.shape[0]} filas, {df.shape[1]} columnas")
    print(f"\nPrimeras 3 filas")
    print(df.head(3))
except Exception as e:
    print(f"Error al cargar los datos: {e}")
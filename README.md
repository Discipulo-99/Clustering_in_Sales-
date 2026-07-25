# 📊 E-Commerce Customer Segmentation (RFM Analysis & K-Means Clustering)

Un proyecto end-to-end de **Data Science & Marketing Analytics** enfocado en segmentar la base de clientes de una plataforma de comercio electrónico mediante el análisis de **Recency, Frequency, y Monetary (RFM)** y algoritmos de **Machine Learning No Supervisado**.

---

## 🎯 Objetivo del Proyecto

El objetivo principal es identificar comportamientos de compra y agrupar a los clientes en segmentos estratégicos e interpretables. Esto permite al equipo de marketing y ventas diseñar campañas personalizadas, optimizar estrategias de retención y maximizar el *Customer Lifetime Value* (CLV).

---

## 🛠️ Tech Stack & Arquitectura

* **Lenguaje:** Python 3.11+
* **Procesamiento de Datos:** Pandas, NumPy
* **Visualización:** Seaborn, Matplotlib
* **Machine Learning & Preprocesamiento:** Scikit-Learn (`StandardScaler`, `KMeans`, `PCA`)
* **Persistencia de Modelos:** Joblib
* **Control de Versiones & Entorno:** Git, VS Code / Jupyter Notebooks

---

## 🚀 Metodología & Pipeline de Trabajo

### 1. Exploración y Limpieza de Datos (EDA)
* Filtrado de registros sin ID de cliente, transacciones de prueba y devoluciones.
* Consolidación de historial de ventas de **3.5 años** (2023 - Junio 2026).

### 2. Feature Engineering (Métricas RFM)
Generación del dataset consolidado a nivel de cliente con tres métricas clave:
* **Recency ($R$):** Días transcurridos desde la última compra.
* **Frequency ($F$):** Cantidad total de órdenes únicas.
* **Monetary ($M$):** Gasto total acumulado.

### 3. Preprocesamiento & Escalado
* Transformación logarítmica (`log1p`) para mitigar el sesgo a la derecha (*right-skewness*) de las variables financieras.
* Normalización con `StandardScaler` para estandarizar las magnitudes antes del clustering.

### 4. Modelado & Evaluación (K-Means)
* Selección de $K=4$ evaluando las métricas de **Método del Codo (Elbow Method)** y **Puntaje de Silueta (Silhouette Score)**.
* Identificación de 4 perfiles claros de clientes:
  * **VIP / Champions**
  * **Loyal / Regular**
  * **Up-and-Comers / Newcomers**
  * **Inactive / At Risk**

### 5. Reducción de Dimensionalidad (PCA)
* Aplicación de **PCA (Principal Component Analysis)** para proyectar el espacio 3D de RFM a un plano 2D con fines gráficos.
* **Varianza Explicada:** Con solo 2 componentes principales ($PC_1$ y $PC_2$), se logró preservar el **94.2%** de la información total del dataset.

---

## 📈 Visualización de Segments (Proyección PCA 2D)

La siguiente proyección muestra la separación clara y las fronteras vectoriales bien definidas entre los 4 grupos de clientes:

| Componente | Varianza Explicada | Captura Principal |
| :--- | :--- | :--- |
| **PC1** | 75.6% | Valor económico y frecuencia del cliente |
| **PC2** | 18.6% | Comportamiento temporal / Recencia |
| **Total 2D** | **94.2%** | **Fidelidad casi exacta del espacio original** |

---

## 💾 Inferencia & Consumo del Modelo en Producción

Los artefactos del modelo se encuentran persistidos en el directorio `models/`:
* `models/scaler_rfm.joblib`: Objeto `StandardScaler` ajustado.
* `models/kmeans_rfm.joblib`: Modelo `KMeans` entrenado.

### Ejemplo de Predicción de Nuevo Cliente

```python
import joblib
import numpy as np
import pandas as pd

# 1. Load Saved Objects
loaded_scaler = joblib.load("models/scaler_rfm.joblib")
loaded_kmeans = joblib.load("models/kmeans_rfm.joblib")

# 2. Mapping Dictionary for Business Segments
cluster_names = {
    0: "Loyal / Regular",
    1: "Up-and-Comers / Newcomers",
    2: "Inactive / At Risk",
    3: "VIP / Champions"
}

# 3. Let's assume a new customer with: Recency=12 days, Frequency=5 purchases, Monetary=$1,200
new_client_raw = pd.DataFrame([[12, 5, 1200]], columns=["Recency", "Frequency", "Monetary"])

# 4. Apply the logarithm
new_client_log = np.log1p(new_client_raw)

# 5. Transform using the saved Scaler
scaled_array = loaded_scaler.transform(new_client_log)
new_client_scaled = pd.DataFrame(scaled_array, columns=new_client_log.columns)

# 6. Predict the Cluster
assigned_cluster_id = loaded_kmeans.predict(new_client_scaled)[0]

# 7. Map the ID to the human-readable name of the segment
assigned_cluster_name = cluster_names.get(assigned_cluster_id, "Unknown")

print(f"The Client belong to the Cluster: {assigned_cluster_name}")

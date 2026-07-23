###### **# Acceder a las carpetas**

Bash

cd Proyectos

cd "Clustering (Customer Segmentation \& Persona Profiling)"



###### **# Creamos un entorno aislado de Python en la carpeta .venv:**

&#x09;*.venv (con punto) es una carpeta oculta.*

&#x09;*venv (sin punto) es una carpeta normal.*

Bash

python -m venv .venv



###### **# Activar el entorno**

Bash

source .venv/Scripts/activate



###### **# Crear y activar el entorno virtual en VS Code**

1. Abrir la paleta de comandos (Ctrl + Shift + P) en VS Code
2. busca "Python: Select Interpreter"
3. selecciona "Enter interpreter path..."
4. vamos a la ruta .venv\\Scripts\\python.exe.
5. finalizamos dando clic en "Select Interpreter"



###### **# Instalar las librerías del proyecto**

Bash

pip install pandas numpy matplotlib seaborn scikit-learn scipy openpyxl jupyter



###### **# Tip para GitHub: Genera tu archivo requirements.txt ejecutando:**

Bash

pip freeze > requirements.txt



###### **# Script rápido de verificación (check\_env.py)**

Bash

cd src

python check\_env.py



*## Debe dar el siguiente resultado*

Scikit-learn versión: 1.8.0

Cargando dataset

¡Dataset cargado con éxito!

Dimensiones del dataset: 541909 filas, 8 columnas



Primeras 3 filas

&#x20; InvoiceNo StockCode                         Description  Quantity         InvoiceDate  UnitPrice  CustomerID         Country

0    536365    85123A  WHITE HANGING HEART T-LIGHT HOLDER         6 2010-12-01 08:26:00       2.55     17850.0  United Kingdom

1    536365     71053                 WHITE METAL LANTERN         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom

2    536365    84406B      CREAM CUPID HEARTS COAT HANGER         8 2010-12-01 08:26:00       2.75     17850.0  United Kingdom



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



###### **# Acceder a las carpetas**

Bash

cd Proyectos

cd "Clustering (Customer Segmentation & Persona Profiling)"



###### **# Activar el entorno**

Bash

source .venv/Scripts/activate



###### **# Script rápido de verificación (check\_env.py)**

Bash

cd src

python check\_env.py








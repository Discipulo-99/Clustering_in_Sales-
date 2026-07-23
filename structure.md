marketing-churn-prediction/
│
├── data/
│   ├── raw/                  # Datos originales (o link si son muy pesados)
│   └── processed/            # Datos limpios listos para modelar
│
├── notebooks/                # Exploración y prototipado
│   ├── 01_eda_and_cleaning.ipynb
│   └── 02_model_training.ipynb
│
├── src/                      # Código modularizado
│   ├── __init__.py
│   ├── data_loader.py
│   └── predict.py
│
├── .gitignore
├── requirements.txt          # Dependencias (pandas, scikit-learn, etc.)
└── README.md                 # ¡El documento más importante!
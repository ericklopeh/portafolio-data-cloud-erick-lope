# 🧩 Proyecto 1 – ETL Cloud Data Pipeline

### 📋 Descripción
Este proyecto implementa un pipeline **ETL (Extract, Transform, Load)** con Python, donde se extraen datos desde un archivo CSV, se limpian y transforman, y se generan métricas de negocio junto con visualizaciones.

---

### 🎯 Objetivos
- Realizar **extracción, transformación y carga (ETL)** de datos de ventas.  
- Implementar manejo de codificación y limpieza de datos nulos.  
- Calcular métricas de desempeño como **margen de ganancia (`profit_margin`)**.  
- Generar una visualización automática de ventas por ciudad.  

---

### ⚙️ Tecnologías utilizadas
- Python 3.11  
- Pandas  
- Matplotlib  
- Dotenv  
- Visual Studio Code  
- Oracle Cloud (para despliegue futuro)

---

### 🗂️ Estructura del proyecto
proyecto_1_etl_pipeline/
├── data/
│ ├── Sample_Superstore.csv
│ ├── superstore_clean.csv
│ └── top_cities.png
├── etl.py
├── .env
└── requirements.txt

yaml
Copiar código

---

### 🚀 Ejecución

1. **Crear entorno virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
Instalar dependencias:



pip install -r requirements.txt
Ejecutar el pipeline:



python etl.py


📊 Resultados

Dataset limpio: data/superstore_clean.csv

Visualización generada: data/top_cities.png

Validación automática de codificación y valores faltantes.

🧑‍💻 Autor

Erick Lope
ericklopeh@icloud.com
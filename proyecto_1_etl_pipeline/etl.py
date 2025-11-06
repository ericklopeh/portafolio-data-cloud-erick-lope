from pathlib import Path
import os
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# ===== 1) Configuración inicial =====
BASE_DIR = Path(__file__).resolve().parent           # C:\Portafolio\proyecto_1_etl_pipeline
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)

# Cargar ruta desde .env o usar valor por defecto
csv_env = os.getenv("CSV_PATH")
CSV_PATH = (BASE_DIR / csv_env).resolve() if csv_env else (BASE_DIR / "data" / "Sample_Superstore.csv").resolve()

print("Usando CSV:", CSV_PATH)
if not CSV_PATH.exists():
    print(f"❌ No se encontró el archivo CSV en la ruta: {CSV_PATH}")
    raise SystemExit(1)

# ===== 2) Extracción de datos =====
try:
    df = pd.read_csv(CSV_PATH, encoding="utf-8")
except UnicodeDecodeError:
    print("Archivo no está en UTF-8, reintentando con Latin-1...")
    df = pd.read_csv(CSV_PATH, encoding="latin1")

print(" Datos cargados:", df.shape, "filas")

# ===== 3) Limpieza de datos =====
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

if "order_id" in df.columns:
    df = df.drop_duplicates(subset=["order_id"], keep="last")

# Rellenar valores nulos comunes
fill_map = {}
for c in ["city", "state", "region"]:
    if c in df.columns:
        fill_map[c] = "Desconocido"
if "postal_code" in df.columns:
    fill_map["postal_code"] = 0
df = df.fillna(fill_map)

print(" Datos limpios:", df.shape)

# ===== 4) Transformación de datos =====
if all(c in df.columns for c in ["profit", "sales"]):
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce").fillna(0)
    df["profit"] = pd.to_numeric(df["profit"], errors="coerce").fillna(0)
    df["profit_margin"] = (df["profit"] / df["sales"].replace(0, pd.NA)).round(3)

# ===== 5) Carga de datos (CSV limpio) =====
out_csv = BASE_DIR / "data" / "superstore_clean.csv"
df.to_csv(out_csv, index=False)
print(f"Archivo transformado guardado en: {out_csv}")

# ===== 6) Visualización =====
if "city" in df.columns and "sales" in df.columns:
    top_cities = df.groupby("city")["sales"].sum().nlargest(10)
    plt.figure(figsize=(10, 5))
    top_cities.plot(kind="bar", color="skyblue")
    plt.title("Top 10 ciudades por ventas")
    plt.ylabel("Ventas ($)")
    plt.tight_layout()
    out_png = BASE_DIR / "data" / "top_cities.png"
    plt.savefig(out_png)
    plt.show()
    print(f"Gráfico guardado en: {out_png}")

# ===== 7) Final =====
print("ETL completado correctamente.")

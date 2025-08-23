# 0. CARGAR LIBRERIAS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

CSV_PATH = "/mnt/data/DatosProyectoMineria.csv"

# 1. CARGA DE DATOS
df = pd.read_csv(CSV_PATH)

# 2. LIMPIEZA DE DATOS
df.columns = [c.strip() for c in df.columns]
rename_map = {
}
df = df.rename(columns=rename_map)

def normalize_str(s):
    if pd.isna(s):
        return s
    s = str(s).strip().upper()
    s = (s.replace("Á", "A")
           .replace("É", "E")
           .replace("Í", "I")
           .replace("Ó", "O")
           .replace("Ú", "U")
           .replace("Ñ", "N"))
    s = " ".join(s.split())
    return s

for col in ["municipio_productor","departamento","recurso_natural","nombre_proyecto",
            "trimestre","unidad_medida","tipo_contraprestacion"]:
    df[col] = df[col].apply(normalize_str)

for col in ["anio_produccion","valor_contraprestacion","cantidad_produccion"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["anio_produccion","recurso_natural","unidad_medida"])

# 3. CONVERSION DE UNIDADES
def to_toneladas(valor, unidad):
    if pd.isna(valor):
        return np.nan
    if unidad == "GRAMOS":
        return valor / 1_000_000.0
    elif unidad == "KILOGRAMOS":
        return valor / 1_000.0
    elif unidad == "TONELADAS":
        return float(valor)
    else:
        return np.nan

df["produccion_ton"] = df.apply(lambda r: to_toneladas(r["cantidad_produccion"], r["unidad_medida"]), axis=1)

# 4. VARIABLES DERIVADAS
df["tarifa_efectiva_por_ton"] = np.where(
    (df["produccion_ton"] > 0),
    df["valor_contraprestacion"] / df["produccion_ton"],
    np.nan
)

# 5. RESÚMENES
resumen_anual = (df.groupby("anio_produccion", as_index=False)
                   .agg(produccion_ton_total=("produccion_ton","sum"),
                        contraprestacion_total=("valor_contraprestacion","sum")))
resumen_anual["tarifa_efectiva_anual"] = np.where(
    resumen_anual["produccion_ton_total"] > 0,
    resumen_anual["contraprestacion_total"] / resumen_anual["produccion_ton_total"],
    np.nan
)

resumen_material = (df.groupby("recurso_natural", as_index=False)
                      .agg(produccion_ton_total=("produccion_ton","sum"),
                           contraprestacion_total=("valor_contraprestacion","sum")))
resumen_material["tarifa_efectiva_material"] = np.where(
    resumen_material["produccion_ton_total"] > 0,
    resumen_material["contraprestacion_total"] / resumen_material["produccion_ton_total"],
    np.nan
)

resumen_anio_mat = (df.groupby(["anio_produccion","recurso_natural"], as_index=False)
                      .agg(produccion_ton_total=("produccion_ton","sum"),
                           contraprestacion_total=("valor_contraprestacion","sum")))
resumen_anio_mat["tarifa_efectiva_ano_mat"] = np.where(
    resumen_anio_mat["produccion_ton_total"] > 0,
    resumen_anio_mat["contraprestacion_total"] / resumen_anio_mat["produccion_ton_total"],
    np.nan
)

# 6. GRÁFICAS
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.figure()
plt.bar(resumen_anual["anio_produccion"], resumen_anual["produccion_ton_total"])
plt.title("Producción total (ton) por año")
plt.xlabel("Año")
plt.ylabel("Toneladas")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "prod_total_anual.png"), dpi=200)
plt.close()

plt.figure()
plt.plot(resumen_anual["anio_produccion"], resumen_anual["contraprestacion_total"], marker="o")
plt.title("Contraprestación total por año")
plt.xlabel("Año")
plt.ylabel("Valor de contraprestación (COP)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "contraprestacion_total_anual.png"), dpi=200)
plt.close()

top_materiales = resumen_material.sort_values("contraprestacion_total", ascending=False).head(10)
plt.figure()
plt.barh(top_materiales["recurso_natural"], top_materiales["contraprestacion_total"])
plt.title("Top 10 materiales por contraprestación acumulada")
plt.xlabel("Valor de contraprestación (COP)")
plt.ylabel("Recurso natural")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "top_materiales_contraprestacion.png"), dpi=200)
plt.close()

top6 = top_materiales["recurso_natural"].head(6).tolist()
pivot_tarifa = (resumen_anio_mat[resumen_anio_mat["recurso_natural"].isin(top6)]
                .pivot_table(index="anio_produccion",
                             columns="recurso_natural",
                             values="tarifa_efectiva_ano_mat"))
plt.figure()
for col in pivot_tarifa.columns:
    plt.plot(pivot_tarifa.index, pivot_tarifa[col], marker="o", label=str(col))
plt.title("Tarifa efectiva (COP/ton) por material y año (Top 6)")
plt.xlabel("Año")
plt.ylabel("COP por tonelada")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "tarifa_efectiva_top6.png"), dpi=200)
plt.close()

plt.figure()
plt.scatter(resumen_anio_mat["produccion_ton_total"], resumen_anio_mat["contraprestacion_total"])
plt.title("Producción vs. Contraprestación (año-material)")
plt.xlabel("Producción total (ton)")
plt.ylabel("Contraprestación total (COP)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "scatter_prod_vs_contraprestacion.png"), dpi=200)
plt.close()
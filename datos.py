#Importar librerías necesarías
import pandas as pd

# leer el archivo csv en un DataFrame
df=pd.read_csv("./datosminas.csv")

#contar cantidad de registros
df.count()

# Mostrar las primeras filas del DataFrame
print("===============Vista inicial del DataFrame===================")
print(df.head(10))

# 1 verificar valores nulos
print("\n Valores nulos por columnas:")
print(df.isnull().sum())


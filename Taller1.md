# 🧪 Taller Práctico: Análisis de Datos con Pandas
#Nivel: Básico - Intermedio
#Objetivo: Aplicar los conceptos de Series y DataFrame en Pandas utilizando una base de datos ficticia de estudiantes.

## 📁 Dataset: Información de Estudiantes
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset ficticio
datos_estudiantes = {
    "peso": pd.Series([55, 68, 74, 60, 72], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "altura": pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "promedio": pd.Series([4.5, 3.8, 4.2, 2.9, 3.5], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "edad": pd.Series([17, 18, 17, 19, 18], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
}
df = pd.DataFrame(datos_estudiantes)
print(df)
```
## 🧩 Actividades
#1. Crear una Serie con los nombres y alturas de los estudiantes
```
altura = pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
print(altura)
```
# Pregunta: ¿Cuál es la altura de Daniela
```
print(altura.loc['Daniela'])
```

#2. Accede al promedio de calificación de Carlos de 3 formas diferentes:
# promedio de carlos usando loc
```
promedio_Carlos=df.loc['Carlos']['promedio']
print(promedio_Carlos)
```
# promedio de carlos usando iloc
```
promedio_Carlos=df.iloc[1]["promedio"]
print(promedio_Carlos)
```
# promedio de carlos usando query
```
promedio_Carlos = df.query("index == 'Carlos'")["promedio"]
print(promedio_Carlos)
```

#3. Filtra a los estudiantes con promedio mayor o igual a 4.0
# Usando query
```
estudiantes_mayor4 = df.query("promedio >= 4.0")
print(estudiantes_mayor4)
```
# Usando loc
```
estudiantes_mayor4 = df.loc[df['promedio']>=4.0]
print(estudiantes_mayor4)
```
# Pregunta: ¿Cuántos estudiantes tienen un buen promedio?
```
numero_estudiantes = len(estudiantes_mayor4)
print(f"Hay {numero_estudiantes} estudiantes con buen promedio")
```

#4. Calcula operaciones estadísticas:
```
estadisticas=df.describe()
print(estadisticas)
```

#5. Agrega una nueva columna que indique si el estudiante es mayor de edad
```
df["Mayor de edad"] = df["edad"] >= 18
print("\nAñadiendo columna de mayor de edad: \n", df)
```

#6. Agrega una columna con el año de nacimiento (suponiendo que estamos en 2025)
```
df["año de nacimiento"] = 2025 - df["edad"]
print(df["año de nacimiento"])
```

#7. Visualiza los promedios de los estudiantes en un gráfico
```
df["promedio"].plot(kind="bar", title="Promedio de estudiantes")
plt.xlabel("Estudiante")
plt.ylabel("Nota promedio")
plt.show()
```

#8. Filtra a los estudiantes con altura entre 165 y 175 cm
```
df2 = df.query("altura >= 165 & altura <= 175")
print(df2)
```

#9. Copia el DataFrame y elimina la columna "peso"
```
df_copy = df.copy()
del df_copy['peso']
print(df_copy)
```

#10. Crea un nuevo DataFrame con solo 3 columnas: nombre, edad y año de nacimiento
```
df3=pd.DataFrame(
    df,
    columns=["edad","año de nacimiento"]
)
print(df3)
```
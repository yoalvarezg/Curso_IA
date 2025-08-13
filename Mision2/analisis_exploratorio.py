#Importar librerías necesarías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
1. Generar un DataFrame con los datos del fichero titanic.csv
2. Hacer tratamiendo de los nulos
3. Mostrar por pantalla las dimensiones del DataFrame, el numero 
   de datos que contiene, los nombres de sus columnas y filas, los
   tipos de datos de las columnas, las 10 primeras y ultimas filas
4. Mostrar por pantalla los datos del pasajero con identificador 148
5. Mostrar por pantalla las filas pares del DataFrame
6. Mostrar por pantalla los nombres de las personas que iban en
   primera clase ordenadas alfabeticamente
7. Mostrar por pantalla el porcentaje de personas que sobrevivieron 
   en cada clase
8. Mostrar por pantalla la edad media de las mujeres que viajan
   en cada clase
9. Añadir una nueva columna boleana para saber si el pasajero era
   menor de edad o no
10. Mostrar por pantalla el porcentaje de menores de edad
    que sobrevivieron en cada clase
11. Mostrar por pantalla el porcentaje de mayores de edad
    que sobrevivieron en cada clase
"""

## 1.leer el archivo csv en un DataFrame
df=pd.read_csv("./titanic.csv")
# Mostrar las primeras filas del DataFrame
print("===============Vista inicial del DataFrame===================")
print(df.head())

#imprimir las columnas
print(df.columns)

## 2.Tratamiendo de valores nulos
# Rellenar los valores de la edad (age) con la media
if 'Age' in df.columns:
    df['Age'].fillna(df['Age'].mean(),inplace=True)

# Eliminacion de columna (Cabin) debido a su alto numero de nulos mayor al 50%
if 'Cabin' in df.columns and df['Cabin'].isnull().sum()/len(df)>0.5:
    # Borramos la columna
    df.drop('Cabin',axis=1,inplace=True)

# Rellenar puerto de embarque (Embarked) con la moda
if 'Embarked' in df.columns:
    df['Embarked'].fillna(df['Embarked'].mode()[0],inplace=True)

# Impresion de los datos despues de la correccion
print("\n Valores nulos por columnas:")
print(df.isnull().sum())

# Histograma de las edades
plt.figure(figsize=(8,5))
sns.histplot(df['Age'],bins=30,color='skyblue')
plt.title("Frecuencia de la edad de los pasajeros")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
#plt.show()

# Histograma de las edades
#plt.figure(figsize=(8,5))
#sns.boxplot(x='Pclass',y='Age',data=df,palette='set2')
#plt.title("Distribucion de las edades por clase")
#plt.xlabel("Clase")
#plt.ylabel("Edad")
#plt.show()

# Diagrama de sectores de fallecidos y supervivientes
#df_numerico=df.select.dtypes(include='number')
#correlacion_matriz=df_numerico.corr()
#sns.heatmap(correlacion_matriz, annot=True, cmap='coolwarm')
#plt.title("Correlaciones entre las caracteristicas")
#plt.show()

# Diagrama de sectores de fallecidos y supervivientes
#plt.figure()
#df.survived.value_counts().plot(kind='pie'),
#labels=["Muertos","Supervivientes"],title=['Diagrama de torta de % de vivos y miertos']
#autopct=('%1.1f%%')
#plt.show()

# Diagrama de barras con el numero de personas de cada clase
df.Pclass.value_counts().plot(kind='bar',title='Numero de personas por clase')
#plt.show()

# 3. 
print('Dimensiones:',df.shape)
print('Numero de elementos:',df.size)
print('Nombre de filas:',df.index)
print('Tipos de datos:',df.dtypes)
print('Primeras 10 filas:',df.head(10))
print('Ultimas 10 filas:',df.tail(10))

#4. Pasajero 148 (n-1)
print(f"El pasajero 148 es {df.loc[147]}")




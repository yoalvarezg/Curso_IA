# Librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creacion de objetos serie
s= pd.Series([2,4,6,8,10])
print(s)

# Creacion de un objeto Serie inicializado con un diccionario de python
altura={"Santiago":180,"Marcelo":172,"Luis":174,"Alejandra":160}
s=pd.Series(altura)
print(s)
"""
Creacion de un objeto Series inicializandolo con algunos
de los elementos de un diccionario python
"""
altura={"Santiago":180,"Marcelo":172,"Luis":174,"Alejandra":160}
s=pd.Series(altura,index=["Marcelo","Luis"])
print(s)

#Creacion de un objeto Series inicializandolo con un escalar
s=pd.Series(34,["test1","test2","test3"])
print(s)

# Acceso a los Elementos de un objeto Series
# cada elemento de objeto series tiene un identificador unico
s=pd.Series([2,4,6,8],index=["num1","num2","num3","num4"])
print(s)
# accediendo al tercer elemento objeto
print(s["num3"])
# acceder por la posicion
print(s.iloc[2])
print(s.loc["num3"])
#aceder al segundo y tercer elemento por posicion
print(s.iloc[2:4])

# Operaciones aritmeticas con series
#sumar
print(np.sum(s))
print(f"suma",np.sum(s))

# Creacion de un objeto series denominado temperaturas
temperaturas=pd.Series([4.4,5.1,6.1,6.2,6.1,6.1,5.2,4.7,4.1,3.9])
s=pd.Series(temperaturas,name="Temperaturas")
print(s)
#s.plot()
#plt.show()

#Creacion de un objeto DataFrame
personas={
    "peso":pd.Series([90,80,70,60],["Santiago","Marcelo","Luis","Alejandra"]),
    "altura":pd.Series({"Santiago":180,"Marcelo":172,"Luis":174,"Alejandra":160}),
    "hijos":pd.Series([2,3],["Luis","Marcelo"])
}
df=pd.DataFrame(personas)
print(df)
df2=pd.DataFrame(
    personas,
    columns=["altura","peso"],
    index=["Santiago","Luis","Marcelo"]
)
print(df)
#Acceso a los elementos
print(df["peso"])
#combinar metodos
print((df["peso"]>=60) & (df["peso"]<80))

print(df.iloc[1:3])
#Consultas avanzadas
df4=df.query("altura >= 170 and peso >70")
print(df)
#copiar un dataframe
df_copy=df.copy()
#añadirle una nueva columna
df_copy["cumpleaños"]=[1990,1991,1997,2000]
print(df_copy)
#añadir columna calculada
df_copy["años"]=2025 - df_copy["cumpleaños"]
print(df_copy)


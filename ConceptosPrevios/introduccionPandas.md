# Introduccion Pandas
Python 3.13.5
## librerias
```
import pandas as pd
```
## Creacion de objetos serie
s= pd.Series([2,4,6,8,10])
print(s)

## Creacion de un objeto Serie inicializado con un diccionario de python
altura={"Santiago":180,"Marcelo":172,"Luis":174,"Alejandra":160}
s=pd.Series(altura)
print(s)

## Creacion de un objeto Series inicializandolo con algunos de los elementos de un diccionario python
altura={"Santiago":180,"Marcelo":172,"Luis":174,"Alejandra":160}
s=pd.Series(altura,index=["Marcelo","Luis"])
print(s)

## Creacion de un objeto Series inicializandolo con un escalar
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

# acceder al segundo y tercer elemento por posicion
print(s.iloc[2:4])
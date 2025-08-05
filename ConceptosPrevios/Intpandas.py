import pandas as pd

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
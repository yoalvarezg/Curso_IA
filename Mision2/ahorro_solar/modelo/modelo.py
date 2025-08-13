import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

data ={
    'ubicacion':['zona_1','zona_2','zona_1','zona_3','zona_2'],
    'tamano_hogar':[3,4,2,5,3],
    'costo_instalacion':[5000,6000,4500,7000,5200],
    'energia_generada':[3000,32000,2500,4000,2900],
    'ahorro_real':[1800,2000,1500,2300,1750]
}
df =pd.DataFrame(data)
#print(df)
# Separar variables
x= df.drop(columns='ahorro_real')
y= df['ahorro_real']
# Codificar variables categoricas
x_encoded=pd.get_dummies(x)
#print(x_encoded)
# Dividir datos
x_train,x_test,y_train,y_test=train_test_split(x_encoded,y,test_size=0.2,random_state=42)
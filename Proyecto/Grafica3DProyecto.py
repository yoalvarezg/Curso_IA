import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

#===================
# 1. Carga de datos
#===================
df = pd.read_csv('curso IA\Proyecto\DatosProyectoMineria.csv')
print(df['Año Produccion'])

x=df[['Año Produccion','Valor Contraprestacion ','Cantidad Producción']]
print(x)

#===========================
# Entrenar K_Means con k=6
#===========================
kmeans=KMeans(n_clusters=5,random_state=42)
kmeans.fit(x)
df['Cluster']=kmeans.labels_

#================================
# Graficas en 3D con anotaciones
#================================
fig=plt.figure(figsize=(10,7))
ax=fig.add_subplot(111,projection='3d')

# Colocar colores a los Clusters
sc =ax.scatter(df['Año Produccion'],df['Valor Contraprestacion '],df['Cantidad Producción'],
               c=df['Cluster'],cmap='viridis',s=50)

# Etiquetas de ejes
ax.set_xlabel('Año Produccion')
ax.set_ylabel('Valor Contraprestacion ')
ax.set_zlabel('Cantidad Producción')
plt.title('Segmentacion de Produccion-Contraprestacion Kmeans k=5')

# Anotaciones interpretativas
ax.text(2012,10000000,1000000,'Contraprestacion pagada en 2012',color='black')
ax.text(2014,20000000,2000000,'Contraprestacion pagada en 2014',color='black')
ax.text(2016,30000000,3000000,'Contraprestacion pagada en 2016',color='black')
ax.text(2018,40000000,4000000,'Contraprestacion pagada en 2018',color='black')
ax.text(2020,50000000,5000000,'Contraprestacion pagada en 2020',color='black')
plt.show()
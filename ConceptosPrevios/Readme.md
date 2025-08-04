# Comandos
```
python --version
Python 3.13.5
git --version
pip list
actualizar pip
python.exe -m pip install --upgrade pip
```

## Crear entorno virtual
python -m venv env
## Activar entorno
env/scripts/activate
para activar en powershell ejecuto y dar s
set-executionPolicy unrestricted

# Estructura de datos en pandas
| Tipo      | contenido                                     |
| --------- | --------------------------------------------- |
| Series    | Array de una dimension                        |
| Dataframe | se corresponde con una tabla de 2 dimensiones |
| Panel     | Similar a un diccionario de Dataframe         |

# Creacion de objetos series
```
import pandas as pd # pip install pandas
# Creacion de objetos serie
s= pd.Series([2,4,6,8,10])
print(s)
```

manejo de git
git init
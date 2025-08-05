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
git add .
git commit -m "introduccion a pandas 5%"
si sale error
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

crear archivo requirements.txt
pip freeze > requirements.txt
clonar repositorio
como desactivar el entorno virtual
>deactivate

Para clonar se abre nuevo folder en escritorio y se pone
git clone https://github.com/yoalvarezg/Curso_IA.git #link del codigo en github

para recuperar las librerias de un proyecto
pip install -r requirements.txt
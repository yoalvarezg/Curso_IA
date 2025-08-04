#Tipos de datos numericos

#Asignamos un tipo de dato numerico entero
x=6
print(x)
print(type(x))

#Asignamos un tipo de dato numerico decimal
x=6.8
print(x)
print(type(x))

"""
calcular el resultado de la siguente operacion; sumar dos numeros y dividir el resultado entre 2
"""
x=(8+2)/2
print(x)

"""
Calcular el area del circulo pi*r**2
"""
pi=3.1416
r=2
area_circulo=pi*r**2
print(area_circulo)

"""
Hallar el area del circulo y el volumen del cilindro, si r=2 y h=4
"""
pi=3.1416
r=2
h=4
area_circulo=round(pi*(r**2),2)
volumen_cilindro=round(pi*(r**2)*h,2)
print(area_circulo)
print(volumen_cilindro)

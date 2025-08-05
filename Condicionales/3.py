# Indicar si un numero es divisible entre 3 y 5 al mismo tiempo
numero=int(input("Ingrese un numero:"))

if numero % 3 == 0 and numero% 5 == 0:
   print("Su numero ES divisible entre 3 y 5.")
else:
   print("Su numero NO ES divisible entre 3 y 5")
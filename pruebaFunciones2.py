#from funciones import resta
#from funciones import suma

#importar todo de funciones.py
import funciones
import conexiones
import librerias/laslibrerias.py


valor1 = 9
valor2 = 6
#print("La suma es ",funciones.multiplicaciones(valor1,valor2))


if conexiones.conectarArduino(2000,15000):
    print("si se  logró la conexion")
else:
    print("No se logró la conexion")



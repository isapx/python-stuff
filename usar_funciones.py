from funciones import suma
import conexiones


def saludar(nombre="Anonimo"):
    print("Hola ,",nombre)

def sumar(a, b):
    return a + b

a = 5
b = 10

def sumador(*numeros):
    suma_ = 0
    for numero in numeros:
        suma_ = suma_ + numero
    return suma_

laSuma = suma(5,10)

print("la suma es: ",laSuma)

saludar("Isaias")
saludar()
sumar(5,8)
variasSumas = sumador(5,10,20,30)
print( )

if conexiones.conectarArduino(5000,12000):
    print("se conecto al arduino")
else:
    print("No se conecto al arduino")

if conexiones.conectarPLC():
    print("Se conectó al PLC")
else:
    print("No se conecto al PLC")
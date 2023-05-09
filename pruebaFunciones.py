

def saludar(nombre="Goku"):
    #aqui va el codigo de la FUNCION
    saludo = "Hola " + nombre
    return saludo


def holaMundo():
    print("Hola mundo")

def suma():
    suma = 2 + 8
    print(suma)




if __name__ == "__main__":
   try:
    print(saludar())
   except:
    print("Error el usar la funcion")




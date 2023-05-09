contador = 0
while True:    
    aNacimiento = 1900
    try:
        aNacimiento = int(input("Dame tu año de nacimiento: "))
    except ValueError as otroError:
        if contador == 5:
            print("Ya se acabaron los intentos (5)")
            break #termina el ciclo
        contador = contador + 1
        print(f"ERROR {contador}: PONER SOLO NUMEROS")
        continue #termina la iteracion
    laEdad = 2023-aNacimiento
    print("Tu edad es :",laEdad)
    break #termina el ciclo
print("Listo, ya terminó el programa")

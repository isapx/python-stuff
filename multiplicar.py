import random

#numeros_posibles = list(range(1, 11))
#numeros_posibles = list((1,2,3,4,5,6,7,8,9,10))
numeros_posibles = [1,2,3,4,5,6,7,8,9,10]

print("Dime que tabla de multiplicar quieres aprender")
tabla = int(input("😎 >"))
aciertos = 0
errores = 0
while True:
    numero_aleatorio = random.choice(numeros_posibles)
    #print(numero_aleatorio)
    resultado_usuario = int(input(f"{tabla} X {numero_aleatorio} = "))
    if resultado_usuario == numero_aleatorio * tabla:
        print(f"¡Bien hecho! 👍 {tabla} X {numero_aleatorio} = {numero_aleatorio * tabla}")
        #aciertos = aciertos + 1
        aciertos += 1
    else:
        print(f"¡Lo siento! 😭 {tabla} X {numero_aleatorio} = {numero_aleatorio * tabla}")
        errores = errores + 1
    numeros_posibles.remove(numero_aleatorio)
    if not numeros_posibles:
        print(f"Terminamos la tabla del {tabla}")
        print(f"¡Aciertos: ✔️ {aciertos}!")
        print(f"¡Errores: ❌ {errores}!")
        break
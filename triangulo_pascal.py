
coheficientes = [1]
#coheficientes = [1,2,1]
#coheficientes = [1,3,3,1]
potencia = 40
nuevo = [None] * len(coheficientes)
#nuevo = coheficientes
n = 0
tam = len(coheficientes)
#print("Tamaño: ", tam)
while n < potencia:
    #for i in range(len(coheficientes)-1):
    for i in range(tam-1):
        #print(i)
        nuevo[i+1] = coheficientes[i] + coheficientes[i+1]
        #print(f"Datos: nuevo[{i+1}] = {nuevo[i+1]} coheficientes[{i}] = {coheficientes[i]} coheficientes[{i+1}] = {coheficientes[i+1]}")
    nuevo[0]=1
    nuevo.append(1)
    coheficientes = nuevo.copy()
    n = n + 1
    tam = len(nuevo)
    i = 0
    #print("Tamaño: ",tam)
    #break
print(nuevo)

#para imprimir con formato de numeros con como para los miles
for elemento in nuevo:
    print(f"{elemento:,}", end="; ")

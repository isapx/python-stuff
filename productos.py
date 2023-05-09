producto1_nombre = input("Dame el nombre de Producto 1 ")
producto1_cantidad = int(input("Dame la cantidad del Producto 1 "))
producto1_precio = int(input("Dame el precio unitario de Producto 1 "))

producto2_nombre = input("Dame el nombre de Producto 2 ")
producto2_cantidad = int(input("Dame la cantidad del Producto 2 "))
producto2_precio = int(input("Dame el precio unitario de Producto 2 "))

producto3_nombre = input("Dame el nombre de Producto 3 ")
producto3_cantidad = int(input("Dame la cantidad del Producto 3 "))
producto3_precio = int(input("Dame el precio unitario de Producto 3 "))

subtotal = (producto1_cantidad * producto1_precio) + (producto2_cantidad * producto2_precio) + (producto3_cantidad * producto3_precio)

iva = subtotal * .16

total = subtotal + iva

print("Importe a pagar: " + str(total))
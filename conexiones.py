

def conectarArduino(puerto,tasaTransferencia):
    #variable para saber si esta conectado o no
    conectado = False
    
    #aqui va la logica de la conexion al arduino

    mensaje = f"Se conecto correctamente al arduino al puerto {puerto}, con una tasa de transferencia de {tasaTransferencia}"
    print(mensaje)

    conectado = False

    return conectado

def conectarPLC(puerto=8001, tasaTransferencia=9200):
    conectado = False
    
    #aqui va la logica de la conexion al arduino

    mensaje = f"No se pudo conectar al PLC al puerto {puerto}, con una tasa de transferencia de {tasaTransferencia}"
    print(mensaje)

    conectado = False

    return conectado

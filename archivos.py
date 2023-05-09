def metodoUno():
    ruta = "archivo2.txt"
    with open(ruta, mode ="w", encoding="utf-8") as archivo:
        print("Hola Isaias", file=archivo)
        archivo.write("Hola en segunda linea")


def metodoDos():
    nombre = "archivo2.txt"
    f = open(nombre, mode ="w", encoding="utf-8")
    f.write("Hola isaias\n")
    print("Hola en segunda linea",file=f)

def ejercicio1():
    n = int(input('Introduce un número entero entre 1 y 10: '))
    nombre_fichero = 'tabla-' + str(n) + '.txt'
    f = open(nombre_fichero, 'w')
    for i in range(1, 11):
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
    f.close()

def ejercicio2():
    from urllib import request
    from urllib.error import URLError
    url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
    try:
        with request.urlopen(url) as f:
            datos = f.read().decode('utf-8').split('\n') # Leer los datos y guardar cada línea en una lista.
    except URLError:
        return('¡La url ' + url + ' no existe!')
    print(datos)

def leerArchivo():
    ruta="archivo2.txt"
    with open(ruta, mode ="r", encoding="utf-8") as archivo:
        for linea in archivo:
            print(linea)

if __name__ == "__main__":
    leerArchivo()

#crear un archivo que se llame alumnos.csv
#este va a tener los datos de los alumnos separados por comas
#datos a guardar: nombre, apellido paterno, apellido materno, carrera, numero de control, edad
#ejemplo:Fulano,Lopez,Perez,IMC,22600025,23


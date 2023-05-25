import sys
from zipfile import ZipFile
import pandas as pd

def descomprimir(nombre):
    with ZipFile(nombre, 'r') as zip:
        zip.extractall()

def leer_datos (nombre):
    datos = pd.read_csv(nombre, sep= ';')
    return datos

if __name__== '__main__':
    if len(sys.argv) != 2:
        print("Error. Número de parámetros incorrecto. Puede faltar el nombre del archivo")
    else:
        nombre_fichero = sys.argv[1]
        #print(nombre_fichero) --> se utilizó para corroborar que se ejecutó de manera correcta
        descomprimir(nombre_fichero)
        datos=leer_datos(nombre_fichero)
        #print(datos)
        #print(datos.columns)
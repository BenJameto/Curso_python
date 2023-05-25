import sys
from zipfile import ZipFile
import pandas as pd
import sqlite3
from sqlite3 import Error



basededatos= 'coches.db'

def descomprimir(nombre):
    with ZipFile(nombre, 'r') as zip:
        zip.extractall()

def leer_datos (nombre):
    datos = pd.read_csv(nombre, sep= ';')
    return datos

def crear_conexion():
    try:
        conexion = sqlite3.connect(basededatos)
        return conexion
    except Error:
        print(Error)

def crear_tablaCoches(conexion):
    cursor = conexion.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS coches(marca text, modelo text, combustible text, transmision text, estado text, matricula text, kilometraje integer, potencia real, precio real)')
    conexion.commit()

def grabar_tabla(conexion,datos):
    tuplas = datos.itertuples(index=False)

    for tupla in tuplas:
        marca = tupla[0]
        modelo = tupla[1]
        combustible = tupla[2]
        transmision = tupla[3]
        estado = tupla[4]
        matricula = tupla[5]
        kilometraje = tupla[6]
        potencia = tupla[7]
        precio = tupla[8]

        coche = (marca, modelo, combustible,transmision,estado,matricula,kilometraje,potencia,precio)
        insertar_coche(conexion,coche)

def insertar_coche(conexion, coche):
    cursor=conexion.cursor()
    cursor.execute('INSERT INTO coches(marca, modelo, combustible,transmision,estado,matricula,kilometraje,potencia,precio) VALUES (?,?,?,?,?,?,?,?,?)',coche)
    conexion.commit()


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

        conexion=crear_conexion()
        crear_tablaCoches(conexion)
        grabar_tabla(conexion, datos)
        conexion.close()
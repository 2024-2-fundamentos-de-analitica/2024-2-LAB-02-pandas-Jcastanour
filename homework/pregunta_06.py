"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def readcsv(file):
    return pd.read_csv(file, sep='\t')

def sizetabla(tabla):
    return tabla.shape

def sizeregistros(tabla):
    return tabla.groupby('c1').size()

def listunicos(tabla):
    return sorted(tabla['c4'].str.upper().unique())

def pregunta_06():

    tabla = readcsv("files/input/tbl1.tsv")

    return listunicos(tabla)

    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """

print(pregunta_06())    
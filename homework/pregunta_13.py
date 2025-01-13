"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def readcsv(file):
    return pd.read_csv(file, sep='\t')


def jointablas(tabla1, tabla2):
    return pd.merge(tabla1, tabla2, on='c0')

def pregunta_13():

    tbl0 = readcsv("files/input/tbl0.tsv")
    tbl2 = readcsv("files/input/tbl2.tsv")

    tabla = jointablas(tbl0, tbl2)

    return tabla.groupby('c1')['c5b'].sum()

    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
print(pregunta_13())     
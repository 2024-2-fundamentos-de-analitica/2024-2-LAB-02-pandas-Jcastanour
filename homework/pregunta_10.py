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

def convertidor(tabla):

    tabla['c2'] = tabla['c2'].astype(str)
    agrupado = tabla.groupby('c1')['c2'].apply(list)
    # Convertir las listas en cadenas separadas por ':'
    resultado = agrupado.apply(lambda x: ':'.join(sorted(x)))

    # Convertir el resultado a un DataFrame si es necesario
    resultado_df = resultado.reset_index()
    resultado_df.columns = ['c1', 'c2']
    resultado_df = resultado_df.set_index('c1')

    return resultado_df

def pregunta_10():

    tabla = readcsv("files/input/tbl0.tsv")
    tabla10 = convertidor(tabla)
    

    return tabla10
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """

print(pregunta_10())    
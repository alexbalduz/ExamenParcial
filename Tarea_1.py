import pandas as pd
import numbers as np
import csv

# ISSUE 1

def leer_csv (archivo):
    df = pd.read_csv(archivo, sep = ';')

    return df

nav = leer_csv('navegacion.csv')
conv = leer_csv('conversion.csv')

#ISSUE 2

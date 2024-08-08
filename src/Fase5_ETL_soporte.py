import pandas as pd
import numpy as np
import sys
import os

def abrir_archivos():
    """
    Función para abrir el .csv final del proyecto
    """
    datos = pd.read_csv("Datos/datos_empresa.csv", index_col=0)
    return datos

def borrar_colunas(datos, columnas):
    datos.drop(columns=columnas, inplace=True)

def transformar_cabeceras(datos):
    new_columns = {column: column.lower() for column in datos.columns}
    datos.rename(columns=new_columns, inplace=True)

def transformacion(datos):
    datos['age'] = datos['age'].str.replace('fifty-eight', '58').str.replace('thirty-six', '36').str.replace('fifty-five', '55').str.replace('fifty-two', '52').str.replace('thirty-one', '31').str.replace('twenty-six', '26').str.replace('thirty-seven', '37').str.replace('thirty-two', '32').str.replace('twenty-four', '24').str.replace('forty-seven', '47').str.replace('thirty', '30')
    datos['dailyrate'] = datos['dailyrate'].str.replace('$', '')
    datos['distancefromhome'] = datos['distancefromhome'].astype(str).str.replace('-', '')
    datos['gender'] = datos['gender'].map({0: 'M', 1: 'F'})
    datos['hourlyrate'] = datos['hourlyrate'].replace('Not Available', np.nan)
    datos['maritalstatus'] = datos['maritalstatus'].replace({'divorced': 'Divorced', 'Marreid': 'Married'})
    datos['remotework'] = datos['remotework'].map({'Yes': 'Yes', '1': 'Yes', 'False': 'No', '0': 'No', 'True': 'Yes'})

def eliminar_segundo_digito(num): 
    num_str = str(num) 
    if len(num_str) == 2: 
        return int(num_str[0]) # Mantén solo el primer dígito 
    return num

def cambiar_float(datos, cols):
    for col in cols:
        datos[col] = datos[col].apply(lambda dato: float(dato.replace(",", ".")) if isinstance(dato, str) else np.nan)

def cambiar_int(datos, cols):
    for col in cols:
        datos[col] = datos[col].apply(lambda dato: int(dato) if isinstance(dato, str) else np.nan)

def cambiar_texto(datos, cols):
    for col in cols:
        datos[col] = datos[col].str.strip().str.replace('-', ' ').str.replace('_', ' ').str.capitalize()

def gestion_nulos(datos):
    datos['businesstravel'].replace('NaN', np.nan, inplace=True)
    datos['businesstravel'].fillna('Travel rarely', inplace=True)
    datos['dailyrate'].fillna(datos['dailyrate'].median(), inplace=True)
    datos['department'].replace('NaN', np.nan, inplace=True)
    datos['department'].fillna('Unknown', inplace=True)
    datos['hourlyrate'].fillna(datos['hourlyrate'].median(), inplace=True)
    datos['maritalstatus'].replace('NaN', np.nan, inplace=True)
    datos['maritalstatus'].fillna('Other', inplace=True)
    datos['overtime'].replace('NaN', np.nan, inplace=True)
    datos['overtime'].fillna('No', inplace=True)
    datos['performancerating'].fillna(0, inplace=True)
    datos['totalworkingyears'].fillna(datos['totalworkingyears'].median(), inplace=True)
    datos['worklifebalance'].fillna(datos['worklifebalance'].median(), inplace=True)

def crear_columna(datos):
    datos['id_encuesta'] = range(1, len(datos) + 1)

def guardar_archivo(datos):
    datos.to_csv('Datos/datos_empresa_final.csv')

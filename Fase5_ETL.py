# %%
import pandas as pd
import sys
import os
from src import Fase5_ETL_soporte as sp 

# %%
datos = sp.abrir_archivos()
print('Se ha cargado el archivo de datos 🆗')
print('='*80)

columnas_borrar = ['employeecount','Over18','SameAsMonthlyIncome', 'Salary', 'RoleDepartament', 'NUMBERCHILDREN','employeenumber','StandardHours','EducationField','YearsInCurrentRole', 'MonthlyIncome']
sp.borrar_colunas(datos, columnas_borrar)
print('Se han borrado las columnas no necesarias 🆗')
print('='*80)

sp.transformar_cabeceras(datos)
print('Se han modificado las cabeceras 🆗')
print('='*80)

sp.transformacion(datos)
print('Se ha realizado el proceso de transformación de las columnas que tenían casos únicos 🆗')
print('='*80)

datos['environmentsatisfaction'] = datos['environmentsatisfaction'].apply(sp.eliminar_segundo_digito)
print('Hemos borrado el segundo dígito de la columna environmentsatisfaction 🆗')
print('='*80)

cols_float = ['dailyrate', 'performancerating', 'totalworkingyears', 'worklifebalance']
sp.cambiar_float(datos, cols_float)
print('Hemos convertido a float las columnas necesarias 🆗')
print('='*80)

cols_int = ['age', 'distancefromhome', 'hourlyrate']
sp.cambiar_int(datos, cols_int)
print('Hemos convertido a int las columnas necesarias 🆗')
print('='*80)

cols_text = ['attrition', 'businesstravel', 'department', 'gender', 'jobrole', 'maritalstatus', 'overtime', 'remotework']
sp.cambiar_texto(datos, cols_text)
print('Hemos unificado el texto de las columnas 🆗')
print('='*80)

sp.gestion_nulos(datos)
print('Hemos realizado la gestión de nulos 🆗')
print('='*80)

sp.crear_columna(datos)
print('Hemos creado la columna idencuesta 🆗')
print('='*80)

sp.guardar_archivo(datos)
print('Hemos guardado el archivo final 🆗 ')
print('='*80)
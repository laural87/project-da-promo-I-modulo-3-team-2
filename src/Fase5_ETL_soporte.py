#%%
import pandas as pd
import sys
import os

#%%
def abrir_archivos():
    """
    Función para abrir el .csv final del proyecto"""
    df_final = pd.read_csv("Datos/datos_empresa_final.csv", index_col=0)
    
    return df_final
# %%

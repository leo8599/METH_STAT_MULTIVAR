# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:58:43 2022

@author: Andres
"""
import numpy as np
import pandas as pd
from scipy.stats import kurtosis, skew  # Asegúrate de importar kurtosis y skew desde scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

df = pd.read_excel ('C:/Users/USER/Desktop/Colima/Personas_06.xlsx')
df = df[df.EDAD != 999]
df = df[df.INGTRMEN != 999999]
df = df[df.INGTRMEN != 'nan']

pivot= pd.pivot_table(df, values=('EDAD'), index=('NOM_MUN'), columns=('SEXO'), aggfunc='mean', margins=True, margins_name='Total')
pivot2= pd.pivot_table(df, values=('INGTRMEN'), index=('NOM_MUN'), columns=('SEXO'), aggfunc='mean', margins=True, margins_name='Total')

# Calcular estadísticas descriptivas para EDAD
edad_stats = {
    'Suma': df['EDAD'].sum(),
    'Conteo': df['EDAD'].count(),
    'Media': df['EDAD'].mean(),
    'Varianza': df['EDAD'].var(),
    'Desviación Estándar': df['EDAD'].std(),
    'Curtosis': kurtosis(df['EDAD']),
    'Asimetría': skew(df['EDAD'])
}

# Calcular estadísticas descriptivas para INGTRMEN
ingreso_stats = {
    'Suma': df['INGTRMEN'].sum(),
    'Conteo': df['INGTRMEN'].count(),
    'Media': df['INGTRMEN'].mean(),
    'Varianza': df['INGTRMEN'].var(),
    'Desviación Estándar': df['INGTRMEN'].std(),
    'Curtosis': kurtosis(df['INGTRMEN']),
    'Asimetría': skew(df['INGTRMEN'])
}

# Mostrar las tablas dinámicas
print("\nTabla dinámica de EDAD por NOM_MUN y SEXO:")
print(pivot)
print("\nTabla dinámica de INGTRMEN por NOM_MUN y SEXO:")
print(pivot2)




df2 = df[['EDAD', 'SEXO', 'INGTRMEN']]

df2 = df2[df2.INGTRMEN >= 1700]

df2 = df2[df2.EDAD != 'nan']

df2['EDAD2'] = df2['EDAD'] * df2["EDAD"]


import statsmodels.api as sm           ## Este proporciona funciones para la estimación de muchos modelos estadísticos
import statsmodels.formula.api as smf  ## Permite ajustar modelos estadísticos utilizando fórmulas de estilo R

#crear diccionario
sexo1 = {"Hombres": 1 , "Mujeres": 0}

# Aplica la recodificación a la columna "SEXO".
df2['SEXO'] = df2['SEXO'].replace(3,0)

mod = smf.ols('INGTRMEN ~ EDAD + EDAD2 + SEXO', data=df2).fit()
print(mod.summary())


df2_m = df2[df2['SEXO'] == 3]

# Ajusta el modelo de regresión solo para las filas filtradas
mod = smf.ols('INGTRMEN ~ EDAD + EDAD2 + SEXO', data=df2_m).fit()

# Imprime el resumen del modelo
print(mod.summary())





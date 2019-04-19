#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:35:01 2018

@author: edwin
"""
### Este codigo toma todas las estaciones de una carpeta y las une por columnas
#####Preprocesamiento de hydras temperatura

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import plotly.plotly as py

#Directorio
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras')

#Lista de archivos

lista_estaciones = pd.DataFrame(list(os.listdir()))

lista_estaciones.columns = ['a']   #nombres
lista_estaciones.columns.values[0] = 'a'

lista_estaciones['cod'], lista_estaciones['year'], lista_estaciones['varr'] = lista_estaciones.a.str.split('_').str

lista_estaciones['variable'], lista_estaciones['csv']= lista_estaciones.varr.str.split('.').str

lista_estaciones_2 = lista_estaciones.iloc[:,[1,2,4]]

# =============================================================================
# 21206600 = Nueva generación Bogotá
# 21206990 = Tibaitatá
# 21206790 = Nemocón Hda Sta Ana 
# =============================================================================

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras')
#base1 = pd.read_csv('21206990_2007_0075.csv', header=None)


#Cargar la base de datos
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
vari_hydras = pd.read_csv('base_nombres.csv')
vari_hydras.convert_objects(convert_numeric=True)

# Función para arreglar cada csv y ponerlo en forma para ser usado
def ajuste_base(base):
    base.columns = ['cod', 'dat1', 'dat2', 'value', 'cod_var']
    base['date'] = base.dat1.astype(str) + '-' + base.dat2.astype(str)
    base.date = pd.to_datetime(base.date, format ='%Y%m%d-%H:%M:%S', errors='coerce')
    nombre_1 = vari_hydras[vari_hydras.variable.isin(base.cod_var)].titulo # Busca cual es el nombre de la variable
    base.columns.values[3] = nombre_1.iloc[0]
    base2 = base.iloc[:,[0,5,3]]
    base2 = base2.convert_objects(convert_numeric=True)
    return(base2)

lista_estaciones_3 = lista_estaciones_2.iloc[:,:].astype(str)

for i in list(lista_estaciones_3.cod.unique()):
#for i in list(pd.DataFrame(lista_estaciones_3.cod.unique()).iloc[61:78,0]):
    #print(i)
    c1 = pd.DataFrame({ 'cod' : [99999999, 99999991],
                           'date' : ([pd.to_datetime('1999-01-01 02:00:00'),
                                      pd.to_datetime('1999-01-01 03:00:00')]),})
    d1 = pd.DataFrame({ 'cod' : [99999999, 99999991],
                           'date' : ([pd.to_datetime('1999-01-01 02:00:00'),
                                      pd.to_datetime('1999-01-01 03:00:00')]),})
    for j in list(lista_estaciones_3.year.unique()):
        #print(j)
        a = np.NaN
        c = pd.DataFrame({ 'cod' : [99999999, 99999991],
                           'date' : ([pd.to_datetime('1999-01-01 02:00:00'), pd.to_datetime('1999-01-01 03:00:00')]),
                })
        for k in list(lista_estaciones_3.variable.unique()):
            acod = (i + '_' + str(j) + '_'+ k +'.csv')
            acod2 = lista_estaciones[lista_estaciones.a == acod]
            if len(lista_estaciones[lista_estaciones.a == acod]) > 0: # El condicional para la selección del archivo
                os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras')
                a = pd.read_csv(acod)
                b = ajuste_base(a)
                c = pd.merge(left = c, right = b, on=['cod', 'date'], how='outer')
                #os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3')
                if len(c.index) > 4:#Linea para evitar crear archivos pequeños
                    #c.iloc[2:,:].to_csv(i + '_' + j +'.csv')
                    d1 = c.iloc[2:,:]
        c1 = c1.append(d1, ignore_index=True)
        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3')
        c1.iloc[2:,:].to_csv(str(i) +'.csv')
            
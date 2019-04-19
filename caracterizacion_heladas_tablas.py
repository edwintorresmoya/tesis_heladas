#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:25:30 2019
script creado para realizar la caracterización de las heladas en forma de tablas
Las variables que se van a trabajar son: precipitación, humedad relativa, brillo solar y temperatura
@author: edwin
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspect
from datetime import datetime  
from datetime import timedelta
import matplotlib.dates as mdates



###############
def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)
#################

ini_f = pd.to_datetime(19990201, format ='%Y%m%d', errors='coerce')
fin_f = pd.to_datetime(20190206, format ='%Y%m%d', errors='coerce')

#HYDRAS 
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col1')
lista_total = pd.DataFrame({'nombres':os.listdir()})

tabla_1 = pd.DataFrame()

for var_i in ['tmp_2m','precip_1','hum_2m','val_rad']:
    #var_i = 'tmp_2m'
    print(var_i)
    lista_espe = lista_total[lista_total.nombres.str.contains(var_i)]
    for list_i in lista_espe.nombres:
        print(list_i)
        cod_1 = list_i[2:10]
        base_i = pd.read_csv(list_i)
        base = base_i[base_i[[col for col in base_i.columns if 'val_' in col]].iloc[:,0] == 0]
        base.date = pd.to_datetime(base.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
        base = base.sort_values('date')
        base = base.reset_index()
        
        # Condicional para que tome las fechas que existan
        if base.date.min() > ini_f:
            ini_f1 = base.date.min()
        else:
            ini_f1 = ini_f
        
        if base.date.max() < fin_f:
            fin_f1 = base.date.max() 
        else:
            fin_f1 = fin_f
        
        # Extracción de los datos a analizar
        base_1 = base[(base.date > ini_f1) | (base.date < fin_f1)]
        columna_1 = [col for col in base_1.columns if var_i in col]
        base_2 = base_1[[col for col in base_1.columns if var_i in col]]
        
        tabla_2 = pd.DataFrame([])
        tabla_2['cod'] = pd.DataFrame({'fec_ini':[cod_1]})
        tabla_2['var_1'] = pd.DataFrame({'fec_ini':[var_i]})
        tabla_2['fec_ini'] = pd.DataFrame({'fec_ini':[ini_f1]})
        tabla_2['fec_fin'] = pd.DataFrame({'fec_fin':[fin_f1]})
        tabla_2['max_1'] = pd.DataFrame({'fec_fin':[base_2[columna_1].max()[0]]})
        tabla_2['min_1'] = pd.DataFrame({'fec_fin':[base_2[columna_1].min()[0]]})
        tabla_2['mean_1'] = pd.DataFrame({'fec_fin':[base_2[columna_1].mean()[0]]})
        tabla_2['median_1'] = pd.DataFrame({'fec_fin':[base_2[columna_1].median()[0]]})
        tabla_2['std_1'] = pd.DataFrame({'fec_fin':[base_2[columna_1].std()[0]]})
        
        tabla_1 = tabla_1.append(tabla_2)
        
        


data = {'spike-2': [1,2,3], 'hey spke': [4,5,6], 'spiked-in': [7,8,9], 'no': [10,11,12]}
df = pd.DataFrame(data)

spike_cols = [col for col in df.columns if 'spike' in col]
print(list(df.columns))
print(spike_cols)   

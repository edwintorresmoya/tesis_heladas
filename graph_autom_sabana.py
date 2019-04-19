#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 14:03:00 2018

@author: edwin
"""

#Gráficas de temperaturas de las estaciones en la SAbana de Bogotá
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import style

def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)

#Ubicación de las estaciones automáticas de la sabana con la validación
path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_validado_20180522'

os.chdir(path)

for i in list(os.listdir()):
    print(i)
    
    base = pd.read_csv(i)
    base.date = pd.to_datetime(base.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    base_3 = base[base.tmp_2m.notnull()][base.range == 0][base.tmp_2mspikes == 0][base.tmp_2m_dif == 0][base.tmp_2m_roll_1 == 0]
    plt.plot_date(base_3.date, base_3.tmp_2m)
    #
    #inicio_1 = pd.to_datetime('2008/09/11 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
    #fin_1 = pd.to_datetime('2008/09/13 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
    
    ## Horas con heladas
    base_3
    n_f2 = pd.DatetimeIndex(base_3.date)
    base_4 = base_3
    base_4['hora'] = n_f2.hour
    base_4['val'] = 1
    base_4_sum = base_4[base_4.tmp_2m < 0].groupby(['hora'])['val'].sum()
    base_4_sum = base_4_sum.reset_index()
    
        #Gráfica de las horas en las que se presentan las heladas
    plt.bar(base_4_sum.hora, base_4_sum.val, color = 'royalblue')
    plt.xticks(range(0,24),range(0,24), rotation = 90)
    plt.ylabel('Frecuencia')
    
    plt.xlabel('Hora')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph/hora_heladas.png', figsize=(20,10) ,dpi = 199)
    plt.close()
    
    
    ## Horas con tmp_altas
    base_3
    n_f2 = pd.DatetimeIndex(base_3.date)
    base_4 = base_3
    base_4['hora'] = n_f2.hour
    base_4['val'] = 1
    base_4_sum = base_4[base_4.tmp_2m_y > 20].groupby(['hora'])['val'].sum()
    base_4_sum = base_4_sum.reset_index()
    
        #Gráfica de las horas en las que se presentan las heladas
    plt.bar(base_4_sum.hora, base_4_sum.val, color = 'lightcoral')
    plt.xticks(range(0,24),range(0,24), rotation = 90)
    plt.ylabel('Frecuencia')
    
    plt.xlabel('Hora')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph/hora_tmp_altas.png', figsize=(20,10) ,dpi = 199)
    plt.close()
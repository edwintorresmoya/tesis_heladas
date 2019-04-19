#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:34:31 2018
Creado para hacer las gráficas de la temperatura con la validación
@author: edwin
"""

################ Gráfica de la temperatura con y sin control
import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col')

lista_est = os.listdir()
            


#Usado para encontrar la lista de las temperaturas
lista_tmp = []
for ww in lista_est:
    if 'tmp_2m.csv' in ww:
        lista_tmp.append(ww)

for ii in lista_tmp:
    #print(ii)
    base_tmp = pd.read_csv(ii)
    base_tmp.date = pd.to_datetime(base_tmp.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    
    
    plt.plot_date(base_tmp[base_tmp.val_tmp == 1].date, base_tmp[base_tmp.val_tmp == 1].tmp_2m, color='gray')
    plt.xlabel('Año')
    plt.ylabel('Temperatura °C')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_temperatura/'+str(ii)[2:10]+'v.pdf' ,dpi = 100)
    plt.close()
    
    plt.plot_date(base_tmp[base_tmp.val_tmp == 0].date, base_tmp[base_tmp.val_tmp == 0].tmp_2m, color='gray')
    plt.xlabel('Año')
    plt.ylabel('Temperatura °C')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_temperatura/'+str(ii)[2:10]+'.pdf' ,dpi = 100)
    plt.close()

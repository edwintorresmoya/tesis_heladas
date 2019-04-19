#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:22:02 2018
Función creadad para realizar las gráficas de la validación del cielo ddespejado
@author: edwin
"""


import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


base_rad_2.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/' +'v_'+i+'_val_rad.csv')


os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
lista_rad = os.listdir()

lista_rad_2 = []
for uu in lista_rad:
    print(uu)
    if '_val_rad' in uu:
        lista_rad_2.append(uu)

##acá voy

#### Gráfica de la profe

for ll in lista_rad_2:
    #print(ll)
    base_rad_2 = pd.read_csv(ll)
    base_rad_2.date = pd.to_datetime(base_rad_2.date, format ='%Y-%m-%d %H:%M:%S', errors='coerce')
    inicio = pd.to_datetime('20070203', format ='%Y%m%d', errors='coerce')
    fin = pd.to_datetime('20070205', format ='%Y%m%d', errors='coerce')
    base_rad_g = base_rad_2[(base_rad_2.date > inicio) & (base_rad_2.date < fin)]
    
    
    plt.figure(figsize=((8,6)))
    plt.plot_date(base_rad_g[base_rad_g.val_rad == 0].date, base_rad_g[base_rad_g.val_rad == 0].rad_1, color='dimgray' )
    plt.plot_date(base_rad_g[base_rad_g.val_rad == 1].date, base_rad_g[base_rad_g.val_rad == 1].rad_1, color = 'dimgray', marker='^')
    plt.plot_date((base_rad_g.date), base_rad_g.sky_3, '-', color = 'k')
    plt.legend(['Validos','No-Validos','Límite'])
    plt.xticks(rotation=90)
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_radiacion/'+str(ll)[2:10]+'.png' ,dpi = 100)
    plt.close()

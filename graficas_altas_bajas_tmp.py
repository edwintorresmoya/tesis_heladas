#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 10:04:52 2018
Script usado para crear los plots de las fechas de interés; osea de altas y bajas temperaturas
@author: edwin
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
from funciones import busca_cod
from funciones import un_busca_cod



os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')

lista_archivos = os.listdir()

base_3 = pd.DataFrame({'list_2':lista_archivos})
base_3['cod'] = base_3.list_2.str[2:10]
base_3 = base_3.iloc[1:,:]
base_3.dtypes
base_3.cod = base_3.cod.convert_objects(convert_numeric=True)
base4 = busca_cod(base_3)



for oo, name_1, cod in zip(base4.list_2, base4.Nombre, base4.cod):
    print(oo)
    if 'tmp_2m.csv' in oo:
        
        estacion = pd.read_csv(oo)
        
        
        estacion[estacion.val_tmp == 0]
        
        
        estacion.date =  pd.to_datetime(estacion.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
        
        estacion = estacion.sort_values('date')
        
        estacio1 = estacion[estacion.val_tmp == 0]
        
        #31 de enero del 2007 hasta el 5 de febrero del 2007
        
        f_inicio = pd.to_datetime(20070131, format ='%Y%m%d', errors='coerce')
        f_final = pd.to_datetime(20070205, format ='%Y%m%d', errors='coerce')
        
        
        estacio2 = estacio1[(estacio1.date > f_inicio) & (estacio1.date < f_final)]
        
        if len(estacio2) < 10:
            continue
        
        
        fig1 = plt.figure()
        fig1.set_size_inches(10,7)
        ax1 = fig1.add_axes([0.1, 0.2, 0.8, 0.75])
        ax1.plot_date(estacio2.date, estacio2.tmp_2m, '-')
        ax1.tick_params(axis='x', labelrotation=90)
        ax1.set_ylabel('Temperatura °C',fontsize=24)
        ax1.legend()
        #ax1.set_title('Estación '+name_1,fontsize=25)
        ax1.axhline(y = 20, linewidth=2, color='firebrick', linestyle = '--')
        ax1.axhline(y = 25, linewidth=2, color='r', linestyle = '-.')
        ax1.axhline(y = 0, linewidth=2, color='b', linestyle = ':')
        fig1.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/grafica_altas_bajas/' + str(cod)+'.png', figsize=(1,1) ,dpi = 60)
        plt.close()


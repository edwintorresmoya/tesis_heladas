#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:34:31 2018
Script creado para hacer las gráficas de las estaciones con y sin validar.
@author: edwin
"""

################ Gráfica de la temperatura con y sin control
import matplotlib.pyplot as plt
import pandas as pd
import os
import pdb


os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col')

#lista_tmp = os.listdir()

lista_tmp = ['v_21206990_hum_2m.csv', 'v_21206990_precip_1.csv', 'v_21206990_tmp_2m.csv', 'v_21206990_val_dir.csv', 'v_21206990_val_rad.csv','v_21206990_vel_vi10.csv']

#base1 = pd.DataFrame({'col_1':lista_tmp})
#base2 = pd.DataFrame({'base_n':['hum_2m', 'precip_1', 'tmp_2m', 'val_dir', 'val_rad','vel_vi10'],
#    'variable':['Humedad %', 'Precipitación mm', 'Temperatura °C', 'Dirección °', 'Radiación W/$m^2$', 'Velocidad del viento m/s'],
#    'var_2':['hum_2m','precip_1','tmp_2m','dir_viento','rad_1', 'vel_vi10']})

base2 = pd.DataFrame({'base_n':['hum_2m', 'precip_1', 'tmp_2m', 'val_dir', 'val_rad','vel_vi10'],
    'variable':['Humidity %', 'Precipitation mm', 'Temperature °C', 'Direction °', 'Radiation W/$m^2$', 'Wind speed m/s'],
    'var_2':['hum_2m','precip_1','tmp_2m','dir_viento','rad_1', 'vel_vi10']})
#Usado para encontrar la lista de las temperaturas
for ii in lista_tmp:
    base_tmp = pd.read_csv(ii)
    base_tmp.date = pd.to_datetime(base_tmp.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

    # creado para buscar el nombre de las bases de datos
    for col_1, col_2, col_3 in zip(base2.base_n, base2.variable, base2.var_2):
        if ii[11:-4] in col_1:
            nombre = col_2
            nombre2 = col_3

    for jj in base_tmp.columns.values:
        print(jj)
        if 'val' in jj:
            columna = jj
    
#    pdb.set_trace()
    plt.plot_date(base_tmp[base_tmp[columna] == 1].date, base_tmp[base_tmp[columna] == 1][nombre2], color='gray')
    plt.xlabel('Año')
    plt.ylabel(nombre)
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_estaciones_validadas/'+str(ii)[2:10]+ii[11:-4]+'v.png' ,dpi = 100)
    plt.close()
    
    plt.plot_date(base_tmp[base_tmp[columna] == 0].date, base_tmp[base_tmp[columna] == 0][nombre2], color='gray')
    plt.xlabel('Año')
    plt.ylabel(nombre)
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_estaciones_validadas/'+str(ii)[2:10]+ii[11:-4]+'.png' ,dpi = 100)
    plt.close()

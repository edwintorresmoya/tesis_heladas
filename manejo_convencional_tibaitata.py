#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:52:22 2018
Scrip creado para trabajar con los datos de la estación convencional de Tibaitatá para hacer la búsqueda de las heladas
@author: edwin
"""

import pandas as pd 
import os
import matplotlib.pyplot as plt

b_conv = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_corpoica/union_t.csv')


# temperaturas bajas
b_conv[b_conv.min_2m < 0]


b_conv[b_conv.min_2m < 0]['min_2m'].corr(b_conv[b_conv.min_2m < 0]['min_2m'])
b_conv[b_conv.min_2m < 0]['min_2m']
b_conv[b_conv.min_2m < 0]['min_2m']

plt.plot(b_conv[b_conv.min_2m < 0]['min_2m'], b_conv[b_conv.min_2m < 0]['min_5cm'], '*')
plt.plot(b_conv[b_conv.min_2m < 0]['min_2m'], b_conv[b_conv.min_2m < 0]['min_50cm'], '*')
plt.plot(b_conv[b_conv.min_2m < 0]['min_2m'], b_conv[b_conv.min_2m < 0]['min_1m'], '*')

b_conv[['min_5cm', 'min_50cm','min_1m','min_2m',]]

x = range(-8, 10)

base_altura = pd.DataFrame({'altura':[0.05, 0.5, 1, 2]})

b_conv = b_conv.sort_values(['Año','Mes','dia']).reset_index()

for yy in range(20, 50):
    
    
    plt.plot(b_conv[['min_5cm', 'min_50cm','min_1m','min_2m',]].iloc[yy,:], base_altura, color = 'gray')
    plt.axvline(0, color = 'k', linestyle = '--')
    plt.xticks(x)
    plt.xlabel('Temperatura °C')
    plt.ylabel('Altura m')
    plt.title(str(b_conv[['Año',]].iloc[yy,:][0])+'-'+ str(b_conv[['Mes',]].iloc[yy,:][0]) + '-'+str(b_conv[['dia',]].iloc[yy,:][0])[-4:-2]+'.png')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_1/perfil_tmp/' + str(b_conv[['Año',]].iloc[yy,:][0])+'-'+ str(b_conv[['Mes',]].iloc[yy,:][0]) + '-'+str(b_conv[['dia',]].iloc[yy,:][0])[-4:-2]+'.png', figsize=(20,10) ,dpi = 199)
    #plt.show()
    plt.close()
    

for yy in range(0, 30):
    
    
    plt.plot(b_conv[['min_5cm', 'min_50cm','min_1m','min_2m',]].iloc[yy,:], base_altura, color = 'gray')
    plt.axvline(0, color = 'k', linestyle = '--')
    plt.xticks(x)
    plt.xlabel('Temperatura °C')
    plt.ylabel('Altura m')
    plt.title(str(b_conv[['Año',]].iloc[yy,:][0])+ str(b_conv[['Mes',]].iloc[yy,:][0]) + str(b_conv[['dia',]].iloc[yy,:][0])+'.png')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_1/perfil_tmp_1/' + str(b_conv[['Año',]].iloc[yy,:][0])+'-'+ str(b_conv[['Mes',]].iloc[yy,:][0]) + '-'+str(b_conv[['dia',]].iloc[yy,:][0])[-4:-2]+'.png', figsize=(20,10) ,dpi = 199)
    #plt.show()
    plt.close()
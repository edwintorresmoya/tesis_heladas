#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:22:13 2019
Script creado para realizar las gráficas de comparación de los las estaciones y
las diferentes salidas del WRF
@author: edwin
"""


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pdb

def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)
        

    


#for pp in ['200702', '201408', '201508', '201509', '201602', '201712']:
for pp in ['201602', '201712']:
    print(pp)

    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_'+pp) # se para en la carpeta
    
    archivos = pd.DataFrame({'col':os.listdir()})
    archivos = archivos[archivos.col.str.contains('csv')]
    
    for j in archivos.col:#[21206990.0]:#
        print(j)
        
        comparacion = pd.read_csv(j)
        if len(comparacion) < 5:
            continue
        comparacion.date = pd.to_datetime(comparacion.date)
        lista_col = []
        
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.235, 0.6, 0.75])
        for i in ['ideam-colombia', 'ideam-icm_3', 'ideam-icm']:
            
            lista_col.append('tmp_2m')

            for kk in ['d01','d02']:
                print(j[:-4] + '_'+i+'_'+kk)
                col_pos = j[:-4] + '_'+i+'_'+kk

                if pp == '201408':
                    col_pos = j[:-4] + '_s-'+i+'_'+kk


                if i == 'ideam-colombia':
                    type_1 = '-.'
                    color_1 = 'gray'
                    if kk == 'd02':
                        marker_1 = 'p'
                    else:
                        marker_1 = "^"
                    label_1 = 'ideam-colombia'

                if i == 'ideam-icm_3':
                    type_1 = '--'
                    color_1 = 'midnightblue'
                    if kk == 'd02':
                        marker_1 = 'p'
                    else:
                        marker_1 = "^"
                    label_1 = 'icm-mp_physics 3'
                
                if i == 'ideam-icm':
                    type_1 = '--'
                    color_1 = 'darkorange'
                    if kk == 'd02':
                        marker_1 = 'p'
                    else:
                        marker_1 = "^"
                    label_1 = 'icm'
                
                
                ax.plot_date(comparacion.date, comparacion[col_pos], color = color_1, linestyle = '-', marker = marker_1, label =label_1+' '+kk)

                
                
                
    
    
        
        ax.plot_date(comparacion.date, comparacion.tmp_2m, '-', color = 'k', label = 'Estación automática')
        
        ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size':6})## esto es para sacar la legenda de la gráfica
        ax.set_xlabel('Fecha - Hora')
        ax.set_ylabel('Temperatura °C') 
        #fig.autofmt_xdate()
        plt.xticks(rotation=90)
        #ax.set_xticklabels(labelrotation=90)
        fig.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/comparacion_grafica/'+pp+'_'+str(j)[:-4]+'.png' ,dpi = 100, figsize=(20,20))
        plt.close()




#
#        comparacion[lista_col]
#                
#        plt.plot_date(comparacion.date, comparacion.tmp_2m, '-', color = 'k', label = 'Estación automática')
#
#        plt.plot_date(comparacion.date, comparacion.T2, color = color_1, linestyle = '-', marker = marker_1, label =label_1+' '+kk)

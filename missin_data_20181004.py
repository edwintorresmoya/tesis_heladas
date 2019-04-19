#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:22:37 2018

@author: edwin
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:19:11 2018

@author: edwin
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
#import plotly.plotly as py
import matplotlib.gridspec as gridspect
#import datetime

###############
def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)
#################

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam'

os.chdir(path) # Cambia de directorio
os.getcwd() # Determina donde estoy

os.listdir() # lista de los archivos dentro de la carpeta

#ideam_rs_3 = pd.read_pickle('union_6.pickle')

est_zon = [21206190,21206200,21206210,21206220,21206230,21206240,21206250,21206260,21206280,21206450,21206490,21206500,21206510,21206540,21206550,21206560,21206570,21206610,21206620,21206630,21206640,21206650,21206660,21206670,21206680,21206690,21206700,21206970,21200160,21200620,21201050,21201080,21201140,21201160,21201210,21201230,21201240,21201250,21201270,21201550,21201570,21201600,21201610,21201620,21201630,21201650,21202100,21202280,21205013,21205230,21205420,21205520,21205580,21205600,21205700,21205710,21205720,21205730,21205740,21205750,21205760,21205770,21205780,35020320,21205790,35020330,21205800,21205810,35025050,21205820,35025060,21205830,21205840,21205850,21205860,21205870,21205880,21205890,21205900,21205910,21205920,21205930,35027220,21205940,21205950,21205960,21205970,21205980,21205990,21206000,21206010,21206020,21206030,21206040,21206050,21206060,21206150,21206170,21205528,21205529,21206130] # Estas estaciones corresponden al shp llamado Estaciones IDEAM, pero no incluye las ATU ní AUS

#ideam_rs_3_nona = ideam_rs_3[ideam_rs_3.TS.notnull()]
#ideam_rs_3_nona.to_csv('ideam_zona_nonan.csv')

ideam_rs_3_nona = pd.read_csv('ideam_zona_nonan.csv')
ideam_rs_3_nona.date = pd.to_datetime(ideam_rs_3_nona.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

###Limit test
ideam_rs_3_nona[(ideam_rs_3_nona.TS < -30) & (ideam_rs_3_nona.TS > 50)]
ideam_rs_3_nona.TS.max()
ideam_rs_3_nona.TS.min()


os.getcwd() # Determina donde estoy

ideam_con = pd.DataFrame({'indice':[1,2,3,4,5,7,8,9],
                              'Nombres':['Valores_medios', 'Máximos_absolutos', 
                                         'Mínimos_absolutos', 'Totales', 
                                         'Número_de_dia_con_lluvia',
                                         'Máximos_medios', 'Mínmos_medios',
                                         'Máxima_en_24 horas']
            })
    

for j in est_zon:
#j = 21206190
    estacion = ideam_rs_3_nona[ideam_rs_3_nona.cod == j]
    if len(estacion) > 10:
        
        #estacion = estacion.sort_values(by='date')
        
        valores = estacion.tipo.unique()
        
        #==============================================================================
        # Según el IDEAM:
        #     
        #     1 Valores medios
        #     2 Máximos absolutos
        #     3 Mínimos absolutos
        #     4 Totales
        #     5 Número de dia con lluvia
        #     7 Máximos medios
        #     8 Mínmos medios
        #     9 Máxima en 24 horas
        #==============================================================================
        min_est = estacion.date.min()
        max_est = estacion.date.max()
        
        
        
        fecha_na = pd.DataFrame({'date': np.arange(np.datetime64(min_est.strftime("%Y-%m-%d")),
                                    np.datetime64(max_est.strftime("%Y-%m-%d")))})
        
        for i in valores:
            #i = 2
            print(i);print(j)
            estacion_2 = estacion[estacion.tipo == i] # Filtra por tipo, máximo, mínimo, etc
            
            #hist_1 = estacion_2.date.dt.year.hist() # Histograma de los datos existentes de la estación valores medios
            estacion_na = pd.merge(left=estacion_2, right=fecha_na, on='date', how='outer')
            estacion_na = estacion_na.sort_values(by='date')
            estacion_na['data'] = np.where(estacion_na.TS.notnull(), 1, 0)
            estacion_na['missin_data'] = np.where(estacion_na.TS.notnull(), 0, 1)
            estacion_na['sum'] = estacion_na['data'] + estacion_na['missin_data']
            estacion_na['mean_1'] = estacion_na.TS.rolling(window=9, center=True, min_periods=1).mean()
            estacion_na['std_1'] = estacion_na.TS.rolling(window=9, center=True).std()
            estacion_na['std_2'] = estacion_na.TS.rolling(window=9, center=True, min_periods=1).std()
            
            #Plot de los NA anuales = 1
            stackplot_1 = estacion_na.groupby(estacion_na.date.dt.year).sum()[['data', 'missin_data', 'sum']]
            
            plt.stackplot(stackplot_1.index, stackplot_1.data, stackplot_1.missin_data,
                          colors = ['gray','silver'],
                          labels = ['Datos', 'No-datos'])
            plt.xlabel('año')
            plt.ylabel('Frecuencia')
            plt.legend()
            
            plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/graficas_nan/'+str(j)+'_'+str(ideam_con[ideam_con.indice == i].iloc[0][1])+'_1'+'.png', figsize=(20,10) ,dpi = 199)
            plt.close()
            
            
            ###
            #Plot de los NA de los meses = 2
            
            stackplot_2 = estacion_na.groupby(estacion_na.date.dt.month).sum()[['data', 'missin_data', 'sum']]
            
            plt.stackplot(stackplot_2.index, stackplot_2.data, stackplot_2.missin_data,
                          colors = ['gray','silver'],
                          labels = ['Datos', 'No-datos'])
            plt.xlabel('mes')
            plt.ylabel('Frecuencia')
            plt.xticks(np.arange(1,13))
            plt.legend()
            
            plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/graficas_nan/'+str(j)+'_'+str(ideam_con[ideam_con.indice == i].iloc[0][1])+'_2'+'.png', figsize=(20,10) ,dpi = 199)
            plt.close()
            
            
            
            
            
            
            #Plot de las discontinuidades
            
                    
            
            estacion_na['std'] = estacion_na.TS.rolling(window= 11).std()
            estacion_na['std_2'] = estacion_na.TS.rolling(window= 11, min_periods = 1).std()
            
            #####Validación de los datos
            #2 Spikes
            
            
            estacion_na['spikes_connan'] = np.where((((estacion_na.mean_1 - (estacion_na.std_2 * 2.5)) < 
              estacion_na.TS) & (estacion_na.TS < (estacion_na.mean_1 + 
                            (estacion_na.std_2 * 2.5)))), 0,1)
            #Es una linea que llama spikes a aquella fila de temperatura que su valor es superior a el promedio +o- la desviación estándard.
             
            estacion_na['spikes'] = np.where(((estacion_na.spikes_connan == 1) & 
                       (estacion_na.missin_data == 0) & 
                       (~estacion_na.std_2.isnull()) & 
                       (estacion_na.std_2 != 0)),1,0) ### Ojo revisar

            # Este condicional dice que si es True, implica que el valor pasa, pero los valores con Falso pueden ser varias cosas una de ellas es que el valor sea NaN
            ### Ojo porque puede que la desviación estándard y el promedio sean iguales por la ausencia de datos
            
            #3 Discontinuity
            
            estacion_na['discont'] = np.where(estacion_na.TS.rolling(window=(11)).std() >
                       (estacion_na.TS.rolling(window=(11)).std().std() +
                        estacion_na.TS.rolling(window=(11)).std().mean()), 1, 0) ####revisar

            #Guardar los valores
            #estacion_na.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/convencionales_validados/datos/'+str(j)+'_'+ideam_con[ideam_con.indice == i].iloc[0][0]+'_val.csv')
        
            
            stackplot_3 = estacion_na.groupby(estacion_na.date.dt.month).sum()[['data', 'spikes', 'discont']]

            stackplot_4 = estacion_na.groupby(estacion_na.date.dt.year).sum()[['data', 'spikes', 'discont']]
            
            #Plots de los saltos = 3 anuales
            
            plt.stackplot(stackplot_4.index, stackplot_4.spikes,
                          colors = ['gray'],
                          labels = ['Saltos'])
            
            
            plt.xlabel('año')
            plt.ylabel('Frecuencia')
            plt.legend()
            
            plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/graficas_nan/'+str(j)+'_'+str(ideam_con[ideam_con.indice == i].iloc[0][1])+'_3'+'.png', figsize=(20,10) ,dpi = 199)
            plt.close()
            
            
            #Plots de los saltos = 4 mensuales
            
            plt.stackplot(stackplot_3.index, stackplot_3.spikes,
                          colors = ['gray'],
                          labels = ['Saltos'])
            
            
            plt.xlabel('mes')
            plt.ylabel('Frecuencia')
            plt.xticks(np.arange(1,13))
            plt.legend()
            
            plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/graficas_nan/'+str(j)+'_'+str(ideam_con[ideam_con.indice == i].iloc[0][1])+'_4'+'.png', figsize=(20,10) ,dpi = 199)
            plt.close()
            

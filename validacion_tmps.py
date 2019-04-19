#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:57:54 2018

@author: edwin
"""

### Validación de todos los datos de temperatura Hydras


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspect




os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005')
lista_estaciones_2 = pd.DataFrame(list(os.listdir()))

lista_estaciones2 = lista_estaciones_2

lista_estaciones2.columns = ['a']
#lista_estaciones2.columns.values[0] = 'a'

lista_estaciones2['cod'], lista_estaciones2['csv'] = lista_estaciones2.a.str.split('.').str
lista_9 = pd.DataFrame({'aa':['cod;tipo;median']})


def horas(valor): # Función usada para que las horas no sobrepasen las 23 horas porque si dan 24 horas habrá problemas
    if(valor < 23):
        aa = (valor+1)
        return(aa)
    else:
        aa = 23
        return(aa)
        


for l in list(lista_estaciones_2.a):
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005')
    ibase = pd.read_csv(l)
    ibase.date = pd.to_datetime(ibase.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    ibase = ibase.sort_values(by='date', ascending=True)
    
    col_tmp = [col for col in ibase.columns if 'tmp' in col] # Selección de las columnas que tengan esa variable
    # =============================================================================
    # col_tmp2 = pd.DataFrame([col for col in ibase.columns if 'tmp' in col])
    # col_tmp2.columns = ['a']
    # col_tmp2[0]
    # col_tmp2['b'] = col_tmp2.a + '_rango'
    # =============================================================================
    if len(col_tmp) > 0:
        for i in col_tmp:
            
            
                        
            #### Hay muchos valores con NaN además no tiene orden cronológico
            ibase2 = ibase[ibase[i].notnull()].sort_values(by='date', ascending=True)
            ibase3 = ibase2
            min_1 = ibase3[ibase3.date.min() == ibase3.date].date
            min_2 = pd.to_datetime(str(min_1.dt.year.iloc[0]) +'-'+str(min_1.dt.month.iloc[0]
                    ) +'-'+str(min_1.dt.day.iloc[0]) +' '+str(min_1.dt.hour.iloc[0]) + ':00')
            
            max_1 = ibase3[ibase3.date.max() == ibase3.date].date
            
            max_2 = pd.to_datetime(str(max_1.dt.year.iloc[0]) +'-'+str(max_1.dt.month.iloc[0]
                    ) +'-'+str(max_1.dt.day.iloc[0]) +' '+(str(horas(max_1.dt.hour.iloc[0]))) + ':00')
            
            #Se crean los valores de NA para poder determinar cuántos NA existen
            fecha_na = pd.DataFrame({'date': np.arange(np.datetime64(min_2.strftime("%Y-%m-%d %H")),
                                                       np.datetime64(max_2.strftime("%Y-%m-%d %H")))})
    
            ibase4 = pd.merge(left=ibase3[['date', i]], right=fecha_na, on='date', how='outer')
            ibase4 = ibase4.sort_values(by='date')
            ibase4['data'] = np.where(ibase4[i].notnull(), 1, 0)
            ibase4['missin_data'] = np.where(ibase4[i].notnull(), 0, 1)
            ibase4['sum'] = ibase4['data'] + ibase4['missin_data']
            ibase4['mean_1'] = ibase4[i].rolling(window=9, center=True, min_periods=1).mean()
            ibase4['std_1'] = ibase4[i].rolling(window=9, center=True).std()
            ibase4['std_2'] = ibase4[i].rolling(window=9, center=True, min_periods=1).std()
            
            #Primera prueba en donde los valores fuera de -30 y superiores a 50 no serán escogidos
            ibase4['range_1'] = np.where(((-30 < ibase4[i]) & (ibase4[i] < 50)), 0, 1)
            ibase4['range'] = np.where(((ibase4.range_1 == 1) & 
                       (ibase4.missin_data == 0)), 1, 0)  # Sea un valor, no sea un NaN
                       #(~ibase4.std_2.isnull()) & 
                       #(ibase4.std_2 == 0)),1,0)
            
            
            ibase4['spikes_connan'] = np.where((((ibase4.mean_1 - (ibase4.std_2 * 2.5)) > 
                                      ibase4[i]) | (ibase4[i] > (ibase4.mean_1 + 
                                        (ibase4.std_2 * 2.5)))), 1,0)
            
            ####Spikes
            ibase4[i+'spikes'] = np.where(((ibase4.spikes_connan == 1) & 
                          # Sea un valor, no sea un NaN
                       (ibase4.missin_data == 0) & 
                       #que la desviación estándar no sea Na
                       (~ibase4.std_2.isnull()) & 
                       # Que la desviación  estándar no sea 0
                       (ibase4.std_2 != 0)),1,0) 
            
            ####Lapsos
            #Saber si los lapsos de tiempo entre valores no supera los 4°C
            ibase4[i+'_dif_1'] = np.where((abs(ibase4[i] - ibase4[i].shift(1)) < 4), 0, 1) # Se adicionó el valor absoluto
            
            ibase4[i+'_dif'] = np.where(((ibase4[i+'_dif_1'] == 1) & ((ibase4.missin_data == 0)) & (~ibase4.std_2.isnull()) & (ibase4.std_2 != 0)),1,0)
            
            ####Desviación estándar
            # Si la desviación estándar es menor a 0.001 para 5 valores quiere decir que el sensor se pegó
            ibase4[i+'_roll_1'] = np.where(((ibase4[i].rolling(window = 10, center = True).std()) > 0.01), 1,0)
            ibase4[i+'_roll'] = np.where(((ibase4[i+'_roll_1'] == 1) & ((ibase4.missin_data == 0)) & (~ibase4.std_2.isnull()) & (ibase4.std_2 != 0)),1,0)
            
            
            #Resúmenes de los datos por año, mes, hora MISSING DATA
            stackplot_1 = ibase4.groupby(ibase4.date.dt.year).sum()[['data', 'missin_data', 'sum']]
            stackplot_2 = ibase4.groupby(ibase4.date.dt.month).sum()[['data', 'missin_data', 'sum']]
            stackplot_3 = ibase4.groupby(ibase4.date.dt.hour).sum()[['data', 'missin_data', 'sum']]
            
            #Resúmenes de los datos por año, mes, hora SPIKES LAPSOS STD
            stackplot_4 = ibase4.groupby(ibase4.date.dt.year).sum()[[i+'spikes', i+'_dif', i+'_roll']]
            stackplot_5 = ibase4.groupby(ibase4.date.dt.month).sum()[[i+'spikes', i+'_dif', i+'_roll']]
            stackplot_6 = ibase4.groupby(ibase4.date.dt.hour).sum()[[i+'spikes', i+'_dif', i+'_roll']]
            
            #Resumen de los datos fuera de rango
            
            stackplot_7 = ibase4.groupby(ibase4.date.dt.year).sum()[['range']]
            stackplot_8 = ibase4.groupby(ibase4.date.dt.month).sum()[['range']]
            stackplot_9 = ibase4.groupby(ibase4.date.dt.hour).sum()[['range']]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            #######
            ###GRÁFICAS
            ######
            
            ##########MISSING DATA
            
            fig = plt.figure(1)
            fig.set_size_inches(20,10)
            fig.suptitle(str(lista_estaciones_2[lista_estaciones_2.a == l].cod.iloc[0]) +'_'+ i )
            
            
            gridspect.GridSpec(4,2)
            
                        
            #Plot de los años
            plt.subplot2grid((4,2), (0,0), rowspan=1, colspan=1)
            plt.stackplot(stackplot_1.index, stackplot_1.data, stackplot_1.missin_data,
                          colors = ['m','c'],
                          labels = ['Datos', 'No-datos'])
            
            plt.xlabel('año')
            plt.ylabel('Frecuencia')
            plt.legend()
            
            #Plot de los meses
            plt.subplot2grid((4,2), (1,0), rowspan=1, colspan=1)
            plt.stackplot(stackplot_2.index, stackplot_2.data, stackplot_2.missin_data,
                          colors = ['m','c'],
                          labels = ['Datos', 'No-datos'])
            plt.xlabel('mes')
            plt.ylabel('Frecuencia')
            plt.xticks(np.arange(1,13))
            plt.legend()
            
            #Plot de las horas
            plt.subplot2grid((4,2), (2,0), rowspan=1, colspan=1)
            plt.stackplot(stackplot_3.index, stackplot_3.data, stackplot_3.missin_data,
                          colors = ['m','c'],
                          labels = ['Datos', 'No-datos'])
            plt.xlabel('hora')
            plt.ylabel('Frecuencia')
            plt.xticks(np.arange(0,24))
            plt.legend()
            
            
           
            
            #SPIKES-DIFERENCIAS-DESVIACIONES ESTANDAR
            
                        #Plot de los años
            plt.subplot2grid((4,2), (0,1), rowspan=1, colspan=1)
            plt.stackplot(stackplot_4.index, stackplot_4[i+'spikes'], stackplot_4[i+'_dif'], stackplot_4[i+'_roll'],
                          colors = ['r','y', 'lightsalmon'],
                          labels = ['Spikes', 'Diferencia', 'Pegado'])
            
            plt.xlabel('año')
            plt.ylabel('Frecuencia')
            plt.legend()
            
            #Plot de los meses
            plt.subplot2grid((4,2), (1,1), rowspan=1, colspan=1)
            plt.stackplot(stackplot_5.index, stackplot_5[i+'spikes'], stackplot_5[i+'_dif'], stackplot_5[i+'_roll'],
                          colors = ['r','y', 'lightsalmon'],
                          labels = ['Spikes', 'Diferencia', 'Pegado'])
            plt.xlabel('mes')
            plt.ylabel('Frecuencia')
            plt.xticks(np.arange(1,13))
            plt.legend()
            
            #Plot de las horas
            plt.subplot2grid((4,2), (2,1), rowspan=1, colspan=1)
            plt.stackplot(stackplot_6.index, stackplot_6[i+'spikes'], stackplot_6[i+'_dif'], stackplot_6[i+'_roll'],
                          colors = ['r','y', 'lightsalmon'],
                          labels = ['Spikes', 'Diferencia', 'Pegado'])
            plt.xlabel('hora')
            plt.ylabel('Frecuencia')
            plt.xticks(np.arange(0,24))
            plt.legend()
            
            
            
            
            ##VALORES FUERA DE RANGO
            
            #Plot de los valores fuera del rango
            plt.subplot2grid((4,2), (3,0), rowspan=1, colspan=2)
            plt.plot_date(x=ibase4.date, y=ibase4[i])
            plt.plot_date(x=ibase4.date, y=np.where((ibase4.range == 1), 1, np.NaN))
            plt.xlabel('año')
            plt.ylabel('Temperatura')
            plt.legend()
            
            path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005_grap'

            os.chdir(path)
            plt.savefig(str(lista_estaciones_2[lista_estaciones_2.a == l].cod.iloc[0]) +'_'+ i + '.png', figsize=(20,10) ,dpi = 199)
            plt.close()
            
            
            
            ###Rango -----------
            
            fig = plt.figure(1)
            fig.set_size_inches(20,10)
            fig.suptitle(str(lista_estaciones_2[lista_estaciones_2.a == l].cod.iloc[0]) +'_'+ i )
            
            
            gridspect.GridSpec(4,1)
            
                                    
            
            #Plot de los años
            plt.subplot2grid((4,1), (0,0), rowspan=1, colspan=2)
            plt.stackplot(stackplot_7.index, stackplot_7['range'],
                          colors = ['r'],
                          labels = ['Rango'])
            
            plt.xlabel('año')
            plt.ylabel('Frecuencia')
            plt.legend()
            
            #Plot de los meses
            plt.subplot2grid((4,1), (1,0), rowspan=1, colspan=2)
            plt.stackplot(stackplot_8.index, stackplot_8['range'],
                          colors = ['r'],
                          labels = ['Rango'])
            plt.xlabel('mes')
            plt.ylabel('Frecuencia')
            plt.xticks(np.arange(1,13))
            plt.legend()
            
            #Plot de las horas
            plt.subplot2grid((4,1), (2,0), rowspan=1, colspan=2)
            plt.stackplot(stackplot_9.index, stackplot_9['range'],
                          colors = ['r'],
                          labels = ['Rango'])
            plt.xlabel('hora')
            plt.ylabel('Frecuencia')
            plt.xticks(np.arange(0,24))
            plt.legend()
            
            #Datos limpios
            
            plt.subplot2grid((4,1), (3,0), rowspan=1, colspan=2)
            plt.plot_date(x=ibase4[ibase4.range == 0].date, y=ibase4[ibase4.range == 0][i])
            plt.xlabel('año')
            plt.ylabel('temperatura')
            plt.legend()
            
            path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005_grap'

            os.chdir(path)
            plt.savefig(str(lista_estaciones_2[lista_estaciones_2.a == l].cod.iloc[0]) +'_'+ i + '_r.png', figsize=(20,10) ,dpi = 199)
            plt.close()
            
            
            
            
            
            ibase = pd.merge(left = ibase, right = ibase4, on=['date'], how='outer')
            os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005_data')
            ibase4.to_csv(str(lista_estaciones_2[lista_estaciones_2.a == l].cod.iloc[0]) +'_'+ i + '.csv')
            
            ibase4 = np.NaN
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 09:20:11 2018

@author: edwin
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:52:46 2018

@author: edwin
"""

#Comparación entre hydras y automáticas
#Comparación entre hydras y automáticas
#Comparación entre hydras y automáticas

import pandas as pd
import os
import matplotlib.pyplot as plt




###############
def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)
#################

#HYDRAS 
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005')

hyd_tiba = pd.read_csv('21206990.csv')
hyd_tiba.date = pd.to_datetime(hyd_tiba .date, format ='%Y%m%d %H:%M:%S', errors='coerce')

#Convencionales


path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam'

os.chdir(path) # Cambia de directorio

#ideam_rs_3 = pd.read_pickle('union_6.pickle') #Estos es la base original

#ideam_rs_3_nona = ideam_rs_3[ideam_rs_3.TS.notnull()] # Este se usó para sacar todos los datos que no tengan valor en la casilla de la temperatua
#ideam_rs_3_nona.to_csv('ideam_zona_nonan.csv') #

#ideam_rs_3_nona = pd.read_csv('ideam_zona_nonan.csv')
#ideam_rs_3_nona.date = pd.to_datetime(ideam_rs_3_nona.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

#conv_tiba = ideam_rs_3_nona[ideam_rs_3_nona.cod == 21205420]
#conv_tiba.to_csv('conv_tiba.csv')
conv_tiba = pd.read_csv('conv_tiba.csv')
conv_tiba.date = pd.to_datetime(conv_tiba.date, format ='%Y%m%d %H:%M:%S', errors='coerce')


##

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

def gra_tiem(inicio, final, salida):
    

    conv_tiba.tipo.unique() # tipo 1, 2, 8
    
    conv_tiba_min = conv_tiba[conv_tiba.tipo == 8]
    conv_tiba_min = conv_tiba_min.sort_values('date')
    
    conv_tiba_max= conv_tiba[conv_tiba.tipo == 1]
    conv_tiba_max = conv_tiba_max.sort_values('date')
    
    conv_tiba_mean = conv_tiba[conv_tiba.tipo == 2]
    conv_tiba_mean = conv_tiba_mean.sort_values('date')
   
    
    min_rang_1 = hyd_tiba[hyd_tiba.date == max(hyd_tiba[((hyd_tiba.date <= pd.to_datetime(inicio + ' 0:0:0',
                                                format ='%Y%m%d %H:%M:%S', errors='coerce')))].date)].index[0]
    
    max_rang_1 = hyd_tiba[hyd_tiba.date == min(hyd_tiba[((hyd_tiba.date >= pd.to_datetime(final + ' 0:0:0',
                                                format ='%Y%m%d %H:%M:%S', errors='coerce')))].date)].index[0]

  
    
    #Gráfica de solo convencional
    
    min_min = conv_tiba_min.index.get_loc(conv_tiba_min[conv_tiba_min.date == max(conv_tiba_min[conv_tiba_min.date <= pd.to_datetime(inicio + ' 0:0:0',format ='%Y%m%d %H:%M:%S', errors='coerce')].date)].index[0])
    max_min = conv_tiba_min.index.get_loc(conv_tiba_min[conv_tiba_min.date == min(conv_tiba_min[conv_tiba_min.date >= pd.to_datetime(final + ' 0:0:0',format ='%Y%m%d %H:%M:%S', errors='coerce')].date)].index[0])
    
    min_max = conv_tiba_max.index.get_loc(conv_tiba_max[conv_tiba_max.date == max(conv_tiba_max[conv_tiba_max.date <= pd.to_datetime(inicio + ' 0:0:0',format ='%Y%m%d %H:%M:%S', errors='coerce')].date)].index[0])
    max_max = conv_tiba_max.index.get_loc(conv_tiba_max[conv_tiba_max.date == min(conv_tiba_max[conv_tiba_max.date >= pd.to_datetime(final + ' 0:0:0',format ='%Y%m%d %H:%M:%S', errors='coerce')].date)].index[0])
    
    min_mean = conv_tiba_mean.index.get_loc(conv_tiba_mean[conv_tiba_mean.date == max(conv_tiba_mean[conv_tiba_mean.date <= pd.to_datetime(inicio + ' 0:0:0',format ='%Y%m%d %H:%M:%S', errors='coerce')].date)].index[0])
    max_mean = conv_tiba_mean.index.get_loc(conv_tiba_mean[conv_tiba_mean.date == min(conv_tiba_mean[conv_tiba_mean.date >= pd.to_datetime(final + ' 0:0:0',format ='%Y%m%d %H:%M:%S', errors='coerce')].date)].index[0])
    
    
    fig = plt.figure(1)
    fig.set_size_inches(20,10)
    
    fig = plt.figure(1)
    fig.set_size_inches(20,10)
    # A 2 metros
    #plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_2m_max, linestyle='-')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_2m_min, linestyle='-')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_2m, linestyle='-')
    #Suelo
    #plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_10cm, linestyle='-.', marker ='*', label = 'suelo_prom')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:]['tmp_10cm-max'], linestyle='-.', marker ='*', label = 'suelo_max')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:]['tmp_10cm-min'], linestyle='-.', marker ='*', label = 'suelo_min')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_10cm, linestyle='-.', marker ='*', label = 'suelo_prom')
    #Dentro del suelo
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_sue10cm, linestyle=':', marker ='x')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_sue30cm, linestyle=':', marker ='x')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_sue50cm, linestyle=':', marker ='x')
    #Estación convecnional
    plt.plot_date(x=conv_tiba_min.iloc[min_min:max_min,:].date, y=conv_tiba_min.iloc[min_min:max_min,:].TS, linestyle='--', marker ='s', label = 'Mínima-conv')
    plt.plot_date(x=conv_tiba_max.iloc[min_max:max_max,:].date, y=conv_tiba_max.iloc[min_max:max_max,:].TS, linestyle='--', marker ='s', label = 'Promedio-conv')
    plt.plot_date(x=conv_tiba_mean.iloc[min_mean:max_mean,:].date, y=conv_tiba_mean.iloc[min_mean:max_mean,:].TS, linestyle='--', marker ='s', label = 'Máxima-conv')

    
    plt.ylabel('Temperatura °C')
    plt.xlabel('Fecha')
    plt.xticks(rotation='vertical')
    plt.legend()
    
    path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph'
    
    os.chdir(path)
    plt.savefig(salida +'.png', figsize=(20,10) ,dpi = 199)
    plt.close()
    
    ###############
    ##############3
    ###############
    
    

    fig = plt.figure(1)
    fig.set_size_inches(20,10)
    # A 2 metros
    #plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_2m, linestyle='-', color = 'darkorange')
    #plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_2m_max, linestyle='-', color = 'b')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_2m_min, linestyle='-', color = 'g')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_2m, linestyle='-', color = 'darkorange')
    #Suelo
    #plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_10cm, linestyle='-.', marker ='*', label = 'suelo_prom', color = 'red')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:]['tmp_10cm-max'], linestyle='-.', marker ='*', label = 'suelo_max', color = 'm')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:]['tmp_10cm-min'], linestyle='-.', marker ='*', label = 'suelo_min', color = 'sienna')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_10cm, linestyle='-.', marker ='*', label = 'suelo_prom', color = 'red')
    
    plt.ylabel('Temperatira °C')
    plt.xlabel('Fecha')
    plt.xticks(rotation='vertical')
    plt.legend()
    
    path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph'
    
    os.chdir(path)
    plt.savefig(salida +'1.png', figsize=(20,10) ,dpi = 199)
    plt.close()
    
    
    
    fig = plt.figure(1)
    fig.set_size_inches(20,10)
    # A 2 metros
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_2m, linestyle='-', color = 'darkorange')
    #plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_2m_max, linestyle='-', color = 'b')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_2m_min, linestyle='-', color = 'g')
    #plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_2m, linestyle='-', color = 'darkorange')
    #Suelo
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_10cm, linestyle='-.', marker ='*', label = 'suelo_prom', color = 'red')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:]['tmp_10cm-max'], linestyle='-.', marker ='*', label = 'suelo_max', color = 'm')
    plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:]['tmp_10cm-min'], linestyle='-.', marker ='*', label = 'suelo_min', color = 'sienna')
    #plt.plot_date(x=hyd_tiba.iloc[min_rang_1:max_rang_1,:].date, y=hyd_tiba.iloc[min_rang_1:max_rang_1,:].tmp_10cm, linestyle='-.', marker ='*', label = 'suelo_prom', color = 'red')
    
    
    
    plt.ylabel('Temperatira °C')
    plt.xlabel('Fecha')
    plt.xticks(rotation='vertical')
    plt.legend()
    
    path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph'
    
    os.chdir(path)
    plt.savefig(salida +'2.png', figsize=(20,10) ,dpi = 199)
    plt.close()

    
#gra_tiem('20070129','20070208','salida_suelo')
#gra_tiem('20061227','20070101','salida_suelo') # Gráfica usada para la explicación de los datos dobles y faltantes

gra_tiem('20070101','20151201','edwin')
gra_tiem('20140828','20140903','20140830') # Fecha usada
gra_tiem('20080910','20080914','20080910_no_usada') # Fecha no usada
inicio_1 = pd.to_datetime('2016/12/07 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('2016/12/09 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
gra_tiem('20070129','20070208','edwin')

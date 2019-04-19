#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:21:37 2018
Código creado para a partír de la validación crear las gráficas año, mes, hora
@author: edwin
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:06:54 2018
# Script usado para la extracción de los valores de temperatura de los diferentes dominios y
realizar su comparación
@author: edwin
"""

import os
import pandas as pd
import numpy as np
import pdb
import matplotlib.pyplot as plt
 
def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)
 

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col1/')
list_files = pd.DataFrame({'col_1':os.listdir()})

explicacion = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/explicacion.txt')

#def grap_an_mes_hor ():
list_files.col_1.str[11:-3].unique()
names = []
tiempo = pd.DataFrame({'Estación':[],
                      'Delta':[]
        })


for i in list_files.col_1:
    #print(i)
    #i = 'v_21201200_tmp_2m.csv'
    base = pd.read_csv(i)
    cod = str(i)[2:10]
    tipo_1 = str(i)[11:-4]
    tipo = explicacion[explicacion.iloc[:,0] == tipo_1].iloc[1,3]
    
    base.date = pd.to_datetime(base.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    base['unos'] = 1
    base['year_1'] = pd.DatetimeIndex(base.date).year
    base['month_1'] = pd.DatetimeIndex(base.date).month
    base['hour_1'] = pd.DatetimeIndex(base.date).hour
    
    #base.groupby(['year_1'])['null_1'].sum()
    base_sum_year = base.groupby(['year_1']).sum()
    base_sum_month = base.groupby(['month_1']).sum()
    base_sum_hour = base.groupby(['hour_1']).sum()
    

    mediana_1 = (base.date[1:].reset_index() - base.date[:-1].reset_index())
    mediana_2 = mediana_1.median()[1]
    
    tiempo_1 = pd.DataFrame({'Estación':[i],
                          'Delta':mediana_2
            })    
    
    tiempo = pd.concat([tiempo, tiempo_1])
    
    
    columnas_1 = []
    for oo in base.columns: 
        for uu in explicacion.iloc[:,1].unique():
            if oo == uu:
                columnas_1.append(uu)
    
    for jj in columnas_1:
        print(jj)
        #### Año El identificador es 1
        #jj = 'null_1'
        ### Un cambio de las variables en letras a numeros para poder hacer la automatización de las gráficas en latex
        tipo_validacion = explicacion[explicacion.iloc[:,1] == jj].reset_index().iloc[0,5]
        #Año
        #delta = pd.Timedelta('360 days') // mediana_2
        base_sum_year[jj+'_fal'] = base_sum_year.unos - base_sum_year[jj]
        
        plt.stackplot(base_sum_year.index, base_sum_year[jj], base_sum_year[jj+'_fal'], 
                      colors = ['gray','silver'],
                      labels = ['Validos', 'No-validos'])
        plt.title(explicacion[explicacion.iloc[:,1] == jj].reset_index().iloc[0,3])
        plt.xlabel('Año')
        plt.ylabel('Frecuencia')
        plt.legend()
        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_validacion_automaticas_2/'+str(cod)+'_'+str(tipo)+'_'+str(tipo_validacion)+'_1_'+'.png', figsize=(20,10) ,dpi = 199) # El identificador que es un año es el 1 al final
        plt.close()
        
        
        ### MEs

        
        base_sum_month[jj+'_fal'] = base_sum_month.unos - base_sum_month[jj]
        
        plt.stackplot(base_sum_month.index, base_sum_month[jj], base_sum_month[jj+'_fal'], 
                      colors = ['gray','silver'],
                      labels = ['Validos', 'No-validos'])
        plt.title(explicacion[explicacion.iloc[:,1] == jj].reset_index().iloc[0,3])
        plt.xlabel('Mes')
        plt.ylabel('Frecuencia')
        plt.xticks(np.arange(1,13))
        plt.legend()
        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_validacion_automaticas_2/'+str(cod)+'_'+str(tipo)+'_'+str(tipo_validacion)+'_2_'+'.png', figsize=(20,10) ,dpi = 199)
        plt.close()    
        
        
        ### Hora

        
        base_sum_hour[jj+'_fal'] = base_sum_hour.unos - base_sum_hour[jj]
        
        plt.stackplot(base_sum_hour.index, base_sum_hour[jj], base_sum_hour[jj+'_fal'],
                      colors = ['gray','silver'],
                      labels = ['Validos', 'No-validos'])
        plt.title(explicacion[explicacion.iloc[:,1] == jj].reset_index().iloc[0,3])
        plt.xlabel('Hora')
        plt.xticks(np.arange(0,24))
        plt.ylabel('Frecuencia')
        plt.legend()
        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_validacion_automaticas_2/'+str(cod)+'_'+str(tipo)+'_'+str(tipo_validacion)+'_3_'+'.png', figsize=(20,10) ,dpi = 199)
        plt.close()
        
        
        ## Guardar las bases
        
        base_sum_year.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/t_validacion_automaticas_2/'+str(cod)+'_'+str(tipo)+'_1_'+'.csv')
        base_sum_month.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/t_validacion_automaticas_2/'+str(cod)+'_'+str(tipo)+'_2_'+'.csv')
        base_sum_hour.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/t_validacion_automaticas_2/'+str(cod)+'_'+str(tipo)+'_3_'+'.csv')
        
    
    tiempo.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tabla_tiempos_medianos_estaciones.csv')
            

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:50:21 2018
Descripción de una helada con las regresiones multivariadasS
@author: edwin
"""

    
##Descripción de las heladas

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspect
from datetime import datetime  
from datetime import timedelta
import matplotlib.dates as mdates



############### Caracterización de las temperaturas
def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)

####Descripción de los datos de temperatura
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col1')
file_list = os.listdir()
estacion_var = []
estacion_1 = pd.DataFrame({'date':[]})
base_1 = pd.DataFrame()
for uu in file_list:
    if 'tmp_2m.csv' in uu:
        #uu = 'v_21206990_tmp_2m.csv' #Estación automática Tibaitatá
        print(uu)
        cod_1 = uu[2:10]
        estacion_1 = pd.read_csv(uu)



#if 'v_21206990' in uu:
#        print(uu)
#        base_2 = pd.read_csv(uu)
#        estacion_1 = pd.merge(estacion_1, base_2, on='date', how='outer')
        
        
        
        estacion_1.date = pd.to_datetime(estacion_1.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
        estacion_1 = estacion_1.sort_values('date')
        
        
        estacion_1['date_2'] = (estacion_1.date.dt.year * 10000) + (estacion_1.date.dt.month * 100) + (estacion_1.date.dt.day)
        estacion_1['date_ant'] = estacion_1.date - timedelta(days=1)
        estacion_1['date_ant'] = ((estacion_1.date_ant.dt.year) * 10000) + ((estacion_1.date_ant.dt.month ) * 100) + ((estacion_1.date_ant.dt.day))
        
        ###Busqueda de las heladas
#        estacion_1[(estacion_1.val_tmp == 0) & (estacion_1.tmp_2m < 0)]
#        np.where(((estacion_1.val_tmp == 0) & (estacion_1.tmp_2m < 0)), 1, 0) # 1 = Helada. Si se cumple que la temperatura está bajo cero y es un dato válido entonces se coloca 1
        
        union_1 = estacion_1[['date_2', 'date_ant']]
        union_1['heladas'] = np.where(((estacion_1.val_tmp == 0) & (estacion_1.tmp_2m < 0)), 1, 0)
        
        union_2 = pd.DataFrame(union_1.groupby(['date_2'])['heladas'].max())
        union_2['date_2'] = union_2.index
        ###Unión con los valores de helada del mismo día
        estacion_2 = pd.merge(estacion_1, union_2, on='date_2', how='outer')
        ###unión con los valores de las heladas del día anterior
        union_3 = pd.DataFrame(union_1.groupby(['date_ant'])['heladas'].max())
        union_3['date_2'] = union_3.index
        union_3.columns.values[0] = 'heladas_antes'
        
        estacion_3_1 = pd.merge(estacion_2, union_3, on='date_2', how='outer')
        
        
        # búsqueda de las altas temperaturas
        
        #Extracción de los valores superiores a 25
        union_1_1 = estacion_1[['date_2', 'date_ant']]
        union_1_1['altas'] = np.where(((estacion_1.val_tmp == 0) & (estacion_1.tmp_2m > 25)), 1, 0)
        #agrupación de los valores por presencia de las altas temperaturas
        union_2_1 = pd.DataFrame(union_1_1.groupby(['date_2'])['altas'].max())
        union_2_1['date_2'] = union_2_1.index
        estacion_3_1 = pd.merge(estacion_3_1, union_2_1, on='date_2', how='outer')
        union_3_1 = pd.DataFrame(union_1_1.groupby(['date_ant'])['altas'].max())
        union_3_1['date_2'] = union_3_1.index
        union_3_1.columns.values[0] = 'altas_antes'
        
        estacion_3 = pd.merge(estacion_3_1, union_3_1, on='date_2', how='outer')
        
        
#        estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].tmp_2m.mean()
#        estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].tmp_2m.mean()
#        estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 0)].tmp_2m.mean()
#        
#        estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].tmp_2m.hist()
#        estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].tmp_2m.hist()
#        estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 0)].tmp_2m.hist()
        
        #estacion_3.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_exploracion/estacion_3.csv')
        #estacion_3 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_exploracion/estacion_3.csv')
        
        ##### Gráfica de las horas contra las temperaturas
        estacion_3.date = pd.to_datetime(estacion_3.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
        
        estacion_3['hora'] = 10000+ (estacion_3.date.dt.hour * 100) + (estacion_3.date.dt.minute)
        estacion_3['hora_n'] = (estacion_3.date.dt.hour * 100) + (estacion_3.date.dt.minute/ 60)
        estacion_3['hora'] = estacion_3.hora.astype('str')
        qqq = estacion_3.hora.str[1:]
        www = qqq.str[:-2]
        estacion_3['hora'] = pd.to_datetime(www, format ='%H%M', errors='coerce')


#        
#        plt.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 0)].hora,estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 0)].tmp_2m)
#        plt.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].tmp_2m)
#        plt.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].tmp_2m)
#        plt.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].tmp_2m)
#        plt.legend(['No-Helada','Helada', 'heladas antes'])
#        plt.xticks(rotation=90)
#        
#        ### 
#        
#        x = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].hora
#        x1 = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].hora_n
#        y = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].tmp_2m
#        
#        fit = np.polyfit(x1, y, deg = 5)
#        p = np.poly1d(fit)
#        
#        plt.plot_date(x, y)
#        plt.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].tmp_2m)
#        plt.plot(x, p(x1), "r--")
#        plt.legend(['Helada antes','Helada'])
#        plt.xticks(rotation=90)
        
        
        ###Dejar vacias las variables
        
        p_total = []
        p_sin_hel = []
        p_antes = []
        p_helada = []
        p_altas = []
        p_altas_antes = []
        
        ###Ajusste de un polinomio de 4 orden porque posee 3 picos
        
        base_2 = pd.DataFrame()
        
        base_2['cod_1'] = pd.DataFrame({'a':[cod_1]})
        
        # Datos totales
        #if len(estacion_3[(estacion_3.val_tmp == 0)].hora_n) < 10:
        #    continue
        
        x = estacion_3[(estacion_3.val_tmp == 0)].hora
        x1t = estacion_3[(estacion_3.val_tmp == 0)].hora_n
        yt = estacion_3[(estacion_3.val_tmp == 0)].tmp_2m
        if len(yt) > 10:
            
            base_2['total_max'] = pd.DataFrame({'a':[yt.max()]})
            base_2['total_min'] = pd.DataFrame({'a':[yt.min()]})
            base_2['total_mean'] = pd.DataFrame({'a':[yt.mean()]})
            base_2['total_median'] = pd.DataFrame({'a':[yt.median()]})
            base_2['total_std'] = pd.DataFrame({'a':[yt.std()]})
            base_2['total_std'] = pd.DataFrame({'a':[yt.std()]})
            fit = np.polyfit(x1t, yt, deg = 4)
            p_total = np.poly1d(fit)
            
            #plt.plot(x1, p_total(x1), "r--")
        
        
        # Datos sin heladas
        x = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 0)].hora
        x1 = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 0)].hora_n
        y = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 0)].tmp_2m
        
        if len(y) > 10:
            
            base_2['sin_heladas_max'] = pd.DataFrame({'a':[y.max()]})
            base_2['sin_heladas_min'] = pd.DataFrame({'a':[y.min()]})
            base_2['sin_heladas_mean'] = pd.DataFrame({'a':[y.mean()]})
            base_2['sin_heladas_median'] = pd.DataFrame({'a':[y.median()]})
            base_2['sin_heladas_std'] = pd.DataFrame({'a':[y.std()]})
            base_2['sin_heladas_std'] = pd.DataFrame({'a':[y.std()]})                
            fit = np.polyfit(x1, y, deg = 4)
            p_sin_hel = np.poly1d(fit)
            #plt.plot(x1, p_sin_hel(x1), "r--")
        
        # Datos un día antes de la helada
        x = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].hora
        x1 = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].hora_n
        y = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].tmp_2m
        
        if len(y) > 10:
            
            base_2['heladas_antes_max'] = pd.DataFrame({'a':[y.max()]})
            base_2['heladas_antes_min'] = pd.DataFrame({'a':[y.min()]})
            base_2['heladas_antes_mean'] = pd.DataFrame({'a':[y.mean()]})
            base_2['heladas_antes_median'] = pd.DataFrame({'a':[y.median()]})
            base_2['heladas_antes_std'] = pd.DataFrame({'a':[y.std()]})
            base_2['heladas_antes_std'] = pd.DataFrame({'a':[y.std()]})               
            fit = np.polyfit(x1, y, deg = 4)
            p_antes = np.poly1d(fit)
            #plt.plot(x, p_antes(x1), "r--")
        
        
        # Datos día de la helada
        x = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].hora
        x1 = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].hora_n
        y = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].tmp_2m
        
        if len(y) > 10:
            
            base_2['helada_max'] = pd.DataFrame({'a':[y.max()]})
            base_2['helada_min'] = pd.DataFrame({'a':[y.min()]})
            base_2['helada_mean'] = pd.DataFrame({'a':[y.mean()]})
            base_2['helada_median'] = pd.DataFrame({'a':[y.median()]})
            base_2['helada_std'] = pd.DataFrame({'a':[y.std()]})
            base_2['helada_std'] = pd.DataFrame({'a':[y.std()]})            
            fit = np.polyfit(x1, y, deg = 4)
            p_helada = np.poly1d(fit)
            #plt.plot(x, p_helada(x1), "r--")
        
        
        ####Plot con altas temperaturas
        x = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas == 1)].hora
        x1 = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas == 1)].hora_n
        y = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas == 1)].tmp_2m
        
        if len(y) > 10:
            
            base_2['altas_max'] = pd.DataFrame({'a':[y.max()]})
            base_2['altas_min'] = pd.DataFrame({'a':[y.min()]})
            base_2['altas_mean'] = pd.DataFrame({'a':[y.mean()]})
            base_2['altas_median'] = pd.DataFrame({'a':[y.median()]})
            base_2['altas_std'] = pd.DataFrame({'a':[y.std()]})
            base_2['altas_std'] = pd.DataFrame({'a':[y.std()]}) 
            fit = np.polyfit(x1, y, deg = 4)
            p_altas = np.poly1d(fit)
            #plt.plot(x, p_altas(x1), "r--")
        
        
        ####Plot con altas temperaturas un día antes
        x = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas_antes == 1)].hora
        x1 = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas_antes == 1)].hora_n
        y = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas_antes == 1)].tmp_2m
        
        if len(y) > 10:
            
            base_2['altas_antes_max'] = pd.DataFrame({'a':[y.max()]})
            base_2['altas_antes_min'] = pd.DataFrame({'a':[y.min()]})
            base_2['altas_antes_mean'] = pd.DataFrame({'a':[y.mean()]})
            base_2['altas_antes_median'] = pd.DataFrame({'a':[y.median()]})
            base_2['altas_antes_std'] = pd.DataFrame({'a':[y.std()]})
            base_2['altas_antes_std'] = pd.DataFrame({'a':[y.std()]}) 
            fit = np.polyfit(x1, y, deg = 4)
            p_altas_antes = np.poly1d(fit)
            #plt.plot(x, p_altas_antes(x1), "r--")
        
########En esta parte se realiza la unión de los datos a la base de datos        
        base_1 = base_1.append(base_2) # Usado para la recolección de los datos generados por las estaciones
        
        base_3 = pd.DataFrame({'rango_1':np.linspace(min(x1t), max(x1t), 100)})
        for pp, name_1 in zip([p_total, p_sin_hel, p_antes, p_helada, p_altas, p_altas_antes], ['p_total', 'p_sin_hel', 'p_antes', 'p_helada', 'p_altas', 'p_altas_antes']):
            try:
                base_3[name_1] = pp(base_3.rango_1)
            except TypeError:
                print('error')
                continue
        
        
        
        fecha_1 = pd.to_datetime('1900-01-01 00:32:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
        
        fecha_2 = pd.to_datetime('1900-01-01 23:59:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
        
        #base_3.iloc[:,1:].plot()
        base_3['date'] = pd.to_datetime(np.linspace(fecha_1.value, fecha_2.value, 100))
        
        
        ##Primera gráfica de las temperaturas
        
        ###Plot de las temperaturas totales = 1
        ###Plot de las temperaturas sin heladas = 2
        ###Plot de las temperaturas con heladas = 3
        ###Plot de las temperaturas antes de la helada = 4
        ###Plot de las temperaturas con altas temperaturas = 5
        ###Plot de las temperaturas antes de las altas temperaturas= 6
        
        
        #Plot de las temperaturas totales
        for ooo in base_3.columns.unique():
            if ooo == 'p_total':
                
                
                _=plt.rcParams["figure.figsize"] = (8,6)
                fig, ax = plt.subplots()
                ax.plot_date(estacion_3[(estacion_3.val_tmp == 0)].hora, estacion_3[(estacion_3.val_tmp == 0)].tmp_2m, markersize=5, color='gray')
                #ax.plot_date(base_3.date,  base_3.p_total, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel('Temperatura °C')
                _=plt.xticks(rotation=90)
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:10]+'_1.png' ,dpi = 100)
                plt.close()
        
        
        
        #Plot de las temperaturas sin las heladas
        for ooo in base_3.columns.unique():
            if ooo == 'p_sin_hel':
                
                
                fig, ax = plt.subplots()
                plt.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 0)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 0)].tmp_2m, markersize=5, color='gray')
                
                #ax.plot_date(base_3.date,  base_3.p_sin_hel, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel('Temperatura °C')
                _=plt.xticks(rotation=90)     
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:10]+'_2.png' ,dpi = 100)
                plt.close()
        
        
        
        #Plot de las temperaturas en la helada
        for ooo in base_3.columns.unique():
            if ooo == 'p_helada':
                
                
                
                fig, ax = plt.subplots()
                ax.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].tmp_2m, markersize=5, color='gray')
                #ax.plot_date(base_3.date,  base_3.p_helada, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel('Temperatura °C')
                _=plt.xticks(rotation=90)   
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:10]+'_3.png' ,dpi = 100)
                plt.close()        
        
        #Plot de las temperaturas antes de la helada
        for ooo in base_3.columns.unique():
            if ooo == 'p_antes':
                
                fig, ax = plt.subplots()
                ax.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].tmp_2m, markersize=5, color='gray')
                #ax.plot_date(base_3.date,  base_3.p_antes, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel('Temperatura °C')
                _=plt.xticks(rotation=90)   
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:10]+'_4.png' ,dpi = 100)
                plt.close()
        
        
        #Plot de las altas temperaturas altas
        for ooo in base_3.columns.unique():
            if ooo == 'p_altas':
                
                fig, ax = plt.subplots()
                ax.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas == 1)].tmp_2m, markersize=5, color='gray')
                #ax.plot_date(base_3.date,  base_3.p_altas, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel('Temperatura °C')
                _=plt.xticks(rotation=90)   
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:10]+'_5.png' ,dpi = 100)
                plt.close()
        
        
        #Plot de las temperaturas antes de la helada
        for ooo in base_3.columns.unique():
            if ooo == 'p_altas_antes':
                
                fig, ax = plt.subplots()
                ax.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas_antes == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas_antes == 1)].tmp_2m, markersize=5, color='gray')
                #ax.plot_date(base_3.date,  base_3.p_altas_antes, '-', color='k')
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                _=plt.xlabel('Hora')
                _=plt.ylabel('Temperatura °C')
                _=plt.xticks(rotation=90)   
                plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:10]+'_6.png' ,dpi = 100)
                plt.close()


#base_1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/resumen_dias_con_heladas_20190129.csv')
#base_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/resumen_dias_con_heladas_20190129.csv')




#######################################################
                
                # Humedad


#######################################################


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspect
from datetime import datetime  
from datetime import timedelta
import matplotlib.dates as mdates
import pdb


############### Caracterización de las temperaturas
def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)
    
### Buscardor de letras en las columnas
    
def busca_columna(base, contains):
    lista_base = pd.DataFrame({'a':base.columns.unique()})
    salida = []
    for i in lista_base.a:
        if contains in i:
            salida.append(lista_base[lista_base.a == i].index[0])
    return(salida)

####Descripción de los datos de temperatura
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col1')
file_list = os.listdir()
estacion_var = []
estacion_1 = pd.DataFrame({'date':[]})
base_1 = pd.DataFrame()
for uu in file_list:
    if 'tmp_2m.csv' in uu:
        uu = 'v_21206990_tmp_2m.csv' #Estación automática Tibaitatá
        print(uu)
        cod_1 = uu[2:10]
        estacion_1 = pd.read_csv(uu)
        
        for tipo_1, var_2, val_2, nombre_var in zip(['_hum_2m.csv', '_precip_1.csv', '_vel_vi10.csv', '_val_rad.csv'], ['hum_2m', 'precip_1', 'vel_vi10', 'rad_1'], ['val_hum', 'val_prec', 'val_vv', 'val_rad'], ['Humedad %', 'Precipitación mm', 'm/s', 'W/$m^2$']):
#            tipo_1 = '_hum_2m.csv'
#            var_2= 'hum_2m'
#            val_2 = 'val_hum'
#            tipo_1 = '_vel_vi10.csv'
#            var_2= 'vel_vi10'
#            val_2 = 'val_vv'            
            print(tipo_1, var_2, val_2)
            if 'v_'+cod_1 +tipo_1 in file_list:
                
                
                ##Cargar la otra base a evaluar
                
                estacion_a = pd.read_csv('v_'+cod_1 +tipo_1)
                estacion_a.date = pd.to_datetime(estacion_a.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
                estacion_a['date_2'] = (estacion_a.date.dt.year * 10000) + (estacion_a.date.dt.month * 100) + (estacion_a.date.dt.day)
                
                

        #if 'v_21206990' in uu:
        #        print(uu)
        #        base_2 = pd.read_csv(uu)
        #        estacion_1 = pd.merge(estacion_1, base_2, on='date', how='outer')
                
                
                
                estacion_1.date = pd.to_datetime(estacion_1.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
                estacion_1 = estacion_1.sort_values('date')
                
                
                estacion_1['date_2'] = (estacion_1.date.dt.year * 10000) + (estacion_1.date.dt.month * 100) + (estacion_1.date.dt.day)
                estacion_1['date_ant'] = estacion_1.date - timedelta(days=1)
                estacion_1['date_ant'] = ((estacion_1.date_ant.dt.year) * 10000) + ((estacion_1.date_ant.dt.month ) * 100) + ((estacion_1.date_ant.dt.day))
                
                ###Busqueda de las heladas
        #        estacion_1[(estacion_1.val_tmp == 0) & (estacion_1.tmp_2m < 0)]
        #        np.where(((estacion_1.val_tmp == 0) & (estacion_1.tmp_2m < 0)), 1, 0) # 1 = Helada. Si se cumple que la temperatura está bajo cero y es un dato válido entonces se coloca 1
                
                union_1 = estacion_1[['date_2', 'date_ant']]
                union_1['heladas'] = np.where(((estacion_1.val_tmp == 0) & (estacion_1.tmp_2m < 0)), 1, 0)
                
                union_2 = pd.DataFrame(union_1.groupby(['date_2'])['heladas'].max())
                union_2['date_2'] = union_2.index
                ###Unión con los valores de helada del mismo día
                #estacion_2 = pd.merge(estacion_1, union_2, on='date_2', how='outer')
                ###unión con los valores de las heladas del día anterior
                union_3 = pd.DataFrame(union_1.groupby(['date_ant'])['heladas'].max())
                union_3['date_2'] = union_3.index
                union_3.columns.values[0] = 'heladas_antes'
                
                #estacion_3_1 = pd.merge(estacion_2, union_3, on='date_2', how='outer')
                
                
                # búsqueda de las altas temperaturas
                
                #Extracción de los valores superiores a 25
                union_1_1 = estacion_1[['date_2', 'date_ant']]
                union_1_1['altas'] = np.where(((estacion_1.val_tmp == 0) & (estacion_1.tmp_2m > 25)), 1, 0)
                #agrupación de los valores por presencia de las altas temperaturas
                union_2_1 = pd.DataFrame(union_1_1.groupby(['date_2'])['altas'].max())
                union_2_1['date_2'] = union_2_1.index
                #estacion_3_1 = pd.merge(estacion_3_1, union_2_1, on='date_2', how='outer')
                union_3_1 = pd.DataFrame(union_1_1.groupby(['date_ant'])['altas'].max())
                union_3_1['date_2'] = union_3_1.index
                union_3_1.columns.values[0] = 'altas_antes'
                #Unipon de los datos del día antes de la helada
                
                # Este se comentaréa porque ya no se va a usar temperatura sino la variable que se desee estudiar
                #estacion_3 = pd.merge(estacion_3_1, union_3_1, on='date_2', how='outer') 
                
                ###### Unión de la nueva base con la temperatura con la finalidad de realizar las gráficas y la tabla
                
                estacion_b = pd.merge(estacion_a, union_2, on = 'date_2', how='outer') # unión con las heladas del día
                estacion_c = pd.merge(estacion_b, union_3, on = 'date_2', how='outer') # Unión con el día anterior a las heladas
                estacion_d = pd.merge(estacion_c, union_2_1, on = 'date_2', how='outer') # Unión con el día de las altas temperaturas
                estacion_e = pd.merge(estacion_d, union_3_1, on = 'date_2', how='outer') # Unión con el día anterior de las altas temperaturas
                estacion_3 = estacion_e                        
                
                ##### Gráfica de las horas contra las temperaturas
                estacion_3.date = pd.to_datetime(estacion_3.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
                
                estacion_3['hora'] = 10000+ (estacion_3.date.dt.hour * 100) + (estacion_3.date.dt.minute)
                estacion_3['hora_n'] = (estacion_3.date.dt.hour * 100) + (estacion_3.date.dt.minute/ 60)
                estacion_3['hora'] = estacion_3.hora.astype('str')
                qqq = estacion_3.hora.str[1:]
                www = qqq.str[:-2]
                estacion_3['hora'] = pd.to_datetime(www, format ='%H%M', errors='coerce')
                
                ###Voy a cambiar la variable que venga por la vaiable de temperatura con la finalidad de no hacer más 
                ## modificaciones
                
                ###Buscar la variable y cambiar el nombre
                
                busca_columna(base=estacion_3, contains=var_2)[0]
                
                estacion_3.columns.values[busca_columna(base=estacion_3, contains=var_2)[0]] = 'tmp_2m'
                estacion_3.columns.values[busca_columna(base=estacion_3, contains=val_2)[0]] = 'val_tmp'
                estacion_3 = estacion_3.reset_index()
                
                ###Dejar vacias las variables
                
                p_total = []
                p_sin_hel = []
                p_antes = []
                p_helada = []
                p_altas = []
                p_altas_antes = []
                
                ###Ajusste de un polinomio de 4 orden porque posee 3 picos
                
                base_2 = pd.DataFrame()
                
                base_2['cod_1'] = pd.DataFrame({'a':[cod_1]})
                base_2['var_1'] = pd.DataFrame({'a':[var_2]})
                
                # Datos totales
                if len(estacion_3[(estacion_3.val_tmp == 0)].hora_n) < 10:
                    continue
                
                x = estacion_3[(estacion_3.val_tmp == 0)].hora
                x1t = estacion_3[(estacion_3.val_tmp == 0)].hora_n
                yt = estacion_3[(estacion_3.val_tmp == 0)].tmp_2m
                if len(yt) > 10:
                    
                    base_2['total_max'] = pd.DataFrame({'a':[yt.max()]})
                    base_2['total_min'] = pd.DataFrame({'a':[yt.min()]})
                    base_2['total_mean'] = pd.DataFrame({'a':[yt.mean()]})
                    base_2['total_median'] = pd.DataFrame({'a':[yt.median()]})
                    base_2['total_std'] = pd.DataFrame({'a':[yt.std()]})
                    base_2['total_std'] = pd.DataFrame({'a':[yt.std()]})
                    try:
                        fit = np.polyfit(x1t, yt, deg = 4)
                        p_total = np.poly1d(fit)
                    except ValueError:
                        pass
                        
                    
                    
                    #plt.plot(x1, p_total(x1), "r--")
                
                
                # Datos sin heladas
                x = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 0)].hora
                x1 = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 0)].hora_n
                y = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 0)].tmp_2m
                
                if len(y) > 10:
                    
                    base_2['sin_heladas_max'] = pd.DataFrame({'a':[y.max()]})
                    base_2['sin_heladas_min'] = pd.DataFrame({'a':[y.min()]})
                    base_2['sin_heladas_mean'] = pd.DataFrame({'a':[y.mean()]})
                    base_2['sin_heladas_median'] = pd.DataFrame({'a':[y.median()]})
                    base_2['sin_heladas_std'] = pd.DataFrame({'a':[y.std()]})
                    base_2['sin_heladas_std'] = pd.DataFrame({'a':[y.std()]})                
                    fit = np.polyfit(x1, y, deg = 4)
                    p_sin_hel = np.poly1d(fit)
                    #plt.plot(x1, p_sin_hel(x1), "r--")
                
                # Datos un día antes de la helada
                x = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].hora
                x1 = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].hora_n
                y = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].tmp_2m
                
                if len(y) > 10:
                    
                    base_2['heladas_antes_max'] = pd.DataFrame({'a':[y.max()]})
                    base_2['heladas_antes_min'] = pd.DataFrame({'a':[y.min()]})
                    base_2['heladas_antes_mean'] = pd.DataFrame({'a':[y.mean()]})
                    base_2['heladas_antes_median'] = pd.DataFrame({'a':[y.median()]})
                    base_2['heladas_antes_std'] = pd.DataFrame({'a':[y.std()]})
                    base_2['heladas_antes_std'] = pd.DataFrame({'a':[y.std()]})
                    try:
                        fit = np.polyfit(x1, y, deg = 4)
                        p_antes = np.poly1d(fit)
                    except ValueError:
                        pass
                    
                    #plt.plot(x, p_antes(x1), "r--")
                
                
                # Datos día de la helada
                x = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].hora
                x1 = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].hora_n
                y = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].tmp_2m
                
                if len(y) > 10:
                    
                    base_2['helada_max'] = pd.DataFrame({'a':[y.max()]})
                    base_2['helada_min'] = pd.DataFrame({'a':[y.min()]})
                    base_2['helada_mean'] = pd.DataFrame({'a':[y.mean()]})
                    base_2['helada_median'] = pd.DataFrame({'a':[y.median()]})
                    base_2['helada_std'] = pd.DataFrame({'a':[y.std()]})
                    base_2['helada_std'] = pd.DataFrame({'a':[y.std()]})            
                    try:
                        fit = np.polyfit(x1, y, deg = 4)
                        p_helada = np.poly1d(fit)
                    except ValueError:
                        pass
                    
                    #plt.plot(x, p_helada(x1), "r--")
                
                
                ####Plot con altas temperaturas
                x = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas == 1)].hora
                x1 = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas == 1)].hora_n
                y = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas == 1)].tmp_2m
                
                if len(y) > 10:
                    
                    base_2['altas_max'] = pd.DataFrame({'a':[y.max()]})
                    base_2['altas_min'] = pd.DataFrame({'a':[y.min()]})
                    base_2['altas_mean'] = pd.DataFrame({'a':[y.mean()]})
                    base_2['altas_median'] = pd.DataFrame({'a':[y.median()]})
                    base_2['altas_std'] = pd.DataFrame({'a':[y.std()]})
                    base_2['altas_std'] = pd.DataFrame({'a':[y.std()]}) 
                    try:
                        fit = np.polyfit(x1, y, deg = 4)
                        p_altas = np.poly1d(fit)
                    except ValueError:
                        pass
                    
                    #plt.plot(x, p_altas(x1), "r--")
                
                
                ####Plot con altas temperaturas un día antes
                x = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas_antes == 1)].hora
                x1 = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas_antes == 1)].hora_n
                y = estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas_antes == 1)].tmp_2m
                
                if len(y) > 10:
                    
                    base_2['altas_antes_max'] = pd.DataFrame({'a':[y.max()]})
                    base_2['altas_antes_min'] = pd.DataFrame({'a':[y.min()]})
                    base_2['altas_antes_mean'] = pd.DataFrame({'a':[y.mean()]})
                    base_2['altas_antes_median'] = pd.DataFrame({'a':[y.median()]})
                    base_2['altas_antes_std'] = pd.DataFrame({'a':[y.std()]})
                    base_2['altas_antes_std'] = pd.DataFrame({'a':[y.std()]}) 
                    try:
                        fit = np.polyfit(x1, y, deg = 4)
                        p_altas_antes = np.poly1d(fit)
                    except ValueError:
                        pass
                    
                    #plt.plot(x, p_altas_antes(x1), "r--")
                
        ########En esta parte se realiza la unión de los datos a la base de datos        
                base_1 = base_1.append(base_2) # Usado para la recolección de los datos generados por las estaciones
                
                base_3 = pd.DataFrame({'rango_1':np.linspace(min(x1t), max(x1t), 100)})
                for pp, name_1 in zip([p_total, p_sin_hel, p_antes, p_helada, p_altas, p_altas_antes], ['p_total', 'p_sin_hel', 'p_antes', 'p_helada', 'p_altas', 'p_altas_antes']):
                    try:
                        base_3[name_1] = pp(base_3.rango_1)
                    except TypeError:
                        print('No hay variable ', name_1)
                        continue
                
                
                
                fecha_1 = pd.to_datetime('1900-01-01 00:32:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
                
                fecha_2 = pd.to_datetime('1900-01-01 23:59:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
                
                #base_3.iloc[:,1:].plot()
                base_3['date'] = pd.to_datetime(np.linspace(fecha_1.value, fecha_2.value, 100))
                
                
                ##Primera gráfica de las temperaturas
                
                ###Plot de las temperaturas totales = 1
                ###Plot de las temperaturas sin heladas = 2
                ###Plot de las temperaturas con heladas = 3
                ###Plot de las temperaturas antes de la helada = 4
                ###Plot de las temperaturas con altas temperaturas = 5
                ###Plot de las temperaturas antes de las altas temperaturas= 6
                
                #pdb.set_trace()
                #Plot de las temperaturas totales
                for ooo in base_3.columns.unique():
                    if ooo == 'p_total':
                        
                        
                        _=plt.rcParams["figure.figsize"] = (8,6)
                        fig, ax = plt.subplots()
                        ax.plot_date(estacion_3[(estacion_3.val_tmp == 0)].hora, estacion_3[(estacion_3.val_tmp == 0)].tmp_2m, markersize=5, color='gray')
                        #ax.plot_date(base_3.date,  base_3.p_total, '-', color='k')
                        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                        _=plt.xlabel('Hora')
                        _=plt.ylabel(nombre_var)
                        _=plt.xticks(rotation=90)
                        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:11]+var_2+'_1.png' ,dpi = 100)
                        plt.close()
                
                
                
                #Plot de las temperaturas sin las heladas
                for ooo in base_3.columns.unique():
                    if ooo == 'p_sin_hel':
                        
                        
                        fig, ax = plt.subplots()
                        plt.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 0)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 0)].tmp_2m, markersize=5, color='gray')
                        
                        #ax.plot_date(base_3.date,  base_3.p_sin_hel, '-', color='k')
                        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                        _=plt.xlabel('Hora')
                        _=plt.ylabel(nombre_var)
                        _=plt.xticks(rotation=90)     
                        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:11]+var_2+'_2.png' ,dpi = 100)
                        plt.close()
                
                
                
                #Plot de las temperaturas en la helada
                for ooo in base_3.columns.unique():
                    if ooo == 'p_helada':
                        
                        
                        
                        fig, ax = plt.subplots()
                        #ax.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas == 1)].tmp_2m, markersize=5, color='gray')
                        ax.plot_date(estacion_3[(estacion_3.heladas == 1)].hora, estacion_3[(estacion_3.heladas == 1)].tmp_2m, markersize=5, color='gray')
                        #ax.plot_date(base_3.date,  base_3.p_helada, '-', color='k')
                        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                        _=plt.xlabel('Hora')
                        _=plt.ylabel(nombre_var)
                        _=plt.xticks(rotation=90)   
                        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:11]+var_2+'_3.png' ,dpi = 100)
                        plt.close()        
                
                #Plot de las temperaturas antes de la helada
                for ooo in base_3.columns.unique():
                    if ooo == 'p_antes':
                        
                        fig, ax = plt.subplots()
                        ax.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.heladas_antes == 1)].tmp_2m, markersize=5, color='gray')
                        #ax.plot_date(base_3.date,  base_3.p_antes, '-', color='k')
                        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                        _=plt.xlabel('Hora')
                        _=plt.ylabel(nombre_var)
                        _=plt.xticks(rotation=90)   
                        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:11]+var_2+'_4.png' ,dpi = 100)
                        plt.close()
                
                
                #Plot de las altas temperaturas altas
                for ooo in base_3.columns.unique():
                    if ooo == 'p_altas':
                        
                        fig, ax = plt.subplots()
                        ax.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas == 1)].tmp_2m, markersize=5, color='gray')
                        #ax.plot_date(base_3.date,  base_3.p_altas, '-', color='k')
                        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                        _=plt.xlabel('Hora')
                        _=plt.ylabel(nombre_var)
                        _=plt.xticks(rotation=90)   
                        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:11]+var_2+'_5.png' ,dpi = 100)
                        plt.close()
                
                
                #Plot de las temperaturas antes de la helada
                for ooo in base_3.columns.unique():
                    if ooo == 'p_altas_antes':
                        
                        fig, ax = plt.subplots()
                        ax.plot_date(estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas_antes == 1)].hora, estacion_3[(estacion_3.val_tmp == 0)&(estacion_3.altas_antes == 1)].tmp_2m, markersize=5, color='gray')
                        ##ax.plot_date(base_3.date,  base_3.p_altas_antes, '-', color='k')
                        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H-%M"))
                        _=plt.xlabel('Hora')
                        _=plt.ylabel(nombre_var)
                        _=plt.xticks(rotation=90)   
                        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_var_dia_1/'+str(uu)[2:11]+var_2+'_6.png' ,dpi = 100)
                        plt.close()


#base_1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/resumen_todas_var_con_heladas_20190129.csv')
#base_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/resumen_todas_var_con_heladas_20190129.csv')


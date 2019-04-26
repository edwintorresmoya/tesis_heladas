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
        

def regresion(mejor, peor, base):
    m = (-1)/(peor - mejor)
    b = -peor*((-1)/(peor-mejor))
    return((base * m) + b)
    
mejores = pd.read_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ext_otrasvariables_20190316.pickle')
#mejores2 = pd.read_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ext_mejores_3.pickle')
#mejores = pd.concat([mejores1, mejores2])


for pp in ['200702', '201408', '201508', '201509']:
    print(pp)

    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios')
    
    #resumen_1 = pd.read_pickle('resumen_tiempo_20181124.pickle')
    #resumen_2 = pd.read_pickle('resumen_tiempo_20181124_2.pickle')
    #resumen_3 = pd.read_pickle('resumen_tiempo_20181124_3.pickle')
    #
    #resumen_1n = pd.concat([resumen_1, resumen_2])
    #resumen = pd.concat([resumen_1n, resumen_3])
    
    resumen1 = pd.read_pickle('resumen_simulaciones_'+pp+'.pickle')
    condi = mejores.fecha.str.contains(pp)
    
    condi[0] = False
    mejores2 = mejores[condi]
    
    resumen = pd.concat([resumen1, mejores2])

    
    #resumen.fecha = resumen.fecha.str[2:]
    #resumen = resumen.reset_index()
    
    #resumen = pd.read_pickle('resumen_tiempo_20181124.pickle') # Este fue el archivo original de la extracción, pero debido a la adición de nuevos datos del caso 5
    
    #fecha de int es 2014080410 Pero sumando 5 horas es igual a 20017020460 <- esta es la hora que se usa en WRF
    
    resumen.fecha.unique()
    
    #Usado para crear un sólo nombre para cada una de las parametrizaciones
    n_fech = resumen.fecha.str[69:-1]
    n_fech = n_fech.str.replace('/', '-')
    n_fech = n_fech.str.replace('_folder', '')
    
    resumen.fecha = n_fech 
    
    
    ###Ajuste de las horas debido a que es UTM -5
    resumen['date'] = pd.to_datetime(resumen.date_1.str.slice(4), 
           format ='%Y-%m-%d_%H:%M:%S', errors='coerce') - np.timedelta64(5, 'h') # Es necesario restar 5 para que se ajuste a las horas Colombia -5 utm
    
    resumen['dom_1'] = resumen.date_1.str.slice(0,3)
    
    
    
    
    
    
    
    #tabla de las alturas
    balideam = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estaciones_altura_20180905.csv')
    #alturas_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/union_b_20180905.csv')
    
    union_b = pd.merge(resumen, balideam, how='outer', on='cod')
    
    
    #Corrección de la temperatura
    union_b['temp'] = (((union_b.al_alos - union_b.alt_1) * 0.0065) + union_b.T2)
    
    resumen_back = union_b
    
    resumen_back.T2 = resumen_back.temp
    
    if pp == '201408':
        resumen_back.fecha = resumen_back.fecha.str[2:]    
    
    
    ### Creación de la tabla de recepción
    
    recep_t = pd.DataFrame({'tipo_1':np.tile(resumen_back.fecha.unique()[1:], 93),
    'dom_1':np.tile(np.repeat(['d01','d02','d03'], len(resumen_back.fecha.unique()[1:])), 31),
    'cod_1':np.repeat((resumen_back.cod.unique())[1:].astype(np.str), (len(resumen_back.fecha.unique()[1:]) * 3))})
    
    recep_t['r2'] = np.NaN
    recep_t['rmse'] = np.NaN
    recep_t['std_1'] = np.NaN
    recep_t['domin_1'] = np.NaN
    recep_t['std_pura'] = np.NaN
    recep_t['std_estandar'] = np.NaN
    recep_t['std_pura_2'] = np.NaN # ADicionado sólo para comparar
    
    
    recoleccion_minim = pd.DataFrame({'cod_1':[],
                              'min_1':[],
                              'max_1':[]})
        
    
    recep_t = pd.DataFrame({'tipo_1':np.tile(resumen_back.fecha.unique()[1:], 93),
    'dom_1':np.tile(np.repeat(['d01','d02','d03'], len(resumen_back.fecha.unique()[1:])), 31),
    'cod_1':np.repeat((resumen_back.cod.unique())[1:].astype(np.str), (len(resumen_back.fecha.unique()[1:]) * 3))})
    
    recep_t['r2'] = np.NaN
    recep_t['rmse'] = np.NaN
    recep_t['std_1'] = np.NaN
    recep_t['domin_1'] = np.NaN
    recep_t['std_pura'] = np.NaN
    recep_t['std_estandar'] = np.NaN
    recep_t['std_pura_2'] = np.NaN # ADicionado sólo para comparar
    
    
    recoleccion_minim = pd.DataFrame({'cod_1':[],
                              'min_1':[],
                              'max_1':[]})
        
    recoleccion_minim_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/simulacion_'+pp+'.csv')                    
    
    
    base_h = []
    estacion_sintmp = []
    estacion_sintmp_col = []
    dist_menor_3 = []
    dist_menor_10 = []
    fecha_min_rec = []
    estaciones_aut = pd.DataFrame({'cod':[],
                                   'inicio':[],
                                   'fin':[]})
    
        
    base_h = []
    estacion_sintmp = []
    estacion_sintmp_col = []
    dist_menor_3 = []
    dist_menor_10 = []
    fecha_min_rec = []
    estaciones_aut = pd.DataFrame({'cod':[],
                                   'inicio':[],
                                   'fin':[]})
        
    step = pd.DateOffset(hours=1)
    
    
    
    
    
    for j in recoleccion_minim_1.cod_1:#[21206990.0]:#
        print(j)
        
        min_2 = []
        max_2 = []
    
    
                
            
        #os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_validados_20180620/')
        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
        valores = os.listdir()
        if 'v_'+str(j)[0:-2]+'_tmp_2m.csv' not in valores:
            estacion_sintmp.append('v_'+str(j)[0:-2]+'_tmp_2m.csv')
            continue
        base_validada = pd.read_csv('v_'+str(j)[0:-2]+'_tmp_2m.csv')
        ####Revisar si esta corrección es correcta
        base_validada.date =  pd.to_datetime(base_validada.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
        #base_validada[['date', 'tmp_2m']].iloc[45655:45675,:]
        if 'tmp_2m' not in base_validada.columns:
            continue
        tmp_real = base_validada[base_validada.val_tmp == 0][['date', 'tmp_2m']]
        tmp_real.date =  pd.to_datetime(tmp_real.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
        
        desvest_std = tmp_real.tmp_2m.std()
        
        estaciones_aut_1 = pd.DataFrame({'cod':[str(j)[0:-2]],
                               'inicio':[tmp_real.date.min()],
                               'fin':[tmp_real.date.max()]})        
    
        estaciones_aut = pd.concat([estaciones_aut, estaciones_aut_1])
        
        if (tmp_real.date.min() > resumen_back.date.max()) | (tmp_real.date.max() < resumen_back.date.min()):
            continue  
        
        ####Voy a hacer una unión de los datos para disminuí la desviación estándar
        fecha_min = recoleccion_minim_1[recoleccion_minim_1.cod_1 == j].min_1#iloc[:,3][0]
        fecha_max = recoleccion_minim_1[recoleccion_minim_1.cod_1 == j].max_1#iloc[:,2][0]
        
        result = pd.DataFrame()
        inicio_date = pd.to_datetime(fecha_min)
        fin_date = pd.to_datetime(fecha_max)
        
        while (inicio_date <= fin_date)[(inicio_date <= fin_date).index[0]]: # Crea una las fechas de las cuales se van a sacar los vlores de desviación estándar
            result = result.append(inicio_date)
            inicio_date += step
        
        result.rename(columns={result.columns[0]:'date'}, inplace=True)
        
        
        indice = recoleccion_minim_1[recoleccion_minim_1.cod_1 == j].index[0]
        
        print(resumen_back.fecha.unique())
        
        
        plt.rcParams["figure.figsize"] = (7,7.5)       
        for i in ['ideam-icm', 'ideam-colombia']:
            print(i) 
            
            
            
            
            for kk in ['d01','d02']:
                print(kk)
                
                
    
    
                
                #base_h.append([tmp_real.tmp_2m.std(), j, i]) # Hay un problema porque aparentemente la desviación estandar no es la misma
                
                desvest_const_1 = tmp_real.tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
                
                tmp_model = resumen_back[(resumen_back.fecha == i) & (resumen_back.cod == j) & (resumen_back.date_1.str.slice(0,3) == kk)].sort_values('date')[['date','T2', 'date_1']]
                
                comparacion = pd.merge(tmp_real, tmp_model, on='date', how='inner')
                

                                       
                if len(comparacion) < 1:
                    dist_menor_10.append(['v_'+str(j)[0:-2]+'_tmp_2m.csv', kk])
                    print('salto')
                    continue
    

    
    
    
    
    
    
    
    
                
                
                #Usado para poder sacar la desciación estándar de los datos más cercanos a la realidad.
                para_desv = tmp_real[(tmp_real.date > fecha_min[indice]) & (tmp_real.date < fecha_max[indice])]
                para_desv_2 = pd.merge(result, para_desv, on='date', how='inner')
                desvest_const = para_desv_2.tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
                print(desvest_const)
                

                if i == 'ideam-colombia':
                    type_1 = '-.'
                    color_1 = 'gray'
                    if kk == 'd02':
                        marker_1 = 'p'
                    else:
                        marker_1 = "^"
                    label_1 = 'ideam-colombia'
                if i == 'ideam-icm':
                    type_1 = '--'
                    color_1 = 'red'
                    if kk == 'd02':
                        marker_1 = 'D'
                    else:
                        marker_1 = "^"
                    label_1 = 'icm'

                
                
                plt.plot_date(comparacion.date, comparacion.T2, color = color_1, linestyle = '-', marker = marker_1, label =label_1+' '+kk)
                
                
                
    
    
        
        plt.plot_date(comparacion.date, comparacion.tmp_2m, '-', color = 'k', label = 'Estación automática')
        
        plt.legend()
        plt.xlabel('Fecha - Hora')
        plt.ylabel('Temperatura °C') 
        plt.xticks(rotation=90)
        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/comparacion_grafica/'+pp+'_'+str(j)[:-2]+'.png' ,dpi = 100, figsize=(20,20))
        plt.close()
    

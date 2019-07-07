#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 23:36:29 2018
Script usado par ala extracción de los valores de las simulaciones 2014
@author: edwin
"""



import os
import pandas as pd
import numpy as np
import datetime
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
from funciones import regresion
from funciones import busca_cod

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios')

#resumen_1 = pd.read_pickle('resumen_tiempo_20181124.pickle')
#resumen_2 = pd.read_pickle('resumen_tiempo_20181124_2.pickle')
#resumen_3 = pd.read_pickle('resumen_tiempo_20181124_3.pickle')
#
#
mejores = pd.read_pickle('ext_icm-icm_3.pickle') # En esta línea van los valores con la corrección con NRMSE
#mejores = pd.concat([mejores1, mejores2])
condi = mejores.fecha.str.contains('201602')
condi = condi.fillna(False)
resumen = mejores[condi]


#resumen = pd.read_pickle('resumen_tiempo_20181124.pickle') # Este fue el archivo original de la extracción, pero debido a la adición de nuevos datos del caso 5

#fecha de int es 2007020410 Pero sumando 5 horas es igual a 20017020460 <- esta es la hora que se usa en WRF

resumen.fecha.unique()

#Usado para crear un sólo nombre para cada una de las parametrizaciones
n_fech = resumen.fecha.str[69:-1]
n_fech = n_fech.str.replace('/', '-')
n_fech = n_fech.str.replace('_folder', '')

resumen.fecha = n_fech 
resumen[resumen.fecha == 'ideam-mejor7']

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


### Creación de la tabla de recepción
recep_t = pd.DataFrame({'tipo_1':np.tile(resumen_back.fecha.unique(), 93),
    'dom_1':np.tile(np.repeat(['d01','d02','d03'], len(resumen_back.fecha.unique())), 31),
    'cod_1':np.repeat((resumen_back.cod.unique()).astype(np.str), (len(resumen_back.fecha.unique()) * 3))})

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
    

#recep_t = pd.DataFrame({'tipo_1':np.tile(resumen_back.fecha.unique()[1:], 93),
#    'dom_1':np.tile(np.repeat(['d01','d02','d03'], len(resumen_back.fecha.unique()[1:])), 31),
#    'cod_1':np.repeat((resumen_back.cod.unique())[1:].astype(np.str), (len(resumen_back.fecha.unique()[1:]) * 3))})
#
#recep_t['r2'] = np.NaN
#recep_t['rmse'] = np.NaN
#recep_t['std_1'] = np.NaN
#recep_t['domin_1'] = np.NaN
#recep_t['std_pura'] = np.NaN
#recep_t['std_estandar'] = np.NaN
#recep_t['std_pura_2'] = np.NaN # ADicionado sólo para comparar
#
#
#recoleccion_minim = pd.DataFrame({'cod_1':[],
#                          'min_1':[],
#                          'max_1':[]})
#    
#recoleccion_minim_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/fechas_min_sel_dom.csv')

#recoleccion_minim_1.max_1 = pd.to_datetime(recoleccion_minim_1.max_1, format ='%Y-%m-%d %H:%M:%S', errors='coerce')
#recoleccion_minim_1.min_1 = pd.to_datetime(recoleccion_minim_1.min_1, format ='%Y-%m-%d %H:%M:%S', errors='coerce')



base_h = []
estacion_sintmp = []
estacion_sintmp_col = []
dist_menor_3 = []
dist_menor_10 = []
fecha_min_rec = []
estaciones_aut = pd.DataFrame({'cod':[],
                               'inicio':[],
                               'fin':[]})
    
 
#for j in resumen_back.cod.unique()[1:]:#[21206950.0]:#
#    #print(j)
#    min_2 = []
#    max_2 = []
#    for i in resumen_back.fecha.unique()[1:10]:
#        #print(i)
#
#            
#        
#        #os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_validados_20180620/')
#        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
#        valores = os.listdir()
#        if 'v_'+str(j)[0:-2]+'_tmp_2m.csv' not in valores:
#            estacion_sintmp.append('v_'+str(j)[0:-2]+'_tmp_2m.csv')
#            continue
#        base_validada = pd.read_csv('v_'+str(j)[0:-2]+'_tmp_2m.csv')
#        ####Revisar si esta corrección es correcta
#        base_validada.date =  pd.to_datetime(base_validada.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
#        #base_validada[['date', 'tmp_2m']].iloc[45655:45675,:]
#        if 'tmp_2m' not in base_validada.columns:
#            continue
#        tmp_real = base_validada[base_validada.val_tmp == 0][['date', 'tmp_2m']]
#        tmp_real.date =  pd.to_datetime(tmp_real.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
#        
##        desvest_std = tmp_real.tmp_2m.std()
##        
##        estaciones_aut_1 = pd.DataFrame({'cod':[str(j)[0:-2]],
##                               'inicio':[tmp_real.date.min()],
##                               'fin':[tmp_real.date.max()]})        
##    
##        estaciones_aut = pd.concat([estaciones_aut, estaciones_aut_1])
#        
#        
#    
#
#        for kk in ['d01']:
#            print(kk)
#            
#            #base_h.append([tmp_real.tmp_2m.std(), j, i]) # Hay un problema porque aparentemente la desviación estandar no es la misma
#            
#            desvest_const_1 = tmp_real.tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
#            
#            tmp_model = resumen_back[(resumen_back.fecha == i) & (resumen_back.cod == j) & (resumen_back.date_1.str.slice(0,3) == kk)].sort_values('date')[['date','T2', 'date_1']]
#            
#            comparacion = pd.merge(tmp_real, tmp_model.drop_duplicates(), on='date', how='inner')
#            #desvest_const = tmp_real[(tmp_real.date > comparacion.date.min()) & (tmp_real.date < comparacion.date.max())].tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
#            
#            desvest_const = tmp_real[(tmp_real.date > comparacion.date.min()) & (tmp_real.date < comparacion.date.max())] # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
#            
#            #print(comparacion.tmp_2m.std(), len(comparacion), len(desvest_const))
#            #print('min', comparacion.date.min(), '    max', comparacion.date.max(), len(desvest_const))
#            
#                                   
#            if len(comparacion) < 10:
#                dist_menor_10.append(['v_'+str(j)[0:-2]+'_tmp_2m.csv', kk])
#                continue
#
#            min_2.append(comparacion.date.min())
#            max_2.append(comparacion.date.max())
#            print(comparacion.date.min())
#            print('--')
#            print(comparacion.date.max())
#            
#            
#    if len(min_2) < 1:
#        continue
#    
#    aaa = pd.DataFrame({'tiem_1':min_2})       
#    fecha_min = pd.DataFrame({'eee':aaa.tiem_1.value_counts()}).index[0]
#    bbb = pd.DataFrame({'tiem_1':max_2})       
#    fecha_max = pd.DataFrame({'eee':bbb.tiem_1.value_counts()}).index[0]
#    
#    
#    recoleccion_minim = recoleccion_minim.append(pd.DataFrame({'cod_1':[j],
#                                                               'min_1':[fecha_min],
#                                                               'max_1':[fecha_max]}))
#    
#    recoleccion_minim_1 = recoleccion_minim
####### Esta tabla se va a guardar ya que a partír de esta se corregiran los demás datos.
#    recoleccion_minim_1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/simulacion_mejor_200702.csv')                    

recoleccion_minim_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/simulacion_mejor_201602.csv')                                    


os.system('spd-say "Process has ended"')





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


for j in recoleccion_minim_1.cod_1:#[21201200.0]:#
    #print(j)
    
    base_series = pd.DataFrame()
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
    
        
    for count, i in enumerate(resumen_back.fecha.unique()):
        print(i) 
    

        for count_2, kk in enumerate(['d01','d02']):
            print(kk)
            


            
            #base_h.append([tmp_real.tmp_2m.std(), j, i]) # Hay un problema porque aparentemente la desviación estandar no es la misma
            
            desvest_const_1 = tmp_real.tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            tmp_model = resumen_back[(resumen_back.fecha == i) & (resumen_back.cod == j) & (resumen_back.date_1.str.slice(0,3) == kk)].sort_values('date')[['date','T2', 'date_1']]
            
            comparacion = pd.merge(tmp_real, tmp_model.drop_duplicates(), on='date', how='inner')
            desvest_const = comparacion.tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            if len(comparacion) < 10:
                continue
            comparacion.columns.values[2] = str(j)[:-2]+'_'+i+'_'+comparacion['date_1'].str[0:3][1]
            #pdb.set_trace()
            if(count == 0) & (count_2 == 0):
                base_series = comparacion.iloc[:,0:3]
            if(count != 0) & (count_2 != 0):
                base_series = pd.merge(base_series, comparacion.iloc[:,0:3], how='outer', on=['date', 'tmp_2m'])

            #pdb.set_trace()
            base_series[str(j)[:-2]+'_'+i+'_'+comparacion['date_1'].str[0:3][1]] = comparacion['T2']

    base_series.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/tablas_estaciones_dominios/tablas_series_201602/'+str(j)[:-2]+'.csv')



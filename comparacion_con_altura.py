#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:06:54 2018
# Script usado para la extracción de los valores de temperatura de los diferentes dominios y
realizar su comparación con las estaciones automáticas
@author: edwin
"""

import os
import pandas as pd
import numpy as np
import pdb

 
def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)
 

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios')
resumen1 = pd.read_pickle('resumen_tmp2.pickle') # Este fue el archivo original de la extracción, pero debido a la adición de nuevos datos del caso 5
resumen2 = pd.read_csv('resumen_tmp2_20180927.csv') # Adición de los datos del caso 5
resumen3 = pd.read_csv('resumen_tmp2_20181022.csv')
#resumen3 = pd.read_csv('resumen_tmp2_20181014.csv') #Usado para los dominios 200701_10_3n


resumen0 = resumen1.append(resumen2.iloc[:,1:])
resumen = resumen0.append(resumen3.iloc[:,1:])
#pdb.set_trace()
alturas_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/union_b_20180905.csv')


alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6/resultados/', 'Simulación 1')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_36_12/resultados/', 'Simulación 2')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200702_wrf/resultados/ideam/colombia', 'Simulación 3')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_6_2/resultados', 'Simulación 4')
##Dominio de 10_3
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3/resultados', 'Simulación 5')
# Nuevos 4 dominios
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3n/resultados', 'Simulación 6')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_12_4e/resultados', 'Simulación 7')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_15_5e/resultados/', 'Simulación 8')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6e/resultados/', 'Simulación 9')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_12_4_1/resultados', 'Simulación 10')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3_1/resultados', 'Simulación 11')
alturas_1.fecha.unique()

alturas_2 = alturas_1.iloc[:,[4,5,7,13,20]]

alturas_2['dom_1'] = alturas_1.date_1.str.slice(0,3)

alturas_2['correc_1'] = (- alturas_2.msnm + alturas_2.al_alos) * 0.0065

###Resúmen de las alturas usadas para el documento de latex
alturas_1['dom_1'] = alturas_1.date_1.str.slice(0,3)

alturas_1['correc_1'] = (- alturas_1.msnm + alturas_1.al_alos) * 0.0065
# Nombre Codigo, fecha dominio, altura del ideam, altura del alos, altura del wps, corrección
# Ojo se debe cargar la función para buscar los nombres de las estaciones eso está en funciones.py
    
with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/correccion_alturas.tex','w') as tf: # Tabla de la corrección de temperatura por altura.
    tf.write(busca_cod(round(alturas_1[['cod', 'fecha', 'dom_1', 'al_ideam', 'al_alos', 'msnm', 'correc_1'
                           ]], 3))[['Nombre','cod', 'fecha', 'dom_1', 'al_ideam', 'al_alos', 'msnm',
    'correc_1']].to_latex(index = False, longtable = True))

###

#'/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6/resultados/','/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_36_12/resultados/','/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3/resultados','/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3n/resultados','/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_12_4e/resultados','/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_15_5e/resultados/','/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6e/resultados/','/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_12_4_1/resultados/', '/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3_1/resultados/'
    
    
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6/resultados/', 'Simulación 1')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_36_12/resultados/', 'Simulación 2')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200702_wrf/resultados/ideam/colombia', 'Simulación 3')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_6_2/resultados', 'Simulación 4')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3/resultados', 'Simulación 5')

resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3n/resultados', 'Simulación 6')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_12_4e/resultados', 'Simulación 7')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_15_5e/resultados/', 'Simulación 8')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6e/resultados/', 'Simulación 9')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_12_4_1/resultados/', 'Simulación 10')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3_1/resultados/', 'Simulación 11')
resumen.fecha.unique()



###Ajuste de las horas
resumen['date'] = pd.to_datetime(resumen.date_1.str.slice(4), 
       format ='%Y-%m-%d_%H:%M:%S', errors='coerce') - np.timedelta64(5, 'h') # Es necesario restar 5 para que se ajuste a las horas Colombia -5 utm

resumen['dom_1'] = resumen.date_1.str.slice(0,3)

#resumen[['cod','fecha','dom_1']]
alturas_3 = alturas_2[['cod','fecha','dom_1', 'correc_1']]

resumen_1 = pd.merge(resumen, alturas_3, on=['cod','fecha','dom_1'], how='outer')

resumen_1['temp'] = (resumen_1.T2 + resumen_1.correc_1)

#resumen_1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/resumen_1_20181022.csv')

#resumen_back = resumen.reset_index()

#resumen_1 = resumen_1.reset_index()

#resumen_back.T2 = resumen_1.temp # Switch para activar o desactivar las correcciones por temperatura

resumen_back = resumen_1

resumen_back.T2 = resumen_back.temp

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
    
 

for j in resumen_back.cod.unique()[1:]:#[21201200.0]:#
    #print(j)
    min_2 = []
    max_2 = []
    for i in resumen_back.fecha.unique()[1:]:
        #print(i)

            
        
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
        
        
    

        for kk in ['d01','d02','d03']:
            print(kk)
            
            #base_h.append([tmp_real.tmp_2m.std(), j, i]) # Hay un problema porque aparentemente la desviación estandar no es la misma
            
            desvest_const_1 = tmp_real.tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            tmp_model = resumen_back[(resumen_back.fecha == i) & (resumen_back.cod == j) & (resumen_back.date_1.str.slice(0,3) == kk)].sort_values('date')[['date','T2', 'date_1']]
            
            comparacion = pd.merge(tmp_real, tmp_model, on='date', how='inner')
            #desvest_const = tmp_real[(tmp_real.date > comparacion.date.min()) & (tmp_real.date < comparacion.date.max())].tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            desvest_const = tmp_real[(tmp_real.date > comparacion.date.min()) & (tmp_real.date < comparacion.date.max())] # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            #print(comparacion.tmp_2m.std(), len(comparacion), len(desvest_const))
            #print('min', comparacion.date.min(), '    max', comparacion.date.max(), len(desvest_const))
            
                                   
            if len(comparacion) < 10:
                dist_menor_10.append(['v_'+str(j)[0:-2]+'_tmp_2m.csv', kk])
                continue

            min_2.append(comparacion.date.min())
            max_2.append(comparacion.date.max())
            
    if len(min_2) < 1:
        continue
            
    recoleccion_minim = recoleccion_minim.append(pd.DataFrame({'cod_1':[j],
                                                               'min_1':[max(min_2)],
                                                               'max_1':[min(max_2)]}))
    
    recoleccion_minim_1 = recoleccion_minim
###### Esta tabla se va a guardar ya que a partír de esta se corregiran los demás datos.
    #recoleccion_minim_1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/fechas_min_sel_dom_20181022.csv')                    
    recoleccion_minim_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/fechas_min_sel_dom_20181022.csv')                    







base_h = []
estacion_sintmp = []
estacion_sintmp_col = []
dist_menor_3 = []
dist_menor_10 = []
fecha_min_rec = []
estaciones_aut = pd.DataFrame({'cod':[],
                               'inicio':[],
                               'fin':[]})
    
 

for j in resumen_back.cod.unique()[1:]:#[21201200.0]:#
    #print(j)
    min_2 = []
    max_2 = []
    for i in resumen_back.fecha.unique()[1:]:
        #print(i)

            
        
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
        
        
    

        for kk in ['d01','d02','d03']:
            print(kk)
            
            #base_h.append([tmp_real.tmp_2m.std(), j, i]) # Hay un problema porque aparentemente la desviación estandar no es la misma
            
            desvest_const_1 = tmp_real.tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            tmp_model = resumen_back[(resumen_back.fecha == i) & (resumen_back.cod == j) & (resumen_back.date_1.str.slice(0,3) == kk)].sort_values('date')[['date','T2', 'date_1']]
            
            comparacion = pd.merge(tmp_real, tmp_model, on='date', how='inner')
            #desvest_const = tmp_real[(tmp_real.date > comparacion.date.min()) & (tmp_real.date < comparacion.date.max())].tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            desvest_const = tmp_real[(tmp_real.date > comparacion.date.min()) & (tmp_real.date < comparacion.date.max())] # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            #print(comparacion.tmp_2m.std(), len(comparacion), len(desvest_const))
            #print('min', comparacion.date.min(), '    max', comparacion.date.max(), len(desvest_const))
            
                                   
            if len(comparacion) < 10:
                dist_menor_10.append(['v_'+str(j)[0:-2]+'_tmp_2m.csv', kk])
                continue

            min_2.append(comparacion.date.min())
            max_2.append(comparacion.date.max())









            
            
            fecha_min = recoleccion_minim_1[recoleccion_minim_1.cod_1 == j].min_1#iloc[:,3][0]
            fecha_max = recoleccion_minim_1[recoleccion_minim_1.cod_1 == j].max_1#iloc[:,2][0]
            
            indice = recoleccion_minim_1[recoleccion_minim_1.cod_1 == j].index[0] # Forma de obtener un valor de índice
            
            desvest_const = tmp_real[(tmp_real.date > fecha_min[indice]) & (tmp_real.date < fecha_max[indice])].tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            position_1 = recep_t[(recep_t.tipo_1 == i) & (recep_t.cod_1 == str(j)) & (recep_t.dom_1 == str(kk))].index[0]
            
                       
            
            #Pearson
            
            recep_t.iloc[position_1, 3] = comparacion['tmp_2m'].corr(comparacion['T2'])
            
            #RMSE
            recep_t.iloc[position_1, 4] = (((comparacion['tmp_2m'] - comparacion['T2']) **2).mean()) ** .5
            # Desviación estándar se restó con el valor de referencia
            recep_t.iloc[position_1, 5] = abs(comparacion['tmp_2m'].std() - comparacion['T2'].std())# Esta desviación se resta contra ella misma para tener en cuenta la desviación de ella misma

            #RMSE            
            #recep_t.iloc[position_1, 4] = (((comparacion['tmp_2m'] - comparacion['T2']) **2).mean()) ** .5
            # Desviación estándar se restó con el valor de referencia
            #recep_t.iloc[position_1, 5] = comparacion['T2'].std()
            
            #Dominio
            
            recep_t.iloc[position_1, 6] = comparacion.date_1.str.slice(0, 3).unique()[0]
            
            #Desviación estándar de la fila
            recep_t.iloc[position_1, 7] = desvest_const
            recep_t.iloc[position_1, 8] = comparacion['T2'].std() # desvaición estándar del modelo
            #recep_t.iloc[position_1, 9]= comparacion['tmp_2m'].std()  # Desviación estándard del empalme sin discriminar el valor mínimo
            
    if len(min_2) < 1:
        continue
            
    recoleccion_minim = recoleccion_minim.append(pd.DataFrame({'cod_1':[j],
                          'min_1':[max(min_2)],
                          'max_1':[min(max_2)]}))
    
    recoleccion_minim_1 = recoleccion_minim
###### Esta tabla se va a guardar ya que a partír de esta se corregiran los demás datos.
    recoleccion_minim_1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/fechas_min_sel_dom.csv')            
            
            


recep_t['r2_esc'] = recep_t.r2# / recep_t.r2.max()
recep_t['rmse_esc'] = 1-(recep_t.rmse / recep_t.rmse.max())
recep_t['std_1_esc'] = 1-(recep_t.std_1 / recep_t.std_1.max())
recep_t['suma_esc'] = (recep_t['r2_esc'] + recep_t['rmse_esc']+recep_t['std_1_esc'])/3 # La suma se multiplica por 2 para darle más peso




############Esta es la tabla con la que se realiza el diagrama de Taylor
recep_t.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181022_con_correccion.csv')        

#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181022_con_correccion.csv')        



#############Resumen de los valores

sin_tmp = pd.DataFrame({'a':estacion_sintmp})
len(sin_tmp.a.unique())

menor_10 = pd.DataFrame({'a':dist_menor_10})
#len(menor_10.a.unique())

# Total hay 31 estaciones
#Hay 10 que se dibujaron, hay 8 que no tienen datos


tabla_ej1 = recep_t[['dom_1', 'tipo_1', 'r2', 'rmse', 'std_1', 'rmse_esc', 'std_1_esc', 'suma_esc']]


tabla_ej1['Código'] = recep_t.cod_1.astype('str').str[:-2]

#tabla_ej1 = tabla_ej1.iloc[:,[10,0,1,2,3,4,6,7,8,9]]
tabla_ej1 = tabla_ej1.iloc[:,[8,1,0,2,3,4,5,6,7]]


tabla_ej1.columns = [['Código','Caso', 'Dominio','Pearson', 'RMSE', 'STD', 'RMSE-esc', 'STD-esc', 'Suma' ]]

tabla_ej1 = tabla_ej1.sort_values(['Caso','Suma'], ascending=[False, False])

tabla_ej2 = tabla_ej1

tabla_ej2['cond'] = (tabla_ej2.Suma > 0.8)

tabla_ej2.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/tabla_final_20181022.csv')        

tabla_ej1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/tabla_final_20181022.csv')        
#tabla_ej1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/tabla_final_20180907.csv')        
        
print(tabla_ej1[-tabla_ej1.Suma.isnull()].iloc[:,:-1].round(4).to_latex(index=False, longtable = True))        
print(tabla_ej1[-tabla_ej1.Suma.isnull()].iloc[:,:-1].round(4).to_latex(index=False, longtable = False))        


##Resumen

#tabla_ej2['cond'] = (tabla_ej2.Suma > 0.8)



####Número de simulaciones 
n_simula = []
for uu in range(1, 12): ### OJO Acá se debe cambiar el número de simulaciones + 1
    n_simula.append('Simulación '+str(uu))
    
resultados_1 = pd.DataFrame({'Simulación':[], 'Dominio':[], 'Resolución':[], 'Valores':[]})
for ii in n_simula:
    #print(ii)
    #print(tabla_ej1[(tabla_ej2.cond == True) & (tabla_ej2.Caso == ii)].Dominio.value_counts())
    salida_1 = tabla_ej1[(tabla_ej2.cond == True) & (tabla_ej2.Caso == ii)].Dominio.value_counts()
    resultados_2 = pd.DataFrame({'Simulación':list(np.repeat(ii, len(salida_1))),
                  'Dominio':list(reversed(salida_1.index)), 'Resolución':list(np.repeat(np.NaN, len(salida_1))),
                  'Valores':list(reversed(salida_1))})
    resultados_1 = pd.concat([resultados_1, resultados_2])
    
print(resultados_1[['Simulación','Dominio','Resolución','Valores']].to_latex(index=False))







######## Tabla del resumen de las estaciones para saber las fechas de incio de las estaciones

import matplotlib.pyplot as plt
    
base_h = []
estacion_sintmp = []
estacion_sintmp_col = []
dist_menor_3 = []
dist_menor_10 = []
fecha_min_rec = []
estaciones_aut = pd.DataFrame({'cod':[],
                               'inicio':[],
                               'fin':[]})
    

fecha_inicio = pd.to_datetime('20070131', format ='%Y%m%d', errors='coerce')
fecha_final = pd.to_datetime('20070203', format ='%Y%m%d', errors='coerce')

fecha_inicio_1 = pd.to_datetime('20070126', format ='%Y%m%d', errors='coerce')
fecha_final_1 = pd.to_datetime('20070208', format ='%Y%m%d', errors='coerce')


#for j in resumen_back.cod.unique()[1:]:#[21201200.0]:#
for j in (estaciones_aut[-estaciones_aut.fin.isnull()].cod + 0.0):
    print(j)
    min_2 = []
    max_2 = []

    #print(i)

        
    
    #os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_validados_20180620/')
    os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
    valores = os.listdir()
    if 'v_'+str(j)[0:-2]+'_tmp_2m.csv' not in valores:
        print('no está')
        estacion_sintmp.append('v_'+str(j)[0:-2]+'_tmp_2m.csv')
        estaciones_aut_2 = pd.DataFrame({'cod':[str(j)[0:-2]],
                           'inicio':['NaN'],
                           'fin':['NaN']})            
        estaciones_aut = pd.concat([estaciones_aut, estaciones_aut_2])
        continue
    base_validada = pd.read_csv('v_'+str(j)[0:-2]+'_tmp_2m.csv')
    ####Revisar si esta corrección es correcta
    base_validada.date =  pd.to_datetime(base_validada.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    #base_validada[['date', 'tmp_2m']].iloc[45655:45675,:]
    if 'tmp_2m' not in base_validada.columns:
        estacion_sintmp_col.append('v_'+str(j)[0:-2]+'_tmp_2m.csv')
        continue
    tmp_real = base_validada[base_validada.val_tmp == 0][['date', 'tmp_2m']]
    tmp_real.date =  pd.to_datetime(tmp_real.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    
    desvest_std = tmp_real.tmp_2m.std()
    
    estaciones_aut_1 = pd.DataFrame({'cod':[str(j)[0:-2]],
                           'inicio':[tmp_real.date.min()],
                           'fin':[tmp_real.date.max()]})        

    #estaciones_aut = pd.concat([estaciones_aut, estaciones_aut_1])
    
    
    para_plt = tmp_real[(tmp_real.date > fecha_inicio_1) & (tmp_real.date < fecha_final_1)]   
    if tmp_real.date.min() > pd.to_datetime('20070204', format ='%Y%m%d', errors='coerce'):
        continue
    if len(para_plt) < 2:
        
        inicio_2 = tmp_real[tmp_real.date < fecha_inicio_1].date.max()
        fin_2 = tmp_real[tmp_real.date > fecha_final_1].date.min()
        
        inicio_3 = inicio_2 - pd.Timedelta('5 days')
        fin_3 = fin_2 + pd.Timedelta('5 days')
        
        para_plt = tmp_real[(tmp_real.date > inicio_3) & (tmp_real.date < fin_3)]   
        
        
    plt.figure(figsize=[11, 9])
    plt.plot_date(para_plt.date, para_plt.tmp_2m, '-', color='lightgray')
    plt.xticks(rotation=90)
    plt.xlabel('Fecha')
    plt.ylabel('°C')
    plt.vlines(x=[fecha_inicio, fecha_final], ymin=(para_plt.tmp_2m.min() - 5), ymax=(para_plt.tmp_2m.max() + 5), color = 'black')
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/automaticas_periodos/'+ str(j)[:-2]+'.png', dpi = 100)
    plt.close()
    
    
    
    
#estaciones_aut.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/resumenestaciones_aut.csv')
estaciones_aut = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/resumenestaciones_aut.csv')
estaciones_aut.fin =  pd.to_datetime(estaciones_aut.fin, format ='%Y-%m-%d %H:%M:%S', errors='coerce')
estaciones_aut.inicio =  pd.to_datetime(estaciones_aut.inicio, format ='%Y-%m-%d %H:%M:%S', errors='coerce')
estaciones_aut = estaciones_aut.sort_values('inicio', ascending=True).reset_index()
## Función creada en el script funciones.py
estaciones_aut = busca_cod(estaciones_aut)
estaciones_aut.index = estaciones_aut.index +1
estaciones_aut_1 = busca_cod(estaciones_aut)

print(estaciones_aut_1[['cod','Nombre' ,'inicio', 'fin']].to_latex(index = True))

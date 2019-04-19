#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:47:48 2018
Script usado para la extracción de los valores de temperatura de las 
parametrizaciones usadas en los diferentes tiempos
@author: edwin
"""


import os
import pandas as pd
import numpy as np


def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios')
resumen = pd.read_pickle('resumen_distancia_20181008.pickle') # Este fue el archivo original de la extracción, pero debido a la adición de nuevos datos del caso 5

alturas_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/union_b_20180905.csv')


#Correccipon de los nombres
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6/resultados/', '18-6-2')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_36_12/resultados/', '36-12-4')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200702_wrf/resultados/ideam/colombia', 'solo2')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_6_2/resultados', '6-2')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3/resultados', '10-3')

alturas_2 = alturas_1.iloc[:,[4,5,7,13,20]]

alturas_2['dom_1'] = alturas_1.date_1.str.slice(0,3)

alturas_2['correc_1'] = (- alturas_2.msnm + alturas_2.al_alos) * 0.0065
#fecha de int es 2007020410 Pero sumando 5 horas es igual a 20017020460 <- esta es la hora que se usa en WRF
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/013018', 'Simulación 1')#108
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/013118', 'Simulación 2')#84
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020118', 'Simulación 3')#60
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020205', 'Simulación 4')#48
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020218', 'Simulación 5')#36
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020305', 'Simulación 6')#24
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020318', 'Simulación 7')#12
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020406', 'Simulación 8')#0

###Ajuste de las horas debido a que es UTM -5
resumen['date'] = pd.to_datetime(resumen.date_1.str.slice(4), 
       format ='%Y-%m-%d_%H:%M:%S', errors='coerce') - np.timedelta64(5, 'h') # Es necesario restar 5 para que se ajuste a las horas Colombia -5 utm

resumen['dom_1'] = resumen.date_1.str.slice(0,3)

#resumen[['cod','fecha','dom_1']]
alturas_3 = alturas_2[['cod','fecha','dom_1', 'correc_1']]

alturas_4 = alturas_3[alturas_3.fecha == '10-3']

resumen_1 = pd.merge(resumen, alturas_4[['cod', 'dom_1', 'correc_1']], on=['cod','dom_1'], how='outer')

resumen_1['temp'] = (resumen_1.T2 + resumen_1.correc_1)

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

base_h = []

for j in resumen_back.cod.unique()[1:]:#[21195160.0]:
    print(j)
    min_2 = []
    max_2 = []
    for i in resumen_back.fecha.unique()[1:]:
        print(i)

            
        
        #os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_validados_20180620/')
        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
        valores = os.listdir()
        if 'v_'+str(j)[0:-2]+'_tmp_2m.csv' not in valores:
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
        

        for kk in ['d01','d02','d03']:
            print(kk)
            
            #base_h.append([tmp_real.tmp_2m.std(), j, i]) # Hay un problema porque aparentemente la desviación estandar no es la misma
            
            desvest_const_1 = tmp_real.tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            tmp_model = resumen_back[(resumen_back.fecha == i) & (resumen_back.cod == j) & (resumen_back.date_1.str.slice(0,3) == kk)].sort_values('date')[['date','T2', 'date_1']]
            
            comparacion = pd.merge(tmp_real, tmp_model.drop_duplicates(), on='date', how='inner')
            #desvest_const = tmp_real[(tmp_real.date > comparacion.date.min()) & (tmp_real.date < comparacion.date.max())].tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            desvest_const = tmp_real[(tmp_real.date > comparacion.date.min()) & (tmp_real.date < comparacion.date.max())] # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            #print(comparacion.tmp_2m.std(), len(comparacion), len(desvest_const))
            #print('min', comparacion.date.min(), '    max', comparacion.date.max(), len(desvest_const))
            
            
            

            
            
            if len(comparacion) < 10:
                continue

            min_2.append(comparacion.date.min())
            max_2.append(comparacion.date.max())
            
            fecha_min = pd.to_datetime('20070204 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
            fecha_max = pd.to_datetime('20070204 18:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
    
            desvest_const = tmp_real[(tmp_real.date > fecha_min) & (tmp_real.date < fecha_max)].tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            #base_h.append([j, i, desvest_const_1, desvest_std]) # Hay un problema porque aparentemente la desviación estandar no es la misma Cambia mucho para hacer los diagramas de Taylor
            
            position_1 = recep_t[(recep_t.tipo_1 == i) & (recep_t.cod_1 == str(j)) & (recep_t.dom_1 == str(kk))].index[0]
            
                       
            
            #Pearson
            
            recep_t.iloc[position_1, 3] = comparacion['tmp_2m'].corr(comparacion['T2'])
            
            #RMSE
            recep_t.iloc[position_1, 4] = ((((comparacion['tmp_2m'] - comparacion['T2']) **2).mean()) ** .500)/(comparacion['T2'].max() - comparacion['T2'].min())
            # Desviación estándar se restó con el valor de referencia
            recep_t.iloc[position_1, 5] = abs(comparacion['tmp_2m'].std() - comparacion['T2'].std())# Esta desviación se resta contra ella misma para tener en cuenta la desviación de ella misma

            #RMSE            
            #recep_t.iloc[position_1, 4] = ((((comparacion['tmp_2m'] - comparacion['T2']) **2).mean()) ** .500)/(comparacion['T2'].max() - comparacion['T2'].min())
            # Desviación estándar se restó con el valor de referencia
            #recep_t.iloc[position_1, 5] = comparacion['T2'].std()
            
            #Dominio
            
            recep_t.iloc[position_1, 6] = comparacion.date_1.str.slice(0, 3).unique()[0]
            
            #Desviación estándar de la fila
            recep_t.iloc[position_1, 7] = desvest_const
            recep_t.iloc[position_1, 8] = comparacion['T2'].std() # desvaición estándar del modelo
            #recep_t.iloc[position_1, 9]= comparacion['tmp_2m'].std()  # Desviación estándard del empalme sin discriminar el valor mínimo
            
            

recep_t.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/distancia_20181008.csv')        
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/distancia_20181008.csv')        

recep_t['r2_esc'] = recep_t.r2# / recep_t.r2.max()
recep_t['rmse_esc'] = 1-(recep_t.rmse / recep_t.rmse.max())
recep_t['std_1_esc'] = 1-(recep_t.std_1 / recep_t.std_1.max())
recep_t['suma_esc'] = (recep_t['r2_esc'] + recep_t['rmse_esc']+recep_t['std_1_esc'])/3 # La suma se multiplica por 2 para darle más peso




recep_t.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/distancia_20181008_2.csv')        
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/distancia_20181008_2.csv')        



tabla_ej1 = recep_t[['dom_1', 'tipo_1', 'r2', 'rmse', 'std_1', 'rmse_esc', 'std_1_esc', 'suma_esc']]


tabla_ej1['Código'] = recep_t.cod_1.astype('str').str[:-2]

#tabla_ej1 = tabla_ej1.iloc[:,[10,0,1,2,3,4,6,7,8,9]]
tabla_ej1 = tabla_ej1.iloc[:,[8,1,0,2,3,4,5,6,7]]


tabla_ej1.columns = [['Código','Caso', 'Dominio','Pearson', 'RMSE', 'STD', 'RMSE-esc', 'STD-esc', 'Suma' ]]

tabla_ej1 = tabla_ej1.sort_values(['Caso','Suma'], ascending=[False, False])

tabla_ej2 = tabla_ej1

tabla_ej2['cond'] = (tabla_ej2.Suma > 0.8)

tabla_ej2.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/distancia_20181008_final.csv')        
tabla_ej1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/distancia_20181008_final.csv')        

        
print(tabla_ej1[-tabla_ej1.Suma.isnull()].iloc[:,:].round(4).to_latex(index=False, longtable = True))        
print(tabla_ej1[-tabla_ej1.Suma.isnull()].iloc[:,:].round(4).to_latex(index=False, longtable = False))        




##Resumen

#tabla_ej2['cond'] = (tabla_ej2.Suma > 0.8)



for ii in tabla_ej2.Caso.unique():
    print(ii)
    print(tabla_ej1[(tabla_ej2.cond == True) & (tabla_ej2.Caso == ii)].Dominio.value_counts())
    

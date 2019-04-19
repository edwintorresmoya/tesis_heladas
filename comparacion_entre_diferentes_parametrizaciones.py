#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 12:32:51 2018

@author: edwin
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios')
resumen = pd.read_pickle('resumen_tmp2.pickle')

#Agregado
alturas_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/union_b_20180905.csv')


alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6/resultados/', '18-6-2')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_36_12/resultados/', '36-12-4')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200702_wrf/resultados/ideam/colombia', 'solo2')
alturas_1.fecha = alturas_1.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_6_2/resultados', '6-2')

alturas_2 = alturas_1.iloc[:,[3,4,6,12,19]]

alturas_2['dom_1'] = alturas_1.date_1.str.slice(0,3)

alturas_2['correc_1'] = (- alturas_2.msnm + alturas_2.al_alos) * 0.0065

resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6/resultados/', '18-6-2')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_36_12/resultados/', '36-12-4')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200702_wrf/resultados/ideam/colombia', 'solo2')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_6_2/resultados', '6-2')


resumen['date'] = pd.to_datetime(resumen.date_1.str.slice(4), format ='%Y-%m-%d_%H:%M:%S', errors='coerce') - np.timedelta64(5, 'h') # Es necesario restar 5 para que se ajuste a las horas Colombia -5 utm


### Creación de la tabla de recepción

recep_t = pd.DataFrame({'tipo_1':np.tile(resumen.fecha.unique()[1:], 93),
'dom_1':np.tile(np.repeat(['d01','d02','d03'], len(resumen.fecha.unique()[1:])), 31),
'cod_1':np.repeat((resumen.cod.unique())[1:].astype(np.str), (len(resumen.fecha.unique()[1:]) * 3))})

recep_t['r2'] = np.NaN
recep_t['rmse'] = np.NaN
recep_t['std_1'] = np.NaN
recep_t['domin_1'] = np.NaN



for i in resumen.fecha.unique()[1:]:
    print(i)
    for j in resumen.cod.unique()[1:]:
        print(j)

            
        
        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_validados_20180620/')
        valores = os.listdir()
        if str(j)[0:-2]+'.csv' not in valores:
            continue
        base_validada = pd.read_csv(str(j)[0:-2]+'.csv')
        
        base_validada.date =  pd.to_datetime(base_validada.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
        if 'tmp_2m' not in base_validada.columns:
            continue
        tmp_real = base_validada[base_validada.val_tmp == 0][['date', 'tmp_2m']]
        tmp_real.date =  pd.to_datetime(tmp_real.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
        
        

        for kk in ['d01','d02','d03']:
            print(kk)
                    
            tmp_model = resumen[(resumen.fecha == i) & (resumen.cod == j) & (resumen.date_1.str.slice(0,3) == kk)].sort_values('date')[['date','T2', 'date_1']]
            
            comparacion = pd.merge(tmp_real, tmp_model, on='date', how='inner')
            
            if len(comparacion) < 10:
                continue
            
            position_1 = recep_t[(recep_t.tipo_1 == i) & (recep_t.cod_1 == str(j)) & (recep_t.dom_1 == str(kk))].index[0]
            
                       
            
            #Pearson
            
            recep_t.iloc[position_1, 3] = comparacion['tmp_2m'].corr(comparacion['T2'])
            
            #RMSE
            recep_t.iloc[position_1, 4] = (((comparacion['tmp_2m'] - comparacion['T2']) **2).mean()) ** .5
            # Desviación estándar se restó con el valor de referencia
            recep_t.iloc[position_1, 5] = abs(comparacion['tmp_2m'].std() - comparacion['T2'].std())
            
            #Dominio
            
            recep_t.iloc[position_1, 6] = comparacion.date_1.str.slice(0, 3).unique()[0]

#recep_t.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_crudo.csv')        
recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_crudo.csv')        

##recep_t = recep_t[(recep_t.cod_1 == '21206990.0') | (recep_t.cod_1 == '21206940.0')]

#Se hizo esta relación para escalar los numeros siendo 1 el mejor valor y cero el peor valor

#Con pendiente positiva            
m_r2 = 1/(recep_t.r2.max()-recep_t.r2.min())
b_r2 = 1- ((1/(recep_t.r2.max()-recep_t.r2.min())) * recep_t.r2.max())

#Con pendiente negativa
m_rmse = -1/(recep_t.rmse.max()-recep_t.rmse.min())
b_rmse = ((1/(recep_t.rmse.max()-recep_t.rmse.min())) * recep_t.rmse.max())


m_std_1 = -1/(recep_t.std_1.max()-recep_t.std_1.min())
b_std_1 = ((1/(recep_t.std_1.max()-recep_t.std_1.min())) * recep_t.std_1.max())

recep_t['r2_esc'] = (recep_t.r2*m_r2 + b_r2)
recep_t['rmse_esc'] = recep_t.rmse*m_rmse + b_rmse
recep_t['std_1_esc'] = recep_t.std_1*m_std_1 + b_std_1
recep_t['suma_esc'] = (recep_t['r2_esc']*2) + recep_t['rmse_esc']+recep_t['std_1_esc'] # La suma se multiplica por 2 para darle más peso

recep_t = recep_t.sort_values('suma_esc', ascending=False)



#recep_t.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem.csv')        
#recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem.csv')        



tabla_ej1 = recep_t.iloc[:,[2,3,4,5,6,7,8,9,10,11]]

tabla_ej1['Código'] = recep_t.cod_1.astype('str').str[:-2]

tabla_ej1 = tabla_ej1.iloc[:,[10,0,1,2,3,4,6,7,8,9]]



tabla_ej1.tipo_1 = tabla_ej1.tipo_1.replace('36-12-4', 'Caso 1')
tabla_ej1.tipo_1 = tabla_ej1.tipo_1.replace('18-6-2', 'Caso 2')
tabla_ej1.tipo_1 = tabla_ej1.tipo_1.replace('6-2', 'Caso 3')
tabla_ej1.tipo_1 = tabla_ej1.tipo_1.replace('solo2', 'Caso 4')

tabla_ej1.columns = [['Código','Dominio','Caso', 'Pearson', 'RMSE', 'STD', 'Pearson-esc','RMSE-esc', 'STD-esc', 'Suma' ]]

tabla_ej1 = tabla_ej1.sort_values(['Código','Suma'], ascending=[False, False])
        
print(tabla_ej1[-tabla_ej1.Suma.isnull()].round(2).to_latex(index=False, longtable = True))        

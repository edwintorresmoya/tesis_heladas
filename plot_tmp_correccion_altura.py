#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:34:25 2018
Códigop echo para hacer las gráficas de la temperatura con y sin la corrección
grafica_comparacion_temperaturas
@author: edwin
"""



import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)

def regresion(mejor, peor, base):
    m = (-1)/(peor - mejor)
    b = -peor*((-1)/(peor-mejor))
    return((base * m) + b)


os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios')
resumen = pd.read_pickle('resumen_tmp2_20181123.pickle') # Este fue el archivo original de la extracción, pero debido a la adición de nuevos datos del caso 5

#fecha de int es 2007020410 Pero sumando 5 horas es igual a 20017020460 <- esta es la hora que se usa en WRF

resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6/resultados/', 'Simulación 1')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_36_12/resultados/', 'Simulación 2')
#resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200702_wrf/resultados/ideam/colombia', 'Simulación 3')
#resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_6_2/resultados', 'Simulación 4')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3/resultados', 'Simulación 3')

resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3n/resultados', 'Simulación 4')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_12_4e/resultados', 'Simulación 5')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_15_5e/resultados/', 'Simulación 6')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6e/resultados/', 'Simulación 7')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_12_4_1/resultados/', 'Simulación 8')
resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_10_3_1/resultados/', 'Simulación 9')





#resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/013018', 'Simulación 1')#108
#resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/013118', 'Simulación 2')#84
#resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020118', 'Simulación 3')#60
#resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020205', 'Simulación 4')#48
#resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020218', 'Simulación 5')#36
#resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020305', 'Simulación 6')#24
#resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020318', 'Simulación 7')#12
#resumen.fecha = resumen.fecha.replace('/scr/hercules1san/meteoro/edwin/wrf/resultados/distancia/020406', 'Simulación 8')#0
resumen.fecha.unique()

###Ajuste de las horas debido a que es UTM -5
resumen['date'] = pd.to_datetime(resumen.date_1.str.slice(4), 
       format ='%Y-%m-%d_%H:%M:%S', errors='coerce') - np.timedelta64(5, 'h') # Es necesario restar 5 para que se ajuste a las horas Colombia -5 utm

resumen['dom_1'] = resumen.date_1.str.slice(0,3)







#tabla de las alturas
balideam = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estaciones_altura_20180905.csv')
#alturas_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/union_b_20180905.csv')
balideam_csv = busca_cod(balideam)

print(balideam_csv[['Nombre', 'al_ideam', 'al_alos']].to_latex())

union_b = pd.merge(resumen, balideam, how='outer', on='cod')
union_b = balideam

fecha_inicio = pd.to_datetime('20070131', format ='%Y%m%d', errors='coerce')
fecha_final = pd.to_datetime('20070205', format ='%Y%m%d', errors='coerce')

#Corrección de la temperatura
union_b['temp'] = (((union_b.al_alos - union_b.alt_1) * 0.0065) + union_b.T2)

##Creación de la tabla de alturas

union_c = busca_cod(union_b)

union_c['alt_corre'] = ((union_b.al_alos - union_b.alt_1) * 0.0065)

union_c.date = pd.to_datetime(union_c.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
valores = os.listdir()
#
#for icod in union_c.cod.unique()[1:]:
#    print(icod)
#    for ifecha in union_c.fecha.unique()[1:]:
#        print(ifecha)
#        for idom in union_c.dom_1.unique()[1:]:
#            print(idom)
#            if len(union_c[(union_c.cod == icod)&(union_c.fecha == ifecha)&
#                           (union_c.dom_1 == idom)&(union_c.date > fecha_inicio)&
#                           (union_c.date < fecha_final)]) > 5:
#                para_pl = union_c[(union_c.cod == icod)&(union_c.fecha == ifecha)&
#                           (union_c.dom_1 == idom)&(union_c.date > fecha_inicio)&
#                           (union_c.date < fecha_final)][['Nombre', 'date','cod', 'fecha', 'dom_1', 'T2', 'temp']]
#                
#                
#                
#                os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
#                if 'v_'+str(icod)[0:-2]+'_tmp_2m.csv' not in valores:
#                    print('no está')
##                    estacion_sintmp.append('v_'+str(j)[0:-2]+'_tmp_2m.csv')
##                    estaciones_aut_2 = pd.DataFrame({'cod':[str(j)[0:-2]],
##                                       'inicio':['NaN'],
##                                       'fin':['NaN']})            
##                    estaciones_aut = pd.concat([estaciones_aut, estaciones_aut_2])
#                    continue
#                base_validada = pd.read_csv('v_'+str(icod)[0:-2]+'_tmp_2m.csv')
#                ####Revisar si esta corrección es correcta
#                base_validada.date =  pd.to_datetime(base_validada.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
#                #base_validada[['date', 'tmp_2m']].iloc[45655:45675,:]
#                if 'tmp_2m' not in base_validada.columns:
#                    print('no tmp')
#                    #estacion_sintmp_col.append('v_'+str(j)[0:-2]+'_tmp_2m.csv')
#                    continue
#                tmp_real = base_validada[base_validada.val_tmp == 0][['date', 'tmp_2m']]
#                tmp_real.date =  pd.to_datetime(tmp_real.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
#                
#                para_pl_2 = pd.merge(left=para_pl, right=tmp_real, on='date', how='left')
#                
#                if len(para_pl_2[para_pl_2.tmp_2m.isnull()]) > 10:
#                    print('no validos_tmp')
#                    continue
#                
#                if len(para_pl_2) > 10:
#                    plt.rcParams["figure.figsize"] = (8,8)
#                    para_pl_2 = para_pl_2.sort_values('date')
#                    plt.plot_date(para_pl_2.date, para_pl_2.tmp_2m, '-', label='Medida', color= 'blue')
#                    plt.plot_date(para_pl_2.date, para_pl_2.T2, '--', label='Modelada', color='gray')
#                    plt.plot_date(para_pl_2.date, para_pl_2.temp, '-', label='Modelada corregida', color='k')
#                    plt.xticks(rotation=90)
#                    plt.legend()
#                    plt.xlabel('Fecha')
#                    plt.ylabel('°C')
#                    plt.title('Estación '+para_pl.Nombre.unique()[0]+str(ifecha)+' domínio '+str(idom))
#                    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_comparacion_temperaturas/' + str(icod)+'_'+str(ifecha)+'_'+str(idom) +'.png' ,dpi = 100)
#                    plt.close()
#                
#
#for i in union_c.columns.unique():
#    print(union_c[i].head())
    
    
    
    
    
    
    
    
    
    
    
    
    

for j in union_c.cod.unique()[1:]:#[21201200.0]:#
    #j = 21206990.0
    print(j)
    min_2 = []
    max_2 = []
    for i in union_c.fecha.unique()[1:]:
        print(i)

            
        
        #os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_validados_20180620/')
        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
        valores = os.listdir()
        if 'v_'+str(j)[0:-2]+'_tmp_2m.csv' not in valores:
            print('no están los valores')
            #estacion_sintmp.append('v_'+str(j)[0:-2]+'_tmp_2m.csv')
            continue
        base_validada = pd.read_csv('v_'+str(j)[0:-2]+'_tmp_2m.csv')
        ####Revisar si esta corrección es correcta
        base_validada.date =  pd.to_datetime(base_validada.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
        #base_validada[['date', 'tmp_2m']].iloc[45655:45675,:]
        if 'tmp_2m' not in base_validada.columns:
            print('no hay temperatura')
            continue
        tmp_real = base_validada[base_validada.val_tmp == 0][['date', 'tmp_2m']]
        tmp_real.date =  pd.to_datetime(tmp_real.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    

        for kk in ['d01','d02','d03']:
            #kk = 'd01'
            print(kk)
            
            tmp_model = union_c[(union_c.fecha == i) & (union_c.cod == j) & (union_c.dom_1 == kk)].sort_values('date')[['date','T2', 'date_1', 'temp']]
            
            para_pl_2 = pd.merge(tmp_real, tmp_model, on='date', how='inner')
            #desvest_const = tmp_real[(tmp_real.date > comparacion.date.min()) & (tmp_real.date < comparacion.date.max())].tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
                                               
            if len(para_pl_2) < 10:
                
                continue
            
            plt.rcParams["figure.figsize"] = (8,8)
            para_pl_2 = para_pl_2.sort_values('date')
            plt.plot_date(para_pl_2.date, para_pl_2.tmp_2m, '-', label='Medida', color= 'blue')
            plt.plot_date(para_pl_2.date, para_pl_2.T2, '--', label='Modelada', color='gray')
            plt.plot_date(para_pl_2.date, para_pl_2.temp, '-', label='Modelada corregida', color='k')
            plt.xticks(rotation=90)
            plt.legend()
            plt.xlabel('Fecha')
            plt.ylabel('°C')
            plt.title('Estación '+un_busca_cod(j)+' '+str(i)+' domínio '+str(kk))
            plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_comparacion_temperaturas/' + str(j)+'_'+str(i)+'_'+str(kk) +'.png' ,dpi = 100)
            plt.close()
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
import pdb

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios')

#resumen_1 = pd.read_pickle('resumen_tiempo_20181124.pickle')
#resumen_2 = pd.read_pickle('resumen_tiempo_20181124_2.pickle')
#resumen_3 = pd.read_pickle('resumen_tiempo_20181124_3.pickle')
#
#resumen_1n = pd.concat([resumen_1, resumen_2])
#resumen = pd.concat([resumen_1n, resumen_3])

#resumen1 = pd.read_pickle('resumen_simulaciones_200702.pickle')
#mejores = pd.read_pickle('ext_mejores.pickle')
#condi = mejores.fecha.str.contains('200702')
#condi[0] = False
#mejores2 = mejores[condi]
#
mejores = pd.read_pickle('ext_icm_3.pickle') # En esta línea van los valores con la corrección con NRMSE
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
    
 
for j in resumen_back.cod.unique():#[21206950.0]:#
    #print(j)
    min_2 = []
    max_2 = []
    for i in resumen_back.fecha.unique()[:10]:
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
        
#        desvest_std = tmp_real.tmp_2m.std()
#        
#        estaciones_aut_1 = pd.DataFrame({'cod':[str(j)[0:-2]],
#                               'inicio':[tmp_real.date.min()],
#                               'fin':[tmp_real.date.max()]})        
#    
#        estaciones_aut = pd.concat([estaciones_aut, estaciones_aut_1])
        
        
    

        for kk in ['d01']:
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
                dist_menor_10.append(['v_'+str(j)[0:-2]+'_tmp_2m.csv', kk])
                continue

            min_2.append(comparacion.date.min())
            max_2.append(comparacion.date.max())
            print(comparacion.date.min())
            print('--')
            print(comparacion.date.max())
            
            
    if len(min_2) < 1:
        continue
    
    aaa = pd.DataFrame({'tiem_1':min_2})       
    fecha_min = pd.DataFrame({'eee':aaa.tiem_1.value_counts()}).index[0]
    bbb = pd.DataFrame({'tiem_1':max_2})       
    fecha_max = pd.DataFrame({'eee':bbb.tiem_1.value_counts()}).index[0]
    
    
    recoleccion_minim = recoleccion_minim.append(pd.DataFrame({'cod_1':[j],
                                                               'min_1':[fecha_min],
                                                               'max_1':[fecha_max]}))
    
    recoleccion_minim_1 = recoleccion_minim
###### Esta tabla se va a guardar ya que a partír de esta se corregiran los demás datos.
    recoleccion_minim_1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/simulacion_mejor_201602.csv')                    

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
    
        
    for i in resumen_back.fecha.unique():
        print(i) 
    

        for kk in ['d01','d02']:
            print(kk)
            


            
            #base_h.append([tmp_real.tmp_2m.std(), j, i]) # Hay un problema porque aparentemente la desviación estandar no es la misma
            
            desvest_const_1 = tmp_real.tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            tmp_model = resumen_back[(resumen_back.fecha == i) & (resumen_back.cod == j) & (resumen_back.date_1.str.slice(0,3) == kk)].sort_values('date')[['date','T2', 'date_1']]
            
            comparacion = pd.merge(tmp_real, tmp_model.drop_duplicates(), on='date', how='inner')
            #desvest_const = tmp_real[(tmp_real.date > comparacion.date.min()) & (tmp_real.date < comparacion.date.max())].tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
#            desvest_const = tmp_real[(tmp_real.date > comparacion.date.min()) & (tmp_real.date < comparacion.date.max())] # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            
            #print(comparacion.tmp_2m.std(), len(comparacion), len(desvest_const))
            #print('min', comparacion.date.min(), '    max', comparacion.date.max(), len(desvest_const))
            
                                   
            if len(comparacion) < 10:
                dist_menor_10.append(['v_'+str(j)[0:-2]+'_tmp_2m.csv', kk])
                print('salto')
                continue

#            min_2.append(comparacion.date.min())
#            max_2.append(comparacion.date.max())



            if recep_t.cod_1.dtype == 'float64':
                recep_t.cod_1 = recep_t.cod_1.astype(str)

            
            
            #Usado para poder sacar la desciación estándar de los datos más cercanos a la realidad.
            para_desv = tmp_real[(tmp_real.date > fecha_min[indice]) & (tmp_real.date < fecha_max[indice])]
            para_desv_2 = pd.merge(result, para_desv, on='date', how='inner')
            desvest_const = comparacion.tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
            print(desvest_const)
            
            position_1 = recep_t[(recep_t.tipo_1 == i) & (recep_t.cod_1 == str(j)) & (recep_t.dom_1 == str(kk))].index[0]
            
                       
            
            #Pearson
            
            recep_t.iloc[position_1, 3] = comparacion['tmp_2m'].corr(comparacion['T2'])
            
            #RMSE
            recep_t.iloc[position_1, 4] = ((((comparacion['tmp_2m'] - comparacion['T2']) **2).mean()) ** .500)/(comparacion['T2'].max() - comparacion['T2'].min())
            # Desviación estándar se restó con el valor de referencia
            recep_t.iloc[position_1, 5] = abs(desvest_const - comparacion['T2'].std())# Esta desviación se resta contra ella misma para tener en cuenta la desviación de ella misma

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
            

recep_t.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/tiempo_salida.csv')        
recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/tiempo_salida.csv')        
base_a = pd.DataFrame({'r2_esc':[np.NaN]})
base_a1 = pd.DataFrame({'rmse_esc':[np.NaN]})
base_a2 = pd.DataFrame({'std_1_esc':[np.NaN]})
            
for pp in recep_t.cod_1.unique():
    base_b = pd.DataFrame({'r2_esc':regresion(mejor=recep_t[recep_t.cod_1 == pp].r2.max(),
              peor=recep_t[recep_t.cod_1 == pp].r2.min(),
              base=recep_t[recep_t.cod_1 == pp].r2)})
    base_a = pd.concat([base_a, base_b])

    base_b1 = pd.DataFrame({'rmse_esc':regresion(mejor=recep_t[recep_t.cod_1 == pp].rmse.min(),
              peor=recep_t[recep_t.cod_1 == pp].rmse.max(),
              base=recep_t[recep_t.cod_1 == pp].rmse)})
    base_a1 = pd.concat([base_a1, base_b1])

    base_b2 = pd.DataFrame({'std_1_esc':regresion(mejor=abs(recep_t[recep_t.cod_1 == pp].std_estandar - 
                                                            recep_t[recep_t.cod_1 == pp].std_pura).min(),
              peor=abs(recep_t[recep_t.cod_1 == pp].std_estandar - 
                                                            recep_t[recep_t.cod_1 == pp].std_pura).max(),
              base=abs(recep_t[recep_t.cod_1 == pp].std_estandar - 
                                                            recep_t[recep_t.cod_1 == pp].std_pura))})
    base_a2 = pd.concat([base_a2, base_b2])
    
    
    
    
    
recep_t['r2_esc'] = base_a.iloc[1:,0]
recep_t['rmse_esc'] = base_a1.iloc[1:,0]
recep_t['std_1_esc'] = base_a2.iloc[1:,0]
#recep_t['aaaa'] = base_a.r2_esc
#
#recep_t['r2_esc'] = recep_t.r2# / recep_t.r2.max()
#recep_t['rmse_esc'] = 1-(recep_t.rmse / recep_t.rmse.max())
#recep_t['std_1_esc'] = 1-(recep_t.std_1 / recep_t.std_1.max())
recep_t['suma_esc'] = (recep_t['r2_esc'] + recep_t['rmse_esc'])/2 # La suma se multiplica por 2 para darle más peso




############Esta es la tabla con la que se realiza el diagrama de Taylor
recep_t.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_mejor_201602.csv')        

recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_mejor_201602.csv')        

os.system('spd-say "Edwin Edwin Edwin Edwin Process has ended"')


#############Resumen de los valores

#sin_tmp = pd.DataFrame({'a':estacion_sintmp})
#len(sin_tmp.a.unique())

#menor_10 = pd.DataFrame({'a':dist_menor_10})
#len(menor_10.a.unique())

# Total hay 31 estaciones
#Hay 11 que se dibujaron, hay 8 que no tienen datos


#tabla_ej1 = recep_t[['dom_1', 'tipo_1', 'r2', 'rmse', 'std_1', 'rmse_esc', 'std_1_esc', 'suma_esc']]
#
#
#tabla_ej1['Código'] = recep_t.cod_1.astype('str').str[:-2]
#
##tabla_ej1 = tabla_ej1.iloc[:,[10,0,1,2,3,4,6,7,8,9]]
#tabla_ej1 = tabla_ej1.iloc[:,[8,1,0,2,3,4,5,6,7]]
#
#
#tabla_ej1.columns = [['Código','Caso', 'Dominio','Pearson', 'RMSE', 'STD', 'RMSE-esc', 'STD-esc', 'Suma' ]]
#
#tabla_ej1 = tabla_ej1.sort_values(['Caso','Suma'], ascending=[False, False])



tabla_ej1 = recep_t[['cod_1', 'tipo_1', 'dom_1', 'r2', 'rmse', 'std_estandar', 'std_1',
                     'rmse_esc', 'std_1_esc', 'r2_esc','suma_esc']]


tabla_ej1['cod_1'] = recep_t.cod_1.astype('str').str[:-2]

#tabla_ej1.tipo_1 = tabla_ej1.tipo_1.str[-2:]

tabla_ej1.columns = ['Código','Simulación', 'Dominio','Pearson', 'RMSE', 'STD', '$STD_{abs}$', 
                      '$RMSE_{esc}$', '$STD_{esc}$', '$Pearson_{esc}$', 'ET' ]


tabla_ej2 = tabla_ej1
tabla_ej2['cond'] = (tabla_ej2.Pearson > 0.8) & (tabla_ej2.RMSE < 0.3)

tabla_ej2.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/simulacion_200702_20190114.csv')        






#tabla_ej1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/tabla_final_20181124_tmp.csv')        
#tabla_ej1.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/tabla_final_20181124_tmp.csv')        

tabla_ej1 = tabla_ej1.sort_values(['Código','Simulación', 'Dominio'], ascending=[False, True,True])
tabla_ej1 = tabla_ej1.reset_index()
tabla_ej1.Código = busca_cod(tabla_ej1, col_cod='Código').Nombre

f = open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/salida_latex_200702.csv','w')

with open('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/salida_200702.csv','w') as f:##Usado para crear un archivo que reciba todas los comandos y se guarden en una hoja
    print(tabla_ej1[-tabla_ej1.ET.isnull()].iloc[:,1:-1].round(4).to_latex(index=False, longtable = True), file= f)        


print(tabla_ej1[-tabla_ej1.ET.isnull()].iloc[:,1:-1].round(4).to_latex(index=False, longtable = True))        
print(tabla_ej1[-tabla_ej1.ET.isnull()].iloc[:,1:-1].round(4).to_latex(index=False, longtable = False))  


##Resumen

#tabla_ej2['cond'] = (tabla_ej2.Suma > 0.8)


    
#####Número de simulaciones 
#n_simula = []
#for uu in range(1, 10): ### OJO Acá se debe cambiar el número de simulaciones + 1
#    n_simula.append('Simulación '+str(uu))
    
resultados_1 = pd.DataFrame({'Simulación':[], 'Dominio':[], 'Resolución':[], 'Valores':[]})
for ii in tabla_ej1.Simulación.unique():
    #print(ii)
    #print(tabla_ej1[(tabla_ej2.cond == True) & (tabla_ej2.Caso == ii)].Dominio.value_counts())
    salida_1 = tabla_ej1[(tabla_ej2.cond == True) & (tabla_ej2.Simulación == ii)].Dominio.value_counts()
    resultados_2 = pd.DataFrame({'Simulación':list(np.repeat(ii, len(salida_1))),
                  'Dominio':list(reversed(salida_1.index)), 'Resolución':list(np.repeat(np.NaN, len(salida_1))),
                  'Valores':list(reversed(salida_1))})
    resultados_1 = pd.concat([resultados_1, resultados_2])
    
print(resultados_1[['Simulación','Dominio','Resolución','Valores']].to_latex(index=False, longtable = True))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:03:14 2019
 Crea las gráficas y las tablas para todas las demás variables que no son temperatura
 En la línea 241 se descomenta para sacar las tablas, de lo contratio saca las gráficas Buscar esto &&&
@author: edwin
"""



import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pdb
from matplotlib.pyplot import figure

def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)
        

def regresion(mejor, peor, base):
    m = (-1)/(peor - mejor)
    b = -peor*((-1)/(peor-mejor))
    return((base * m) + b)
    
def angulo(uu, vv):
    # Función echa para calcular el ángulo dependiendo de las componentes V(Norte - Sur) y U(Oéste - Este)
    # bse_o = pd.DataFrame({'a':[1,2,3], 'b':[4,0,-5]})
    # print(angulo(uu = bse_o.a, vv = bse_o.b))

    hyp = (uu**2 + vv**2)**(1/2)
    theta = (np.arccos(vv / hyp) * 180)/np.pi
    theta_base = []
    for uu_i, theta_i in zip(uu, theta):
        if uu_i < 0:
            theta_i = 360 - theta_i
        theta_base.append(theta_i)

    return theta_base


#mejores2 = pd.read_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ext_otrasvariables.pickle')
#mejores1 = pd.read_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ext_otrasvariables_1.pickle')
##mejores1 = pd.read_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ext_mejores_2.pickle')
##mejores2 = pd.read_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ext_mejores_3.pickle')
#mejores = pd.concat([mejores1, mejores2])
mejores0 = pd.read_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ext_otrasvariables_20190316.pickle')
##
#mejores0 = mejores0[-mejores0.fecha.isnull()]
#mejores0 = mejores0[mejores0.fecha.str.contains('colombia')]


mejores1 = pd.read_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ext_icm_3.pickle') # En esta línea van los valores con la corrección con NRMSE
mejores2 = pd.read_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ext_imc3_20190515.pickle') #Archivo donde viene la parametrización de physics 3

mejores = pd.concat([mejores0, mejores1, mejores2])
mejores = mejores[-mejores.fecha.isnull()]


for pp in ['201602', '201712','200702', '201408', '201508', '201509']:
    print(pp)
    
    for varia_1, pp_col, pp_val, pp_col_wrf, var_y in zip(['_val_dir.csv', '_hum_2m.csv','_val_rad.csv', '_precip_1.csv', '_td.csv', '_wb.csv', '_vel_vi10.csv'],# nombre de las bases
                              ['dir_viento', 'hum_2m', 'rad_1', 'precip_1', 'Td', 'wb', 'vel_vi10'],# Nombre de las columnas en las bases
                              ['val_dir', 'val_hum','val_rad', 'val_prec', 'val_td', 'val_wb', 'val_vv'],# Nombre de las validaciones
                              [['u10','v10'], 'humedad','radiacion','rain', 'dewpoint', 'wetbulb', 'vel_viento'],# Nombre de las variables en WRF
                              ['Dirección', 'Humedad %', r'$Radiación W/m^2$', 'Precipitación mm', '°C', '°C', 'm/s']):#,'_precip_1.csv']

        os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios')
        
        ## Usado para realizar sólo el análisis de la variable de dirección del viento
        if varia_1 == '_val_dir.csv':
            print('salto')
            continue

        
        #resumen_1 = pd.read_pickle('resumen_tiempo_20181124.pickle')
        #resumen_2 = pd.read_pickle('resumen_tiempo_20181124_2.pickle')
        #resumen_3 = pd.read_pickle('resumen_tiempo_20181124_3.pickle')
        #
        #resumen_1n = pd.concat([resumen_1, resumen_2])
        #resumen = pd.concat([resumen_1n, resumen_3])
        
        #resumen1 = pd.read_pickle('resumen_simulaciones_'+pp+'.pickle')
        condi = mejores.fecha.str.contains(pp)
        
        condi[0] = False
        resumen = mejores[condi]
        
        
    
        
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
        
        
        
        resumen.vel_viento = ((resumen.u10)**2+(resumen.v10)**2)**(1/2)
        resumen.dir_viento = ((resumen.u10)**2+(resumen.v10)**2)**(1/2)
        resumen_back = resumen
        
    #    #tabla de las alturas
    #    balideam = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estaciones_altura_20180905.csv')
    #    #alturas_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/union_b_20180905.csv')
    #    
    #    union_b = pd.merge(resumen, balideam, how='outer', on='cod')
    #    
    #    
    #    #Corrección de la temperatura
    #    union_b['temp'] = (((union_b.al_alos - union_b.alt_1) * 0.0065) + union_b.T2)
    #    
    #    resumen_back = union_b
    #    
    #    resumen_back.T2 = resumen_back.temp
        
        if pp == '201408':
            resumen_back.fecha = resumen_back.fecha.str[2:]    
        
        
        ### Creación de la tabla de recepción
        
        
        recep_t = pd.DataFrame({'tipo_1':np.tile(resumen_back.fecha.unique(), 93),
                                'dom_1':np.tile(np.repeat(['d01','d02','d03'], len(resumen_back.fecha.unique())), 31),
                                'cod_1':np.repeat((mejores.cod.unique()).astype(np.str), (len(resumen_back.fecha.unique()) * 3))})
        
        
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
            
        
        
        
        #Esta es la tabla donde se sacan las fechas mínimas para hacer la comparación        
        if (pp == '201602') | (pp == '201712'):
            recoleccion_minim_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/simulacion_mejor_'+pp+'.csv')
        else:

            if (varia_1 == '_td.csv') | (varia_1 == '_wb.csv') | (varia_1 == '_vel_vi10.csv') | (varia_1 == '_val_dir.csv'):
                recoleccion_minim_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/otras_variables/mejores_var_'+pp+'_hum_2m.csv') 
            else:
                recoleccion_minim_1 = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/otras_variables/mejores_var_'+pp+varia_1)                    
        
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
        
        
            os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
            valores = os.listdir()
            if 'v_'+str(j)[0:-2]+varia_1 not in valores:
                estacion_sintmp.append('v_'+str(j)[0:-2]+varia_1)
                continue
            base_validada = pd.read_csv('v_'+str(j)[0:-2]+varia_1)
            ####Revisar si esta corrección es correcta
            base_validada.date =  pd.to_datetime(base_validada.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
            
            if pp_col not in base_validada.columns:
                continue
            tmp_real = base_validada[base_validada[pp_val] == 0][['date', pp_col]]
            tmp_real.date =  pd.to_datetime(tmp_real.date, format ='%Y%m%d %H:%M:%S', errors='coerce')                                

            
            
            
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
            

            
            fig = plt.figure()
            ax = fig.add_axes([0.05, 0.2, 0.8, 0.78])
            fig.set_size_inches(12,5)
            #fig.rcParams["figure.figsize"] = (7,7.5)       
            for i in ['ideam-colombia', 'ideam-icm_3','ideam-icm',]:
                print(i) 
                if i == 'ideam-colombia':
                    cod_2 = 'ideam_c'
                if i == 'ideam-icm_3':
                    cod_2 = 'ideam_3'
                else:
                    cod_2 = 'ideam_i'
                
                
                
                
                for kk in ['d01','d02']:
                    print(kk)
                    
                    
        
        
                    
                    #base_h.append([tmp_real.tmp_2m.std(), j, i]) # Hay un problema porque aparentemente la desviación estandar no es la misma
                    
                    #desvest_const_1 = tmp_real.tmp_2m.std() # Saca la desviación estándar de los valores de las estaciones automáticas a partir de los días
                    
                    if pp_col_wrf == ['u10', 'v10']:
                        resumen_back['dir_vi'] = angulo(resumen_back.u10, resumen_back.v10)
                        pp_col_wrf = 'dir_vi'
                    tmp_model = resumen_back[(resumen_back.fecha == i) & (resumen_back.cod == j) & (resumen_back.date_1.str.slice(0,3) == kk)].sort_values('date')[['date',pp_col_wrf, 'date_1']]
                    comparacion = pd.merge(tmp_real, tmp_model, on='date', how='inner')
    
                                           
                    if len(comparacion) < 10:
                        #dist_menor_10.append(['v_'+str(j)[0:-2]+'_tmp_2m.csv', kk])
                        print('salto')
                        continue
        
    
                    ## Esta línea se usa para generar las tablas usadas para la comparación de los datos &&&
                    comparacion.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/comparacion_grafica_otras_var/tablas/'+pp+'_'+str(j)[:-2]+'_'+cod_2+'_'+kk+pp_col_wrf+'.csv')


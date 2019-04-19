#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:09:40 2018

@author: edwin
"""
#Se seleccionó los valores horarios para poderlos comparar con los datos del wrf
### Se va a crear una base de datos con precipitación, humedad relativa, brillo solar, temperatura, velocidad del viento y dirección del viento


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import style
from pvlib.location import Location
import datetime

def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)
        
def orden(base):
    return(base.sort_values(by='date', ascending=True))

vari = ['cod', 'date', 'precip-10min', 'hum_2m', 'Rad-gl', 'tmp_2m', 'tmp_2m_min', 'tmp_2m_max', 'Vel-vie-10min', 'Dir-vie-10min']

#Carga de los datos

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005')
lista_estaciones_2 = pd.DataFrame(list(os.listdir()))
#i = '21206990.csv'
estaciones = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/catalogo_est_4326.csv')

##Tabla para la inclusión de los datos
#humedad
humedad_tabla = (pd.DataFrame([{'cod':0,
               'isnull':0,
               'total_isnull':0,
               'range':0,
               'diff':0, 
               'total_sinnan':0,
               'No datos':0,
               'P. rango':0,
               'P. diferencia':0,
               'total_total':0}]))# Total de los datos sin contar los NA de la humedad

#Precipitación
prec_tabla = (pd.DataFrame([{'cod':0,
               'isnull':0,
               'total_isnull':0,
               'range':0,
               'total_sinnan':0,
               'No datos':0,
               'P. rango':0,
               'total_total':0}]))# Total de los datos sin contar los NA de la humedad
 
    
#Velocidad del viento

        
vv_tabla = (pd.DataFrame([{'cod':0,
       'isnull':0,
       'total_isnull':0,
       'range':0,
       'diff':0,
       'roll_1':0,
       'P. Rango':0,
       'P. diferencia':0,
       'P. secuencia':0,
       'total_sinnan':0,
       'total_total':0}]))# Total de los datos sin contar los NA de la humedad

    
## Radiación
    
rad_tabla = (pd.DataFrame([{'cod':0,
       'isnull':0,
       'total_isnull':0,
       'range':0,
       'diff':0,
       'sky_1':0,
       'P. Rango':0,
       'P. diferencia':0,
       'P. cielo despejado':0,
       'total_sinnan':0,
       'total_total':0}]))

# Dirección del viento:

dir_tabla = (pd.DataFrame([{'cod':0,
   'isnull':0,
   'total_isnull':0,
   'range':0,
   'total_sinnan':0,
   'P. Rango':0,
   'total_total':0}]))
    
#Tmp tabla

tmp_tabla = (pd.DataFrame([{'cod':0,
   'isnull':0,
   'total_isnull':0,
   'range':0,
   'spikes':0,
   'diff':0,
   'roll':0,
   'P. Rango':0,
   'P. spikes':0,
   'P. diferencia':0,
   'P. roll':0,
   'total_sinnan':0,
   'total_total':0}]))


for i in os.listdir():
#i = '21195160.csv'    
#i = '21206990.csv'  
#i = '21205791.csv'
    
    base = pd.read_csv(i)
    base.date = pd.to_datetime(base.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    base = base.sort_values(by='date', ascending=True)
    base2 = base.iloc[:,np.where(lista_nombres(base).isin(vari) == True)[0]]
    
    n_datos = ((base2.date.max() - base2.date.min())// datetime.timedelta(hours = 1))
    
    #Cambio de los nombres porque no se pueden manejar fácilmente
    
    if 'tmp_2m' not in base2.columns:
            continue
    
    
    #######################Validación de la humedad relativa
    
    if 'hum_2m' in base2.columns:
        
        base_hum = base2.reset_index()[['date', 'hum_2m']]
        
        #Plot del antes
        #plt.plot_date(base_hum.date, base_hum.hum_2m)
        
        # Si el valor es 1 quiere decir que es un dato erroneo
        
        #Quitar los no valores
        
        base_hum['null_1'] = np.where(base_hum.hum_2m.isnull(), 1, 0)
        
        #Límites según Shafer en el artículo de Estevez2011
        
        base_hum['range'] = np.where((base_hum.hum_2m > 0.8) & (base_hum.hum_2m < 103), 0, 1)
        
        # La diferencia de los valores no puede ser superior a 45°C
            # Se le quitan los valores que son NaN para evitar problemas 
        base_hum['diff_0'] = ((abs((base_hum[-base_hum.hum_2m.isnull()].hum_2m) - (base_hum[-base_hum.hum_2m.isnull()].hum_2m.shift(1))) < 45))
        base_hum['diff_1'] = np.where(base_hum.diff_0 == True, 0, 1)
        
        if (n_datos - len(base_hum[base_hum.null_1 == 0])) < 0:
            n_datos = len(base_hum)
        
        ##Tabla para la estadística de la validación
        humedad_tabla = humedad_tabla.append(pd.DataFrame([{'cod':i[0:8], # Código
                       'isnull':(n_datos -len(base_hum[base_hum.null_1 == 0])),
                       'total_isnull':n_datos,
                       'range':base_hum[-base_hum.hum_2m.isnull()].range.sum(),
                       'diff':base_hum[-base_hum.hum_2m.isnull()].diff_1.sum(), 
                       'total_sinnan':len(base_hum[-base_hum.hum_2m.isnull()]),
                       'No datos':((n_datos -len(base_hum[base_hum.null_1 == 0])) * 100)/n_datos,
                       'P. rango':(base_hum[-base_hum.hum_2m.isnull()].range.sum() * 100) / len(base_hum[-base_hum.hum_2m.isnull()]),
                       'P. diferencia':(base_hum[-base_hum.hum_2m.isnull()].diff_1.sum() * 100) / len(base_hum[-base_hum.hum_2m.isnull()]),
                       'total_total':len(base_hum)}]))# Total de los datos sin contar los NA de la humedad
        
        n_datos = ((base2.date.max() - base2.date.min())// datetime.timedelta(hours = 1))
        
        # Test de persistencia para determinar si los valores no están pegados pero no se puede usar en la humedad relativa ya que la humedad alcanza valores de 100% y se puede mantener allí por largas horas en la noche
        
        #base_hum['_roll_1'] = np.where(((base_hum.hum_2m.rolling(window = 5, center = True).std())  > 0.01 ), 0, 1)
        
        ## Resultado final
        
        base2['val_hum'] = np.where((base_hum['null_1'] == 0) & (base_hum['range'] == 0) & (base_hum['diff_1'] == 0), 0, 1)
        
        # =============================================================================
        # plt.plot_date(base_hum.date, base_hum.hum_2m)
        # plt.plot_date(base_hum[base_hum['null_1'] == 0].date, base_hum[base_hum['null_1'] == 0].hum_2m)
        # plt.plot_date(base_hum[base_hum['range'] == 0].date, base_hum[base_hum['range'] == 0].hum_2m)
        # plt.plot_date(base_hum[base_hum['diff_1'] == 0].date, base_hum[base_hum['diff_1'] == 0].hum_2m)
        # plt.plot_date(base_hum[base_hum['_roll_1'] == 0].date, base_hum[base_hum['_roll_1'] == 0].hum_2m)
        # 
        # inicio_1 = pd.to_datetime('2014/02/14 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
        # fin_1 = pd.to_datetime('2014/02/15 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
        # 
        # plt.plot_date(base_hum[(base_hum.date > inicio_1) & (base_hum.date < fin_1)].date , base_hum[(base_hum.date > inicio_1) & (base_hum.date < fin_1)].hum_2m)
        # plt.plot_date(base_hum[(base_hum.date > inicio_1) & (base_hum.date < fin_1)][base_hum['null_1'] == 0][base_hum['range'] == 0][base_hum['diff_1'] == 0].date , base_hum[(base_hum.date > inicio_1) & (base_hum.date < fin_1)][base_hum['null_1'] == 0][base_hum['range'] == 0][base_hum['diff_1'] == 0].hum_2m)
        # #plt.plot_date(base_hum[(base_hum.date > inicio_1) & (base_hum.date < fin_1)][base_hum['null_1'] == 0][base_hum['range'] == 0][base_hum['diff_1'] == 0][base_hum['_roll_1'] == 0].date , base_hum[(base_hum.date > inicio_1) & (base_hum.date < fin_1)][base_hum['null_1'] == 0][base_hum['range'] == 0][base_hum['diff_1'] == 0][base_hum['_roll_1'] == 0].hum_2m)
        # plt.xticks(rotation = 90)
        # 
        # plt.plot_date(base2[base2.val_hum == 0].date, base2[base2.val_hum == 0].hum_2m)
        # =============================================================================
    
    
    ################ Validación de la precipitación
    
    if 'precip-10min' in base2.columns: 
        
        base2.columns.values[np.where(base2.columns.values == 'precip-10min')[0][0]] = 'precip_1'
        
        base_prec = base2.reset_index()[['date', 'precip_1']]
        
        ## Buscar los no valores
        
        base_prec['null_1'] = np.where(base_prec.precip_1.isnull(), 1, 0)
        
        ##Quitar los valores extremos
        
        base_prec['range'] = np.where((base_prec.precip_1 >= 0) & (base_prec.precip_1 < 120), 0, 1)
        
        base2['val_prec'] = np.where((base_prec['null_1'] == 0) & (base_prec['range'] == 0), 0, 1)
    
        ##Tabla para la precipitación
        
         ##Tabla para la estadística de la validación
         
        
        if(n_datos - len(base_prec[base_prec.null_1 == 0])) < 0:
             n_datos = len(base_prec)
         
        prec_tabla = prec_tabla.append(pd.DataFrame([{'cod':i[0:8], #Código
                       'isnull':( n_datos -len(base_prec[base_prec.null_1 == 0])),
                       'total_isnull':n_datos,
                       'range':base_prec[-base_prec.precip_1.isnull()].range.sum(),
                       'total_sinnan':len(base_prec[-base_prec.precip_1.isnull()]),
                       'No datos':(( n_datos -len(base_prec[base_prec.null_1 == 0])) * 100) / n_datos,
                       'P. rango':(base_prec[-base_prec.precip_1.isnull()].range.sum() * 100) / len(base_prec[-base_prec.precip_1.isnull()]),
                       'total_total':len(base2)}]))# Total de los datos sin contar los NA de la humedad
    
        n_datos = ((base2.date.max() - base2.date.min())// datetime.timedelta(hours = 1))
        
    
    # =============================================================================
    # 
    # plt.plot_date(base_prec.date, base_prec.precip_1)
    # plt.plot_date(base_prec[base_prec.range == 0].date, base_prec[base_prec.range == 0].precip_1)
    # plt.plot_date(base2[base2.val_prec == 0].date, base2[base2.val_prec == 0].precip_1)
    # 
    # inicio_1 = pd.to_datetime('2014/05/01 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
    # fin_1 = pd.to_datetime('2014/05/30 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
    # 
    # plt.plot_date(base2.date, base2.precip_1)
    # plt.plot_date(base2[(base2.date > inicio_1) & (base2.date < fin_1)][base2.val_prec == 0].date, base2[(base2.date > inicio_1) & (base2.date < fin_1)][base2.val_prec == 0].precip_1)
    # 
    # plt.xticks(rotation = 90)
    # =============================================================================
    
    
    
    
    ##########################Validación de la velocidad del viento
        
    if 'Vel-vie-10min' in base2.columns:
    
        base2.columns.values[np.where(base2.columns.values == 'Vel-vie-10min')[0][0]] = 'vel_vi10'
        
        base_vv = base2.reset_index()[['date', 'vel_vi10']]
        
        #Plot del antes
        #plt.plot_date(base_vv.date, base_vv.vel_vi10)
        
        # Si el valor es 1 quiere decir que es un dato erroneo
        
        #Quitar los no valores
        
        base_vv['null_1'] = np.where(base_vv.vel_vi10.isnull(), 1, 0)
        
        #Límites según Shafer en el artículo de Estevez2011
        
        base_vv['range'] = np.where((base_vv.vel_vi10 >= 0) & (base_vv.vel_vi10 < 60.3), 0, 1)
        
        # La diferencia de los valores no puede ser superior a 45°C
        
        base_vv['diff_0'] = ((abs((base_vv[-base_vv.vel_vi10.isnull()].vel_vi10) - (base_vv[-base_vv.vel_vi10.isnull()].vel_vi10.shift(1))) < 10))
        base_vv['diff_1'] = np.where(base_vv.diff_0 == True, 0, 1)
        
        # Test de persistencia para determinar si los valores no están pegados pero no se puede usar en la humedad relativa ya que la humedad alcanza valores de 100% y se puede mantener allí por largas horas en la noche
        
        base_vv['_roll_1'] = np.where(((base_vv.vel_vi10.rolling(window = 5, center = True).std())  > 0.01 ), 0, 1)
        
        ##Tabla resúmen para los estadísticos
        
        if (n_datos - len(base_vv[base_vv.null_1 == 0])) < 0:
            n_datos = len(base_vv)
            
        
        vv_tabla = vv_tabla.append(pd.DataFrame([{'cod':i[0:8], #Código
                                                  
                                                                
               'isnull':(n_datos - len(base_vv[base_vv.null_1 == 0])),
               'total_isnull':n_datos,
               'range':base_vv[-base_vv.vel_vi10.isnull()].range.sum(),
               'diff':base_vv[-base_vv.vel_vi10.isnull()].diff_1.sum(),
               'roll_1':base_vv[-base_vv.vel_vi10.isnull()]._roll_1.sum(),
               'No. datos':((n_datos - len(base_vv[base_vv.null_1 == 0])) *100)/n_datos,
               'P. Rango':((base_vv[-base_vv.vel_vi10.isnull()].range.sum()) *100)/len(base_vv[-base_vv.vel_vi10.isnull()]),
               'P. diferencia':( (base_vv[-base_vv.vel_vi10.isnull()].diff_1.sum())*100)/len(base_vv[-base_vv.vel_vi10.isnull()]),
               'P. secuencia':((base_vv[-base_vv.vel_vi10.isnull()]._roll_1.sum()) *100)/len(base_vv[-base_vv.vel_vi10.isnull()]),
               'total_sinnan':len(base_vv[-base_vv.vel_vi10.isnull()]),
               'total_total':len(base2)}]))# Total de los datos sin contar los NA de la humedad

        n_datos = ((base2.date.max() - base2.date.min())// datetime.timedelta(hours = 1))
        
        # =============================================================================
        # plt.plot_date(base_vv.date, base_vv.vel_vi10)
        # plt.plot_date(base_vv[(base_vv.null_1 == 0)].date,
        #               base_vv[(base_vv.null_1 == 0)].vel_vi10)
        # 
        # plt.plot_date(base_vv[(base_vv.range == 0) & (base_vv.null_1 == 0)].date,
        #               base_vv[(base_vv.range == 0) & (base_vv.null_1 == 0)].vel_vi10)
        # 
        # plt.plot_date(base_vv[(base_vv.diff_1 == 0) & (base_vv.range == 0) & (base_vv.null_1 == 0)].date,
        #               base_vv[(base_vv.diff_1 == 0) & (base_vv.range == 0) & (base_vv.null_1 == 0)].vel_vi10)
        # 
        # #plt.plot_date(base_vv[(base_vv._roll_1 == 0) & (base_vv.diff_1 == 0) & (base_vv.range == 0) & (base_vv.null_1 == 0)].date,
        # #              base_vv[(base_vv._roll_1 == 0) & (base_vv.diff_1 == 0) & (base_vv.range == 0) & (base_vv.null_1 == 0)].vel_vi10)
        # 
        # =============================================================================
        
        ## Resultado final
        
        
        
        base2['val_vv'] = np.where(((base_vv.diff_1 == 0) & (base_vv.range == 0) & 
             (base_vv.null_1 == 0)), 0, 1)
        
    
    
    
    ######################################Validación de la radiación
    
    if 'Rad-gl' in base2.columns:
        
        base2.columns.values[np.where(base2.columns.values == 'Rad-gl')[0][0]] = 'rad_1'
        base_rad = base2.reset_index()[['date', 'rad_1']]
        #Quitar los valores con NaN
        
        base_rad['null_1'] = np.where(base_rad.rad_1.isnull(), 1, 0)
        
        #Quitar los valores que estén fuera de rango
        
        base_rad['range'] = np.where((base_rad.rad_1 >= -1) & (base_rad.rad_1 < 1500), 0, 1)
        
        #La diferencia de los datos no puede exceder y si es un Na tomarlo como un dato
        
        base_rad['diff_0'] = (abs((base_rad[-base_rad.rad_1.isnull()].rad_1) - (base_rad[-base_rad.rad_1.isnull()].rad_1.shift(1))) < 555.)
        base_rad['diff_1'] = np.where(base_rad.diff_0 == True, 0, 1)
        
        #Validación de los datos que no se salgan de los valores máximos
        
        tus = Location(float(estaciones[estaciones.cod == int(i[0:8])].LATITUD), float(estaciones[estaciones.cod == int(i[0:8])].LONGITUD), 'America/Bogota')
        base_rad['sky_0'] = tus.get_clearsky(pd.DatetimeIndex(base_rad.date, tz='America/Bogota'))['ghi'].reset_index(drop=True)  # ineichen with climatology table by default
        
        base_rad['sky_1'] = np.where(((base_rad.sky_0 +10) > base_rad.rad_1), 0, 1)
        
        
        ##Tabla de resumen para extracción de las estadísticas
        
        if (n_datos - len(base_rad[base_rad.null_1 == 0])) < 0:
            n_datos = len(base_rad)
        
        rad_tabla = rad_tabla.append(pd.DataFrame([{'cod':i[0:8], #Código
               'isnull':(n_datos - len(base_rad[base_rad.null_1 == 0])),
               'total_isnull':n_datos,
               'range':base_rad[-base_rad.rad_1.isnull()].range.sum(),
               'diff':base_rad[-base_rad.rad_1.isnull()].diff_1.sum(),
               'sky_1':base_rad[-base_rad.rad_1.isnull()].sky_1.sum(),
               'No. datos':((n_datos - len(base_rad[base_rad.null_1 == 0])) *100)/n_datos,
               'P. Rango':( (base_rad[-base_rad.rad_1.isnull()].range.sum())*100)/len(base_rad[-base_rad.rad_1.isnull()]),
               'P. diferencia':((base_rad[-base_rad.rad_1.isnull()].diff_1.sum()) *100)/len(base_rad[-base_rad.rad_1.isnull()]),
               'P. cielo despejado':((base_rad[-base_rad.rad_1.isnull()].sky_1.sum()) *100)/len(base_rad[-base_rad.rad_1.isnull()]),
               'total_sinnan':len(base_rad[-base_rad.rad_1.isnull()]),
               'total_total':len(base2)}]))
        n_datos = ((base2.date.max() - base2.date.min())// datetime.timedelta(hours = 1))
        # =============================================================================
        # plt.plot_date(base_rad.date, base_rad.rad_1)
        # plt.plot_date(base_rad[base_rad.null_1 == 0].date, base_rad[base_rad.null_1 == 0].rad_1)
        # 
        # plt.plot_date(base_rad[(base_rad.range == 0) & (base_rad.null_1 == 0)].date,
        #                        base_rad[(base_rad.range == 0) & (base_rad.null_1 == 0)].rad_1)
        # 
        # plt.plot_date(base_rad[(base_rad.diff_1 == 0) & (base_rad.range == 0) & (base_rad.null_1 == 0)].date,
        #                        base_rad[(base_rad.diff_1 == 0) & (base_rad.range == 0) & (base_rad.null_1 == 0)].rad_1)
        # 
        # 
        # plt.plot_date(base_rad[(base_rad.sky_1 == 0) & (base_rad.diff_1 == 0) & (base_rad.range == 0) & (base_rad.null_1 == 0)].date,
        #                        base_rad[(base_rad.sky_1 == 0) & (base_rad.diff_1 == 0) & (base_rad.diff_1 == 0) & (base_rad.range == 0) & (base_rad.null_1 == 0)].rad_1)
        # 
        # =============================================================================
        
        base2['val_rad'] = np.where(((base_rad.sky_1 == 0) & (base_rad.diff_1 == 0) & 
             (base_rad.range == 0) & (base_rad.null_1 == 0)), 0, 1)
        
        


##################Validación de la dirección del viento
        
    if 'Dir-vie-10min' in base2.columns:
        if 'vel_vi10' in base2.columns:
                    
            base2.columns.values[np.where(base2.columns.values == 'Dir-vie-10min')[0][0]] = 'dir_viento'
            base_dir = base2.reset_index()[['date', 'dir_viento', 'vel_vi10' ]]  
            
            #No valores
            
            base_dir['null_1'] = np.where(((base_dir.dir_viento.isnull()) | base_dir.vel_vi10.isnull()), 1, 0)
            
            # Rangos
            
            base_dir['range'] = np.where((base_dir.dir_viento >= 0) & (base_dir.dir_viento <= 360), 0, 1)
# =============================================================================
#             
#             plt.plot_date(base_dir.date, base_dir.dir_viento)
#             plt.plot_date(base_dir[base_dir.range == 0].date, base_dir[base_dir.range == 0].dir_viento)
#                 
# =============================================================================
            
            ## Tabla de resumen para las estadísticas
            
            if (n_datos - len(base_dir[base_dir.null_1 == 0])) < 0:
                n_datos = len(base_dir)
            
            dir_tabla = dir_tabla.append(pd.DataFrame([{'cod':i[0:8], #Código
               'isnull':(n_datos - len(base_dir[base_dir.null_1 == 0])),
               'total_isnull':n_datos,
               'range':base_dir[-base_dir.dir_viento.isnull()].range.sum(),
               'total_sinnan':len(base_dir[-base_dir.dir_viento.isnull()]),
               'No. datos':((n_datos - len(base_dir[base_dir.null_1 == 0])) *100)/n_datos,
               'P. Rango':((base_dir[-base_dir.dir_viento.isnull()].range.sum()) *100)/len(base_dir[-base_dir.dir_viento.isnull()]),
               'total_total':len(base2)}]))
            n_datos = ((base2.date.max() - base2.date.min())// datetime.timedelta(hours = 1))
            
            base2['val_dir'] = np.where(((base_dir.range == 0) & (base_dir.null_1 == 0)), 0, 1)
       
        
    #######################################"###Validación de la temperatura
    
    if 'tmp_2m' in base2.columns:
        
        if not 'tmp_2m' in base2:
            base2['tmp_2m'] = np.NaN
            
        if not 'tmp_2m_min' in base2:
            base2['tmp_2m_min'] = np.NaN
            
        if not 'tmp_2m_max' in base2:
            base2['tmp_2m_max'] = np.NaN
        
        #if (len(base2.tmp_2m) > 5) & (len(base2.tmp_2m_min) > 5) & (len(base2.tmp_2m_max) > 5):
            
        if (base2.tmp_2m.sum() == 0) & (base2.tmp_2m_min.sum() == 0) & (base2.tmp_2m_max.sum() == 0):
            continue
        
        #Creación de una sola columna de datos de temperatura
        a = base2[-base2.tmp_2m.isnull()][['date','tmp_2m']]
        a.columns = ['date','tmp_2m']
        b = base2[base2.tmp_2m.isnull()& -base2.tmp_2m_min.isnull()][['date','tmp_2m_min']]
        b.columns = ['date', 'tmp_2m']
        c = base2[base2.tmp_2m.isnull()& base2.tmp_2m_min.isnull() & -base2.tmp_2m_max.isnull()][['date','tmp_2m_max']]
        c.columns = ['date','tmp_2m']
        
        dd = pd.merge(on = 'date', left = a, right=b, how = 'outer') # Se pegan las bases para buscar los datos que no están en la base 1 pero están en la base 2
        dd.columns = ['date','tmp_2m_x','tmp_2m']
        
        ee = pd.concat([a, dd[dd.tmp_2m_x.isnull()][['date','tmp_2m']]])
        
        ff = pd.merge(on = 'date', left = ee, right=c, how = 'outer') # Se pegan las bases para buscar los datos que no están en la base 1 pero están en la base 2
        ff.columns = ['date','tmp_2m_x','tmp_2m']
        
        gg = pd.concat([ee, ff[ff.tmp_2m_x.isnull()][['date','tmp_2m']]])
        
        base_tmp = gg.sort_values(by='date', ascending=True)
        
        
        ##Quitar los valores que son na
        
        base_tmp['null_1'] = np.where(base_tmp.tmp_2m.isnull(), 1, 0)
        
        #Quitar los valores que se salen del rango
        
        base_tmp['range'] = np.where((base_tmp.tmp_2m >= -20) & (base_tmp.tmp_2m < 40), 0, 1)
        
        #Pruebas
        
        # Desviación estándar y Promedio
        base_tmp['mean_1'] = base_tmp.tmp_2m.rolling(window=9, center=True, min_periods=1).mean()
        base_tmp['std_2'] = base_tmp.tmp_2m.rolling(window=9, center=True, min_periods=1).std()
        
        #Spikes
        base_tmp['spikes_1'] = np.where((((base_tmp.mean_1 - (base_tmp.std_2 * 1)) > 
              base_tmp.tmp_2m) | (base_tmp.tmp_2m > (base_tmp.mean_1 + 
                    (base_tmp.std_2 * 1)))), 1,0)
        #Las diferencias no pueden ser superires a 4°C
        
        base_tmp['dif_0'] = ((abs((base_tmp[-base_tmp.tmp_2m.isnull()].tmp_2m) - (base_tmp[-base_tmp.tmp_2m.isnull()].tmp_2m.shift(1))) < 4))
        base_tmp['dif_1'] = np.where(base_tmp.dif_0 == True, 0, 1)
        
        
        # Probar que los sensores no estén pegados
        
        base_tmp['roll_1'] = np.where(((base_tmp.tmp_2m.rolling(window = 5, center = True).std())  > 0.01 ), 0, 1)
        
        
        ##Resultados finales
        
        base_tmp['val_tmp'] = np.where(((base_tmp.dif_1 == 0) & (base_tmp.spikes_1 == 0) & (base_tmp.null_1 == 0) & (base_tmp.range == 0) & (base_tmp.spikes_1 == 0)), 0, 1)
        
        if (n_datos - len(base_tmp[base_tmp.null_1 == 0])) < 0:
                n_datos = len(base_tmp)
        
        tmp_tabla = tmp_tabla.append(pd.DataFrame([{'cod':i[0:8], #Código
           'isnull':(n_datos - len(base_tmp[base_tmp.null_1 == 0])),
           'total_isnull':n_datos,
           'range':base_tmp[-base_tmp.tmp_2m.isnull()].range.sum(),
           'spikes':base_tmp[-base_tmp.tmp_2m.isnull()].spikes_1.sum(),
           'diff':base_tmp[-base_tmp.tmp_2m.isnull()].dif_1.sum(),
           'roll':base_tmp[-base_tmp.tmp_2m.isnull()].roll_1.sum(),
           'No. datos':((n_datos - len(base_tmp[base_tmp.null_1 == 0])) *100)/n_datos,
           'P. Rango':((base_tmp[-base_tmp.tmp_2m.isnull()].range.sum()) *100)/len(base_tmp[-base_tmp.tmp_2m.isnull()]),
           'P. spikes':((base_tmp[-base_tmp.tmp_2m.isnull()].spikes_1.sum()) *100)/len(base_tmp[-base_tmp.tmp_2m.isnull()]),
           'P. diferencia':((base_tmp[-base_tmp.tmp_2m.isnull()].dif_1.sum()) *100)/len(base_tmp[-base_tmp.tmp_2m.isnull()]),
           'P. roll':((base_tmp[-base_tmp.tmp_2m.isnull()].roll_1.sum()) *100)/len(base_tmp[-base_tmp.tmp_2m.isnull()]),
           'total_sinnan':len(base_tmp[-base_tmp.tmp_2m.isnull()]),
           'total_total':n_dato}]))
    
        n_datos = ((base2.date.max() - base2.date.min())// datetime.timedelta(hours = 1))
        # =============================================================================
        # 
        # plt.plot_date(base_tmp.date, base_tmp.tmp_2m)
        # plt.plot_date(base_tmp[base_tmp.null_1 == 0].date, base_tmp[base_tmp.null_1 == 0].tmp_2m)
        # plt.plot_date(base_tmp[base_tmp.null_1 == 0][base_tmp.range == 0].date,
        #               base_tmp[base_tmp.null_1 == 0][base_tmp.range == 0].tmp_2m)
        # 
        # plt.plot_date(base_tmp[(base_tmp.null_1 == 0) & (base_tmp.range == 0) & (base_tmp.spikes_1 == 0)].date, base_tmp[(base_tmp.null_1 == 0) & (base_tmp.range == 0) & (base_tmp.spikes_1 == 0)].tmp_2m)
        # 
        # plt.plot_date(base_tmp[(base_tmp.dif_1 == 0) & (base_tmp.spikes_1 == 0) & (base_tmp.null_1 == 0) & (base_tmp.range == 0) & (base_tmp.spikes_1 == 0)].date,
        #                        base_tmp[(base_tmp.dif_1 == 0) & (base_tmp.spikes_1 == 0) & (base_tmp.null_1 == 0) & (base_tmp.range == 0) & (base_tmp.spikes_1 == 0)].tmp_2m)
        # 
        # plt.plot_date(base_tmp[(base_tmp.roll_1 == 0) & (base_tmp.dif_1 == 0) & (base_tmp.spikes_1 == 0) & (base_tmp.null_1 == 0) & (base_tmp.range == 0) & (base_tmp.spikes_1 == 0)].date,
        #                        base_tmp[(base_tmp.roll_1 == 0) & (base_tmp.dif_1 == 0) & (base_tmp.spikes_1 == 0) & (base_tmp.null_1 == 0) & (base_tmp.range == 0) & (base_tmp.spikes_1 == 0)].tmp_2m)
        # 
        # =============================================================================
        
        base_tmp[['date','tmp_2m','val_tmp']]
        
        base2 = pd.merge(on = 'date', left= base2, right= base_tmp[['date','tmp_2m','val_tmp']]) # une la nueva temperatura con la base que se viene trabajando
        
        base2.tmp_2m_x = base2.tmp_2m_y # Se cambia la variable de temperatura
        
        base2 = base2.drop(['tmp_2m_y'], axis=1) # Se elimina la columna de exceso 
        
        base2.columns.values[np.where(base2.columns == 'tmp_2m_x')[0][0]] = 'tmp_2m' 
        

        
    base2.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_validados_20180620/' +i[0:8]+ '.csv')
    
    ##Salidas de las bases de temperatura y otras
    
humedad_tabla.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estadisticas_validacion/' +'humedad'+ '.csv')
prec_tabla.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estadisticas_validacion/' +'precip' +'.csv')
vv_tabla.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estadisticas_validacion/' +'vv' +'.csv')
rad_tabla.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estadisticas_validacion/' +'rad' +'.csv')
dir_tabla.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estadisticas_validacion/' +'dir_tabla' +'.csv')
tmp_tabla.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estadisticas_validacion/' +'tmp_tabla' +'.csv')
    
tmp_tabla
print(tmp_tabla.iloc[1:,[5,0,1,2,3,4,11]].round(2).to_latex(index = False))

humedad_tabla  
print(humedad_tabla.iloc[1:,[3,0,1,2,7]].round(2).to_latex(index = False))

prec_tabla
print(prec_tabla.iloc[1:,[2,0,1,5]].round(2).to_latex(index = False))

rad_tabla
print(rad_tabla.iloc[1:,[4,0,1,2,3,9]].round(2).to_latex(index = False))

vv_tabla
print(vv_tabla.iloc[1:,[4,0,1,2,3,9]].round(2).to_latex(index = False))



dir_tabla
print(dir_tabla.iloc[1:,[2,0,1,5]].round(2).to_latex(index = False))



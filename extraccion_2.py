#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:27:34 2018

@author: edwin
"""


import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
import pandas as pd
import os
import pdb


###################################################

os.chdir('/home/edwin/wrf_b/resultados/') # Ubicación en la carpeta superior donde se encuentran las fechas
#os.chdir('/home/agrometeo/wrf/resultados/automa')

lista_fechas = [col for col in os.listdir() if '_wrf' in col]


estaciones_1 = pd.DataFrame({'cod':[np.NaN], 'latitud':[np.NaN], 'longitud':[np.NaN], 'lat_1':[np.NaN],
                           'lon_1':[np.NaN], 'date_1':[np.NaN], 'T2':[np.NaN], 'rain':[np.NaN], 'humedad':[np.NaN],
                           'radiacion':[np.NaN], 'vel_viento':[np.NaN], 'parametro':[np.NaN], 'combinacion':[np.NaN]})

#################Primera fase de lectura para determinar las ubicaciones de las estaciones


estaciones = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estaciones_con_aut_zona_coordenadas.csv')
#estaciones = pd.read_csv('/home/agrometeo/edwin/estaciones_con_aut_zona_coordenadas.csv')

os.chdir('/home/edwin/wrf_b/resultados/'+lista_fechas[0])
#os.chdir('/home/agrometeo/wrf/resultados/automa/'+lista_fechas[0]+'/resultados')

lista_parametros = os.listdir()


os.chdir('/home/edwin/wrf_b/resultados/'+lista_fechas[0]+'/'+lista_parametros[0])
#os.chdir('/home/agrometeo/wrf/resultados/automa/'+lista_fechas[0]+'/resultados'+'/'+lista_parametros[0]) # entra a la carpeta i

lista_posibilidades = (list(os.listdir()))
   

os.chdir('/home/edwin/wrf_b/resultados/'+lista_fechas[0]+'/'+ lista_parametros[0] +'/'+lista_posibilidades[0])
#os.chdir('/home/agrometeo/wrf/resultados/automa/'+ lista_parametros[0] +'/resultados' +'/'+lista_posibilidades[0])

lista_netcdf = pd.DataFrame(list(os.listdir()))#Busca todos los archivos netCDF
lista_netcdf_1 = lista_netcdf[lista_netcdf[0].str.contains('wrfout')]


f = Dataset(lista_netcdf_1[0][0], 'r')

for i in f.variables:
    print(i, '--')
    try:
        print(f.variables[i].description)
    except AttributeError:
        continue
    
latitud = [50]
longitud = [50]
lon = 0
    
pq0 = 379.90516
a2 = 17.2693882
a3 = 273.16
a4 = 35.86

t2 = (f.variables['T2'][ : ,latitud[lon], longitud[lon]])[0]
q2 = (f.variables['Q2'][ : ,latitud[lon], longitud[lon]][0])
psfc = (f.variables['PSFC'][ : ,latitud[lon], longitud[lon]][0])

f_rh2 = q2 * 100 / ( (pq0 / psfc) * np.exp(a2 * (t2 - a3) / (t2 - a4)) )

estaciones['lat_1'] = 0.03
estaciones['lon_1'] = 0.04

#Extracción de los datos de las ubicaciones

cor_lat = pd.DataFrame(f.variables['XLAT'][0][:]) # Extrae las latitudes
for lat in range(0, len(estaciones)):
    cor_lat2 = pd.DataFrame({'a':cor_lat.iloc[:,0], 'b':abs(cor_lat.iloc[:,0] - estaciones.latitud[lat])}) # Crea una tabla con la latitud y el valor que más se acerca a la coordenada
    #lat_2 = cor_lat2[cor_lat2.b == min(cor_lat2.b)].index.get_values()[0] # Se extrae el valor más cercano para la latitud
    estaciones.lat_1[lat] = cor_lat2[cor_lat2.b == min(cor_lat2.b)].index.get_values()[0] # Se extrae el valor más cercano para la latitud
    
latitud = estaciones.lat_1 #Datos de la grilla que se debe usar

cor_lon = pd.DataFrame(f.variables['XLONG'][0][:])    
for lon in range(0, len(estaciones)):
    cor_lon2 = pd.DataFrame({'a':cor_lon.iloc[0,:], 'b':abs(cor_lon.iloc[0,:] - estaciones.longitud[lon])})
    estaciones.lon_1[lon] = cor_lon2[cor_lon2.b == min(cor_lon2.b)].index.get_values()[0]

longitud = estaciones.lon_1 #Datos de la grilla que se debe usar

os.chdir('/home/edwin/wrf_b/resultados/')
#os.chdir('/home/agrometeo/wrf/resultados/automa')

base_1 = pd.DataFrame({'a': [1]})

for k in lista_fechas:
    print(k)
    os.chdir('/home/edwin/wrf_b/resultados/'+k)
    #os.chdir('/home/agrometeo/wrf/resultados/automa/'+k+'/resultados')
    lista_parametros = os.listdir()
    

    
    
    for i in lista_parametros:# ra_lw_physics, ra_sw_physics, 
        print(i)
        os.chdir('/home/edwin/wrf_b/resultados/'+k+'/'+i)
        #os.chdir('/home/agrometeo/wrf/resultados/automa/'+k+'/resultados/'+i) # entra a la carpeta i
        
        lista_posibilidades = (list(os.listdir()))
           
        for j in lista_posibilidades: # Combinaciones 0,1,2,3,99
            print(j)
            os.chdir('/home/edwin/wrf_b/resultados/'+k+'/'+i+'/'+j)
            #os.chdir('/home/agrometeo/wrf/resultados/automa/'+k+'/resultados/'+i+'/'+j)
            
            lista_netcdf = pd.DataFrame(list(os.listdir()))#Busca todos los archivos netCDF
            lista_netcdf_1 = lista_netcdf[lista_netcdf[0].str.contains('wrfout')]
            
            for lista_1 in lista_netcdf_1[0]:## Loop dentro de los archivos salida del wrf
                print(lista_1)
                #lista_1 = 'wrfout_d01_2007-02-01_00:00:00'
                f = Dataset(lista_1, 'r')
                
                
                
                estaciones = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estaciones_con_aut_zona_coordenadas.csv')
                #estaciones = pd.read_csv('/home/agrometeo/edwin/estaciones_con_aut_zona_coordenadas.csv')
                
                estaciones['lat_1'] = latitud
                estaciones['lon_1'] = longitud
                
                estaciones['date_1'] = lista_1[11:] # extracción de la fecha
                #['cod', 'date', 'precip-10min', 'hum_2m', 'Rad-gl', 'tmp_2m', 'tmp_2m_min', 'tmp_2m_max', 'Vel-vie-10min']
                estaciones['T2'] = np.NaN
                estaciones['rain'] = np.NaN
                estaciones['humedad'] = np.NaN
                estaciones['radiacion'] = np.NaN
                estaciones['u10'] = np.NaN
                estaciones['v10'] = np.NaN
                
                estaciones['parametro'] = i
                estaciones['combinacion'] = j
                estaciones['fecha'] = k
                #####
               
                for lon in range(0, len(estaciones)):
                    estaciones.T2[lon] = (f.variables['T2'][ : ,latitud[lon], longitud[lon]] - 273.15)[0] # Parte de la función que busca los valores de temperatura
                    estaciones.rain[lon] = (f.variables['RAINC'][ : ,latitud[lon], longitud[lon]][0]) + (f.variables['RAINNC'][ : ,latitud[lon], longitud[lon]][0]) # Precipitación
                    estaciones.humedad[lon] = (f.variables['Q2'][ : ,latitud[lon], longitud[lon]][0]) # Humedad
                    estaciones.radiacion[lon] = (f.variables['SWDOWN'][ : ,latitud[lon], longitud[lon]])[0] # Radiación
                    estaciones.u10[lon] = (f.variables['U10'][ : ,latitud[lon], longitud[lon]][0])
                    estaciones.v10[lon] = (f.variables['V10'][ : ,latitud[lon], longitud[lon]][0])
                    
                    print(estaciones.T2[lon])
                
                f.close()
                
                estaciones_1 = estaciones_1.append(estaciones)
                print(estaciones_1.iloc[-5:,:])                 
                           
    
            
            #print(lista_archivos)
        
        
os.chdir('/home/edwin/wrf_b/2_resultados/')
#os.chdir('/home/agrometeo/wrf/resultados/automa_bakup')
estaciones_1.to_pickle('resumen_tmp.pickle')# Escritura del archivo final
estaciones_1.to_csv('resumen_tmp.csv')# Escritura del archivo final



#############
#base2 = estaciones_1

#base2.date_1 = pd.to_datetime(base2.date_1, format ='%Y-%m-%d_%H:%M:%S', errors='coerce')
#base2['cod'] = base2.cod.astype(str).str[0:8]
#base2['tipo'] = base2.cod +'__'+ base2.parametro + '__' + base2.combinacion 
#base3 = base2.pivot_table(values='T2', index=['date_1'], columns=['tipo'])
#base31 = base2.pivot_table(values='T2', index=['date_1'], columns=['cod', 'parametro', 'combinacion'])




for i in mejores.cod.unique():
    if i not in mejores2.cod.unique():
            print(i)
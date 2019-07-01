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
import time


###################################################

os.chdir('/home/edwin/wrf_b/resultados/') # Ubicación en la carpeta superior donde se encuentran las parametrizaciones

lista_parametros = (list(os.listdir()))

estaciones_1 = pd.DataFrame({'cod':[np.NaN], 'latitud':[np.NaN], 'longitud':[np.NaN], 'lat_1':[np.NaN],
                           'lon_1':[np.NaN], 'date_1':[np.NaN], 'T2':[np.NaN], 'parametro':[np.NaN],
                            'combinacion':[np.NaN]})

for i in lista_parametros:# ra_lw_physics, ra_sw_physics, 
    #print(i)
    os.chdir(i) # entra a la carpeta i
    
    lista_posibilidades = (list(os.listdir()))
    
    for j in lista_posibilidades: # Combinaciones 0,1,2,3,99
        #print(j)
        os.chdir(j)
        
        lista_netcdf = pd.DataFrame(list(os.listdir()))#Busca todos los archivos netCDF
        lista_netcdf_1 = lista_netcdf[lista_netcdf[0].str.contains('wrfout')]
        
        for lista_1 in lista_netcdf_1[0]:## Loop dentro de los archivos salida del wrf
            #print(lista_1)
            f = Dataset(lista_1, 'r')
            
            
            estaciones = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estaciones_con_aut_zona_coordenadas.csv')
            
            estaciones['lat_1'] = 0.0
            estaciones['lon_1'] = 0.0
            
            estaciones['date_1'] = lista_1[11:] # extracción de la fecha
            estaciones['T2'] = 0.0
            estaciones['parametro'] = i
            estaciones['combinacion'] = j
            
            #####
            #Función para extracción de los valores de los pixeles de cada capa 
            
            cor_lat = pd.DataFrame(f.variables['XLAT'][0][:])
            for lat in range(0, len(estaciones)):
                print(lat)
                cor_lat2 = pd.DataFrame({'a':cor_lat.iloc[:,0], 'b':abs(cor_lat.iloc[:,0] - estaciones.latitud[lat])})
                estaciones.lat_1[lat] = cor_lat2[cor_lat2.b == min(cor_lat2.b)].index.get_values()[0]
            
            cor_lon = pd.DataFrame(f.variables['XLONG'][0][:])    
            for lon in range(0, len(estaciones)):
                cor_lon2 = pd.DataFrame({'a':cor_lon.iloc[0,:], 'b':abs(cor_lon.iloc[0,:] - estaciones.longitud[lon])})
                estaciones.lon_1[lon] = cor_lon2[cor_lon2.b == min(cor_lon2.b)].index.get_values()[0]
                estaciones.T2[lon] = (f.variables['T2'][ : ,estaciones.lat_1[lon], estaciones.lon_1[lon]] - 273.15)[0] # Parte de la función que busca los valores de temperatura
            
            f.close()
            
            estaciones_1 = estaciones_1.append(estaciones)
            print(estaciones_1.iloc[-5:,:])
                  
            
            
                
        
        #print(lista_archivos)
        
        
        
        os.chdir('/home/edwin/wrf_b/resultados/'+i)
        
    
    os.chdir('/home/edwin/wrf_b/resultados/')
    








            estaciones = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estaciones_con_aut_zona_coordenadas.csv')
            
            estaciones['lat_1'] = 0.0
            estaciones['lon_1'] = 0.0
            
            estaciones['date_1'] = f.variables['XTIME'].description[14:] # extracción de la fecha
            estaciones['T2'] = 0.0
            estaciones['parametro'] = i
            estaciones['combinacion'] = i
            
            #####
            
            f = Dataset('wrfout_d01_2007-02-04_01:00:00', 'r') # Read es para leer
            f.variables['XTIME']
            #Función para extracción de los valores de los pixeles de cada capa 
            
            cor_lat = pd.DataFrame(f.variables['XLAT'][0][:])
            for lat in range(0, len(estaciones)):
                print(lat)
                cor_lat2 = pd.DataFrame({'a':cor_lat.iloc[:,0], 'b':abs(cor_lat.iloc[:,0] - estaciones.latitud[lat])})
                estaciones.lat_1[lat] = cor_lat2[cor_lat2.b == min(cor_lat2.b)].index.get_values()[0]
            
            cor_lon = pd.DataFrame(f.variables['XLONG'][0][:])    
            for lon in range(0, len(estaciones)):
                cor_lon2 = pd.DataFrame({'a':cor_lon.iloc[0,:], 'b':abs(cor_lon.iloc[0,:] - estaciones.longitud[lon])})
                estaciones.lon_1[lon] = cor_lon2[cor_lon2.b == min(cor_lon2.b)].index.get_values()[0]
                estaciones.T2[lon] = (f.variables['T2'][ : ,estaciones.lat_1[lon], estaciones.lon_1[lon]] - 273.15)[0] # Parte de la función que busca los valores de temperatura
            
            f.close() 



#

##### Cargar las coordenadas de las estaciones vienen de formato csv
    
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis')

estaciones = pd.read_csv('estaciones_con_aut_zona_coordenadas.csv')

estaciones['lat_1'] = 0.0
estaciones['lon_1'] = 0.0

estaciones['date_1'] = f.variables['XTIME'].description[14:] # extracción de la fecha
estaciones['T2'] = 0.0

#####

os.chdir('/home/edwin/wrf_b/resultados/physic_a/1_folder')
## &&&
os.chdir('/home/edwin/Downloads/wps/ubicacion_zona')

f = Dataset('wrfout_d01_2007-02-04_17:00:00', 'r')# Read es para leer


#Función para extracción de los valores de los pixeles de cada capa 

cor_lat = pd.DataFrame(f.variables['XLAT'][0][:])
for lat in range(0, len(estaciones)):
    print(lat)
    cor_lat2 = pd.DataFrame({'a':cor_lat.iloc[:,0], 'b':abs(cor_lat.iloc[:,0] - estaciones.latitud[lat])})
    estaciones.lat_1[lat] = cor_lat2[cor_lat2.b == min(cor_lat2.b)].index.get_values()[0]

cor_lon = pd.DataFrame(f.variables['XLONG'][0][:])    
for lon in range(0, len(estaciones)):
    cor_lon2 = pd.DataFrame({'a':cor_lon.iloc[0,:], 'b':abs(cor_lon.iloc[0,:] - estaciones.longitud[lon])})
    estaciones.lon_1[lon] = cor_lon2[cor_lon2.b == min(cor_lon2.b)].index.get_values()[0]
    estaciones.T2[lon] = (f.variables['T2'][ : ,estaciones.lat_1[lon], estaciones.lon_1[lon]] - 273.15)[0] # Parte de la función que busca los valores de temperatura

f.close()



estaciones


lista_netcdf = pd.DataFrame(list(os.listdir()))

lista_netcdf_1 = lista_netcdf[lista_netcdf[0].str.contains('wrfout')]




latbounds = [ 4.691417 ]# Punctual values
lonbounds = [ -74.209 ] # degrees east ? # Valores límites
     
cor_lat2 = pd.DataFrame({'a':cor_lat.iloc[:,0], 'b':abs(cor_lat.iloc[:,0] - latbounds)})
#cor_lat2.index.get_loc(cor_lat2.b == min(cor_lat2.b))
a = cor_lat2[cor_lat2.b == min(cor_lat2.b)].index.get_values()[0]

cor_lon = pd.DataFrame(f.variables['XLONG'][0][:])
cor_lon2 = pd.DataFrame({'a':cor_lon.iloc[0,:], 'b':abs(cor_lon.iloc[0,:] - lonbounds)})
b = cor_lon2[cor_lon2.b == min(cor_lon2.b)].index.get_values()[0]

 

lista_netcdf = pd.DataFrame(list(os.listdir()))

lista_netcdf_1 = lista_netcdf[lista_netcdf[0].str.contains('wrfout')]


f = Dataset('wrfout_d01_2007-01-01_10_00_00', 'r') # Read es para leer

vlr = (f.variables['T2'][ : , [a ,a], bbb] - 273.15)[0]
vlr
#######

lista_netcdf_1 = lista_netcdf[lista_netcdf[0].str.contains('wrfout')]

for i in lista_netcdf_1:
    print(i)

latbounds = [ 4.691417, 4.71, 4.5 ]# Punctual values
lonbounds = [ -74.209, -74.3, -74.1 ] # degrees east ? # Valores límites


cor_lat = pd.DataFrame(f.variables['XLAT'][0][:])
a1 = []
for i in range(0, len(latbounds) - 1)
cor_lat2 = pd.DataFrame({'a':cor_lat.iloc[:,0], 'b':abs(cor_lat.iloc[:,0] - latbounds[0])})
a = cor_lat2[cor_lat2.b == min(cor_lat2.b)].index.get_values()[0]
a1[] = a

f.variables['XLAT']

base_1 = pd.DataFrame({'a': [1]})

for o in f.variables:
    base_1[o] = o
    
base_2 = base_1.transpose()

for pp in base_2.iloc[1]:
    print (pp, f.variables[pp].description)

f.variables['XTIME'].description
f.variables['Times'][:]

len(f.variables)
f.variables['Times'][:]


df = pd.DataFrame({'a':[1,3,5,7,4,5,6,4,7,8,9],
                   'b':[3,5,6,2,4,6,7,8,7,8,9]})
df['a'].values.tolist()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:39:42 2018
Script creado para realizar plots de los datos provenientes del GFS
@author: edwin
"""
#
#def variables_nc(data):
#    for ii in data.variables:
#        print(ii, data.variables[ii].shape)
#        
#        
#def reduction(base, valor=5): ##Función creada para hacer una reducción de la cantidad de vectores presentes en las matrices
#    aa = base[list(np.arange(0, base.shape[0], valor))]
#    bb = aa[:, list(np.arange(0, base.shape[1], valor))]
#    return(bb)
#
##map_1 = Basemap(projection='merc',llcrnrlon=-82.,llcrnrlat=-5.,urcrnrlon=-65.7,urcrnrlat=13.21,resolution='i') # Colombia en Mercator
#
#
#
#
#import numpy as np
#
#from netCDF4 import Dataset
#import matplotlib.pyplot as plt
#from matplotlib.cm import get_cmap
#import cartopy.crs as crs
#from cartopy.feature import NaturalEarthFeature
#import pandas as pd
#
#import os
#os.environ['PROJ_LIB'] = '/home/edwin/anaconda3/share/proj'
#from mpl_toolkits.basemap import Basemap
#
#from wrf import to_np, getvar, smooth2d, get_cartopy, cartopy_xlim, cartopy_ylim, latlon_coords
#
#
#os.chdir('/home/edwin/Downloads/wps/descargas_20180713/1_20070131_20070205_nc')
## Open the NetCDF file
#ncfile = Dataset("2007013000.nc", mode='r')
##ncfile = Dataset("/home/edwin/Downloads/ecwf/salida.nc")
#variables_nc(ncfile)
#
#
#
#for aa in ncfile.variables:
#    print(aa, ncfile.variables[aa].shape)
#
data = []

import pandas as pd
import pygrib

for i in file_1:
    data.append([i.typeOfLevel, i.level, i.name, i.validDate, i.analDate])
    #print(i.typeOfLevel, i.level, i.name, i.validDate, i.analDate)
    print(i.level, i.name, i.validDate, i.analDate)

data_2 = pd.DataFrame(data)
data_2.to_csv('~/Downloads/data.csv')
    

import numpy as np
import os
import pygrib
import matplotlib.pyplot as plt
os.environ['PROJ_LIB'] = '/home/edwin/anaconda3/share/proj'
from mpl_toolkits.basemap import Basemap
from wrf import getvar, interplevel, to_np, latlon_coords, get_cartopy, cartopy_xlim, cartopy_ylim
import shapefile as shp





os.chdir('/home/edwin/Downloads/wps/descargas_20180713/1_20070131_20070205')
file_1 = pygrib.open("2007013000.grb")
# Open the NetCDF file
lista_grib = os.listdir()
lista_grib = sorted(lista_grib)
for uu in lista_grib:
    
    plt.figure()
    file_1 = pygrib.open(uu)
    variable = file_1.select(name='Precipitable water')[0]
    #variable = file_1.select(name='Surface pressure')[0]
    #wind_u = file_1.select(name='10 metre U wind component')[0]
    #wind_v = file_1.select(name='10 metre V wind component')[0]
    #p = file_1.select(name='Cloud water')[0]
    valores = variable.values
    #valores = variable.values -273.15# para el caso de la temperatura es necesatio restar 273.15
    lat,lon = variable.latlons()
    
    #Usado para realizar los plots de todo el mapa
#    m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), 
#      urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(),
#      resolution='c')
    
    m=Basemap(projection='mill',lat_ts=10,llcrnrlon=260, \
      urcrnrlon=330,llcrnrlat=-15,urcrnrlat=50, \
      resolution='c')
    
    
    x, y = m(lon,lat)
    
    cs = m.pcolormesh(x,y,valores,shading='flat',cmap=plt.cm.jet_r) # invertir los colores Invertir los colores sólo se debe agregar '_r' a la paleta del color
    
    m.drawcoastlines()
    #m.fillcontinents()
    m.drawmapboundary()
    m.drawparallels(np.arange(-90.,120.,10.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,10.),labels=[0,0,0,1])
    
    
    plt.colorbar(cs,orientation='vertical')
    plt.title('')
    plt.title('Agua precipitable $kg/m^2$ (mbar).')
    
    #plt.barbs(x, y, wind_u, wind_v)
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_tm/' + str(uu)+'.png', figsize=(20,10) ,dpi = 199)
    plt.close()


def reduction(base, valor=5): ##Función creada para hacer una reducción de la cantidad de vectores presentes en las matrices
    aa = base[list(np.arange(0, base.shape[0], 5))]
    bb = aa[:, list(np.arange(0, base.shape[1], 5))]
    return(bb)

##BArbas
    ##BArbas
    ##BArbas
# Plot de las barbas y temperatura a 10 metros sobre la superficie
#
#   A 10METROS
#    

for uu in lista_grib:
    #print('hola')
    plt.figure()
    file_1 = pygrib.open(uu)
    variable = file_1.select(name='2 metre temperature')[0]
    #variable = file_1.select(name='Cloud water')[0]
    wind_u = file_1.select(name='10 metre U wind component')[0].values
    wind_v = file_1.select(name='10 metre V wind component')[0].values
    p = file_1.select(name='Cloud water')[0]
    #valores = variable.values
    valores = variable.values -273.15# para el caso de la temperatura es necesatio restar 273.15
    lat,lon = variable.latlons()
    
    
    #m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \ # Usado para realizar los plots de todo el mapa
    #  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
    #  resolution='c')
    
    m=Basemap(projection='mill',lat_ts=20,llcrnrlon=240, \
      urcrnrlon=350,llcrnrlat=-25,urcrnrlat=60, \
      resolution='c')  
    
    
    x, y = m(lon,lat)
    
    cs = m.pcolormesh(x,y,valores,shading='flat',cmap=plt.cm.jet)
    m.barbs(reduction(x), reduction(y), reduction(wind_u), reduction(wind_v), rounding=False,
            sizes=dict(emptybarb=0.05, spacing=0.2, height=0.3))
    m.drawcoastlines(color = 'w', linewidth=2.0)
    
    #m.fillcontinents()
    m.drawmapboundary()
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
    
    
    plt.colorbar(cs,orientation='vertical')
    
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    plt.title('Viento '+str(uu)[0:10])
#    plt.barbs(x, y, wind_u, wind_v)
    #plt.barbs(x[list(np.arange(0,181,1))][list(np.arange(0,181,1))], y[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_u[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_v[list(np.arange(0,181,1))][list(np.arange(0,181,1))])
    #plt.barbs(x[list(np.arange(0,181,2))][list(np.arange(0,181,2))], y[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_u[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_v[list(np.arange(0,181,2))][list(np.arange(0,181,2))])
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    
    
    
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_grib_barbas/' + str(uu)+'.png', figsize=(20,10) ,dpi = 199)
    plt.close()

##### A 750 mb


for uu in lista_grib:
    #print('hola')
    plt.figure()
    file_1 = pygrib.open(uu)
    variable = file_1.select(name='2 metre temperature')[0]
    #variable = file_1.select(name='Cloud water')[0]
    wind_u = file_1.select(name='U component of wind', level=(750))[0].values
    wind_v = file_1.select(name='V component of wind', level=(750))[0].values    
    p = file_1.select(name='Cloud water')[0]
    #valores = variable.values
    valores = variable.values -273.15# para el caso de la temperatura es necesatio restar 273.15
    lat,lon = variable.latlons()
    
    
    #m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \ # Usado para realizar los plots de todo el mapa
    #  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
    #  resolution='c')
    
    m=Basemap(projection='mill',lat_ts=20,llcrnrlon=240, \
      urcrnrlon=350,llcrnrlat=-25,urcrnrlat=60, \
      resolution='c')  
    
    
    x, y = m(lon,lat)
    
    cs = m.pcolormesh(x,y,valores,shading='flat',cmap=plt.cm.jet)
    m.barbs(reduction(x), reduction(y), reduction(wind_u), reduction(wind_v), rounding=False,
            sizes=dict(emptybarb=0.05, spacing=0.2, height=0.3))
    m.drawcoastlines(color = 'w', linewidth=2.0)
    
    #m.fillcontinents()
    m.drawmapboundary()
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
    
    
    plt.colorbar(cs,orientation='vertical')
    
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    plt.title('Viento 750 mb '+str(uu)[0:10])
#    plt.barbs(x, y, wind_u, wind_v)
    #plt.barbs(x[list(np.arange(0,181,1))][list(np.arange(0,181,1))], y[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_u[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_v[list(np.arange(0,181,1))][list(np.arange(0,181,1))])
    #plt.barbs(x[list(np.arange(0,181,2))][list(np.arange(0,181,2))], y[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_u[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_v[list(np.arange(0,181,2))][list(np.arange(0,181,2))])
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    
    
    
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_grib_barbas_750/' + str(uu)+'.png', figsize=(20,10) ,dpi = 199)
    plt.close()


##### A 500 mb  #############################################################


for uu in lista_grib:
    #print('hola')
    plt.figure()
    file_1 = pygrib.open(uu)
    variable = file_1.select(name='2 metre temperature')[0]
    #variable = file_1.select(name='Cloud water')[0]
    wind_u = file_1.select(name='U component of wind', level=(500))[0].values
    wind_v = file_1.select(name='V component of wind', level=(500))[0].values    
    p = file_1.select(name='Cloud water')[0]
    #valores = variable.values
    valores = variable.values -273.15# para el caso de la temperatura es necesatio restar 273.15
    lat,lon = variable.latlons()
    
    
    #m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \ # Usado para realizar los plots de todo el mapa
    #  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
    #  resolution='c')
    
    m=Basemap(projection='mill',lat_ts=20,llcrnrlon=240, \
      urcrnrlon=350,llcrnrlat=-25,urcrnrlat=60, \
      resolution='c')  
    
    
    x, y = m(lon,lat)
    
    cs = m.pcolormesh(x,y,valores,shading='flat',cmap=plt.cm.jet)
    m.barbs(reduction(x), reduction(y), reduction(wind_u), reduction(wind_v), rounding=False,
            sizes=dict(emptybarb=0.05, spacing=0.2, height=0.3))
    m.drawcoastlines(color = 'w', linewidth=2.0)
    
    #m.fillcontinents()
    m.drawmapboundary()
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
    
    
    plt.colorbar(cs,orientation='vertical')
    
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    plt.title('Viento 750 mb '+str(uu)[0:10])
#    plt.barbs(x, y, wind_u, wind_v)
    #plt.barbs(x[list(np.arange(0,181,1))][list(np.arange(0,181,1))], y[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_u[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_v[list(np.arange(0,181,1))][list(np.arange(0,181,1))])
    #plt.barbs(x[list(np.arange(0,181,2))][list(np.arange(0,181,2))], y[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_u[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_v[list(np.arange(0,181,2))][list(np.arange(0,181,2))])
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    
    
    
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_grib_barbas_500/' + str(uu)+'.png', figsize=(20,10) ,dpi = 199)
    plt.close()


##### A 250 mb  #############################################################


for uu in lista_grib:
    #print('hola')
    plt.figure()
    file_1 = pygrib.open(uu)
    variable = file_1.select(name='2 metre temperature')[0]
    #variable = file_1.select(name='Cloud water')[0]
    wind_u = file_1.select(name='U component of wind', level=(250))[0].values
    wind_v = file_1.select(name='V component of wind', level=(250))[0].values    
    p = file_1.select(name='Cloud water')[0]
    #valores = variable.values
    valores = variable.values -273.15# para el caso de la temperatura es necesatio restar 273.15
    lat,lon = variable.latlons()
    
    
    #m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \ # Usado para realizar los plots de todo el mapa
    #  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
    #  resolution='c')
    
    m=Basemap(projection='mill',lat_ts=20,llcrnrlon=240, \
      urcrnrlon=350,llcrnrlat=-25,urcrnrlat=60, \
      resolution='c')  
    
    
    x, y = m(lon,lat)
    
    cs = m.pcolormesh(x,y,valores,shading='flat',cmap=plt.cm.jet)
    m.barbs(reduction(x), reduction(y), reduction(wind_u), reduction(wind_v), rounding=False,
            sizes=dict(emptybarb=0.05, spacing=0.2, height=0.3))
    m.drawcoastlines(color = 'w', linewidth=2.0)
    
    #m.fillcontinents()
    m.drawmapboundary()
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
    
    
    plt.colorbar(cs,orientation='vertical')
    
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    plt.title('Viento 750 mb '+str(uu)[0:10])
#    plt.barbs(x, y, wind_u, wind_v)
    #plt.barbs(x[list(np.arange(0,181,1))][list(np.arange(0,181,1))], y[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_u[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_v[list(np.arange(0,181,1))][list(np.arange(0,181,1))])
    #plt.barbs(x[list(np.arange(0,181,2))][list(np.arange(0,181,2))], y[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_u[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_v[list(np.arange(0,181,2))][list(np.arange(0,181,2))])
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    
    
    
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_grib_barbas_250/' + str(uu)+'.png', figsize=(20,10) ,dpi = 199)
    plt.close()













###########################Plot de las streamlines

## A NIVEL DEL SUELO
  
    
# Plot de stream_lines
for uu in lista_grib:
    
    plt.figure()
    file_1 = pygrib.open(uu)
    variable = file_1.select(name='Precipitable water')[0]
    #variable = file_1.select(name='Cloud water')[0]
    wind_u = file_1.select(name='10 metre U wind component')[0].values
    wind_v = file_1.select(name='10 metre V wind component')[0].values
    p = file_1.select(name='Cloud water')[0]
    valores = variable.values
    #valores = variable.values -273.15# para el caso de la temperatura es necesatio restar 273.15
    lat,lon = variable.latlons()
    
    
    #m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \ # Usado para realizar los plots de todo el mapa
    #  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
    #  resolution='c')
    
#    m=Basemap(projection='mill',lat_ts=40,llcrnrlon=250, \
#      urcrnrlon=350,llcrnrlat=-20,urcrnrlat=25, \
#      resolution='c')

    m=Basemap(projection='mill',lat_ts=20,llcrnrlon=240, \
      urcrnrlon=350,llcrnrlat=-25,urcrnrlat=60, \
      resolution='c')    
    
    
    x, y = m(lon,lat)
    
    cs = m.pcolormesh(x,y,valores,shading='flat',cmap=plt.cm.jet)
#    m.barbs(x, y, wind_u, wind_v, rounding=False,
#         sizes=dict(emptybarb=0.0, spacing=0.2, height=0.3))
    
    plt.streamplot(x, y, wind_u, wind_v, color='k', density=[5, 5])
    m.drawcoastlines(color = 'r', linewidth=2.0)
    
    #m.fillcontinents()
    m.drawmapboundary()
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
    
    
    plt.colorbar(cs,orientation='vertical')
    
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    plt.title('Agua Precipitable')
#    plt.barbs(x, y, wind_u, wind_v)
    #plt.barbs(x[list(np.arange(0,181,1))][list(np.arange(0,181,1))], y[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_u[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_v[list(np.arange(0,181,1))][list(np.arange(0,181,1))])
    #plt.barbs(x[list(np.arange(0,181,2))][list(np.arange(0,181,2))], y[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_u[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_v[list(np.arange(0,181,2))][list(np.arange(0,181,2))])
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    
    
    
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_grib_jet_lines/' + str(uu)[0:10]+'.png', figsize=(20,10) ,dpi = 199)
    plt.close()
    

##### A 750 mb

## A NIVEL DEL 750 MB

for uu in lista_grib:
    #print('hola')
    plt.figure()
    file_1 = pygrib.open(uu)
    variable = file_1.select(name='2 metre temperature')[0]
    #variable = file_1.select(name='Cloud water')[0]
    wind_u = file_1.select(name='U component of wind', level=(750))[0].values
    wind_v = file_1.select(name='V component of wind', level=(750))[0].values    
    p = file_1.select(name='Cloud water')[0]
    
    valores = variable.values
    lat,lon = variable.latlons()
    
    
    #m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \ # Usado para realizar los plots de todo el mapa
    #  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
    #  resolution='c')
    
    m=Basemap(projection='mill',lat_ts=20,llcrnrlon=240, \
      urcrnrlon=350,llcrnrlat=-25,urcrnrlat=60, \
      resolution='c')  
    
    
    x, y = m(lon,lat)
    
    cs = m.pcolormesh(x,y,valores,shading='flat',cmap=plt.cm.jet)
    plt.streamplot(x, y, wind_u, wind_v, color='k', density=[5, 5])
    m.drawcoastlines(color = 'w', linewidth=2.0)
    
    #m.fillcontinents()
    m.drawmapboundary()
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
    
    
    plt.colorbar(cs,orientation='vertical')
    
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    plt.title('Agua Precipitable 750 mb '+str(uu)[0:10])
#    plt.barbs(x, y, wind_u, wind_v)
    #plt.barbs(x[list(np.arange(0,181,1))][list(np.arange(0,181,1))], y[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_u[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_v[list(np.arange(0,181,1))][list(np.arange(0,181,1))])
    #plt.barbs(x[list(np.arange(0,181,2))][list(np.arange(0,181,2))], y[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_u[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_v[list(np.arange(0,181,2))][list(np.arange(0,181,2))])
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    
    
    
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_grib_jet_lines_750/' + str(uu)+'.png', figsize=(20,10) ,dpi = 199)
    plt.close()


##### A 500 mb  #############################################################

## A NIVEL DEL 500 MB

for uu in lista_grib:
    #print('hola')
    plt.figure()
    file_1 = pygrib.open(uu)
    variable = file_1.select(name='2 metre temperature')[0]
    #variable = file_1.select(name='Cloud water')[0]
    wind_u = file_1.select(name='U component of wind', level=(500))[0].values
    wind_v = file_1.select(name='V component of wind', level=(500))[0].values    
    p = file_1.select(name='Cloud water')[0]
    
    valores = variable.values 
    lat,lon = variable.latlons()
    
    
    #m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \ # Usado para realizar los plots de todo el mapa
    #  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
    #  resolution='c')
    
    m=Basemap(projection='mill',lat_ts=20,llcrnrlon=240, \
      urcrnrlon=350,llcrnrlat=-25,urcrnrlat=60, \
      resolution='c')  
    
    
    x, y = m(lon,lat)
    
    cs = m.pcolormesh(x,y,valores,shading='flat',cmap=plt.cm.jet)
    plt.streamplot(x, y, wind_u, wind_v, color='k', density=[5, 5])
    m.drawcoastlines(color = 'w', linewidth=2.0)
    
    #m.fillcontinents()
    m.drawmapboundary()
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
    
    
    plt.colorbar(cs,orientation='vertical')
    
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    plt.title('Agua Precipitable 500 mb '+str(uu)[0:10])
#    plt.barbs(x, y, wind_u, wind_v)
    #plt.barbs(x[list(np.arange(0,181,1))][list(np.arange(0,181,1))], y[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_u[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_v[list(np.arange(0,181,1))][list(np.arange(0,181,1))])
    #plt.barbs(x[list(np.arange(0,181,2))][list(np.arange(0,181,2))], y[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_u[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_v[list(np.arange(0,181,2))][list(np.arange(0,181,2))])
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    
    
    
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_grib_jet_lines_500/' + str(uu)+'.png', figsize=(20,10) ,dpi = 199)
    plt.close()


##### A 250 mb  #############################################################

## A NIVEL DE 250 MB

for uu in lista_grib:
    #print('hola')
    plt.figure()
    file_1 = pygrib.open(uu)
    variable = file_1.select(name='2 metre temperature')[0]
    #variable = file_1.select(name='Cloud water')[0]
    wind_u = file_1.select(name='U component of wind', level=(250))[0].values
    wind_v = file_1.select(name='V component of wind', level=(250))[0].values    
    p = file_1.select(name='Cloud water')[0]
    
    valores = variable.values 
    lat,lon = variable.latlons()
    
    
    #m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \ # Usado para realizar los plots de todo el mapa
    #  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
    #  resolution='c')
    
    m=Basemap(projection='mill',lat_ts=20,llcrnrlon=240, \
      urcrnrlon=350,llcrnrlat=-25,urcrnrlat=60, \
      resolution='c')  
    
    
    x, y = m(lon,lat)
    
    cs = m.pcolormesh(x,y,valores,shading='flat',cmap=plt.cm.jet)
    plt.streamplot(x, y, wind_u, wind_v, color='k', density=[5, 5])
    m.drawcoastlines(color = 'w', linewidth=2.0)
    
    #m.fillcontinents()
    m.drawmapboundary()
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
    
    
    plt.colorbar(cs,orientation='vertical')
    
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    plt.title('Agua Precipitable 250 mb '+str(uu)[0:10])
#    plt.barbs(x, y, wind_u, wind_v)
    #plt.barbs(x[list(np.arange(0,181,1))][list(np.arange(0,181,1))], y[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_u[list(np.arange(0,181,1))][list(np.arange(0,181,1))], wind_v[list(np.arange(0,181,1))][list(np.arange(0,181,1))])
    #plt.barbs(x[list(np.arange(0,181,2))][list(np.arange(0,181,2))], y[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_u[list(np.arange(0,181,2))][list(np.arange(0,181,2))], wind_v[list(np.arange(0,181,2))][list(np.arange(0,181,2))])
    #plt.barbs(x[list(np.arange(0,18,1))][list(np.arange(0,18,1))],y[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_u[list(np.arange(0,18,1))][list(np.arange(0,18,1))],wind_v[list(np.arange(0,18,1))][list(np.arange(0,18,1))])
    
    
    
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_grib_jet_lines_250/' + str(uu)+'.png', figsize=(20,10) ,dpi = 199)
    plt.close()





































import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U*U + V*V)

fig = plt.figure(figsize=(7, 9))
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 2])

#  Varying density along a streamline
ax0 = fig.add_subplot(gs[0, 0])
plt.streamplot(X, Y, U, V, density=[1, 2])
ax0.set_title('Varying Density')

# Varying color along a streamline
ax1 = fig.add_subplot(gs[0, 1])
strm = ax1.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
fig.colorbar(strm.lines)
ax1.set_title('Varying Color')

#  Varying line width along a streamline
ax2 = fig.add_subplot(gs[1, 0])
lw = 5*speed / speed.max()
plt.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
ax2.set_title('Varying Line Width')

# Controlling the starting points of the streamlines
seed_points = np.array([[-2, -1, 0, 1, 2, -1], [-2, -1,  0, 1, 2, 2]])

ax3 = fig.add_subplot(gs[1, 1])
strm = ax3.streamplot(X, Y, U, V, color=U, linewidth=2,
                     cmap='autumn', start_points=seed_points.T)
fig.colorbar(strm.lines)
ax3.set_title('Controlling Starting Points')

# Displaying the starting points with blue symbols.
ax3.plot(seed_points[0], seed_points[1], 'bo')
ax3.axis((-w, w, -w, w))

# Create a mask
mask = np.zeros(U.shape, dtype=bool)
mask[40:60, 40:60] = True
U[:20, :20] = np.nan
U = np.ma.array(U, mask=mask)

#ax4 = fig.add_subplot(gs[2:, :])
plt.streamplot(X, Y, U, V, color='r')
plt.set_title('Streamplot with Masking')

ax4.imshow(~mask, extent=(-w, w, -w, w), alpha=0.5,
          interpolation='nearest', cmap='gray', aspect='auto')
ax4.set_aspect('equal')

plt.tight_layout()
plt.show()


plt.streamplot















import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(x, x)
U, V = 12 * X, 12 * Y

data = [(-1.5, .5, -6, -6),
        (1, -1, -46, 46),
        (-3, -1, 11, -11),
        (1, 1.5, 80, 80),
        (0.5, 0.25, 25, 15),
        (-1.5, -0.5, -5, 40)]

data = np.array(data, dtype=[('x', np.float32), ('y', np.float32),
                             ('u', np.float32), ('v', np.float32)])

fig1, axs1 = plt.subplots(nrows=2, ncols=2)
# Default parameters, uniform grid
axs1[0, 0].barbs(X, Y, U, V)

# Arbitrary set of vectors, make them longer and change the pivot point
# (point around which they're rotated) to be the middle
axs1[0, 1].barbs(data['x'], data['y'], data['u'], data['v'], length=8, pivot='middle')

# Showing colormapping with uniform grid.  Fill the circle for an empty barb,
# don't round the values, and change some of the size parameters
axs1[1, 0].barbs(X, Y, U, V, np.sqrt(U * U + V * V), fill_empty=True, rounding=False,
                 sizes=dict(emptybarb=0.25, spacing=0.2, height=0.3))

plt.barbs(X, Y, U, V, np.sqrt(U * U + V * V), fill_empty=False, rounding=True,
                 sizes=dict(emptybarb=0.01, spacing=0.2, height=0.9))

# Change colors as well as the increments for parts of the barbs
axs1[1, 1]


plt.barbs(data['x'], data['y'], data['u'], data['v'], flagcolor='r',
                 barbcolor=['b', 'g'], flip_barb=True,
                 barb_increments=dict(half=10, full=80, flag=100))

# Masked arrays are also supported
masked_u = np.ma.masked_array(data['u'])
masked_u[4] = 1000  # Bad value that should not be plotted when masked
masked_u[4] = np.ma.masked

# Identical plot to panel 2 in the first figure, but with the point at
# (0.5, 0.25) missing (masked)
fig2, ax2 = plt.subplots()
ax2.barbs(data['x'], data['y'], masked_u, data['v'], length=8, pivot='middle')

plt.show()




#################Plot de la presión atmosférica


for uu in lista_grib[0:10]:
    
    plt.figure()
    file_1 = pygrib.open(uu)
    #variable = file_1.select(name='Precipitable water')[0]
    variable = file_1.select(name='Mean sea level pressure')[0]
    wind_u = file_1.select(name='10 metre U wind component')[0].values
    wind_v = file_1.select(name='10 metre V wind component')[0].values
    #p = file_1.select(name='Cloud water')[0]
    valores = variable.values
    #valores = variable.values -273.15# para el caso de la temperatura es necesatio restar 273.15
    lat,lon = variable.latlons()
    
#    Usado para realizar los plots de todo el mapa
    m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), 
      urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(),
      resolution='c')
    
#    m=Basemap(projection='mill',lat_ts=10,llcrnrlon=260, \
#      urcrnrlon=350,llcrnrlat=-15,urcrnrlat=40, \
#      resolution='c')
    
    
    x, y = m(lon,lat)
    
    cs = m.pcolormesh(x,y,valores,shading='flat',cmap=plt.cm.jet)
    plt.streamplot(x, y, wind_u, wind_v, color='k', density=[5, 5])
    m.drawcoastlines(color = 'w', linewidth=2.0)
    
    #cs = m.pcolormesh(x,y,valores,shading='flat',cmap=plt.cm.jet)
    
    m.drawcoastlines()
    #m.fillcontinents()
    m.drawmapboundary()
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
    
    
    plt.colorbar(cs,orientation='vertical')
    plt.title('Mean sea lev press '+str(uu)[0:10])
    
    #plt.barbs(x, y, wind_u, wind_v)
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_pres2/' + str(uu)+'.png', figsize=(20,10) ,dpi = 199)
    plt.close()
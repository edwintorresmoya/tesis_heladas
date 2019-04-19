#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:02:35 2018
#Script creado para realizar la carta de superfície lo más parecido posible a la real
@author: edwin
"""


import pandas as pd
import pygrib
import os
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import numpy as np
import os
import pygrib
import matplotlib.pyplot as plt
os.environ['PROJ_LIB'] = '/home/edwin/anaconda3/share/proj'
from mpl_toolkits.basemap import Basemap
from wrf import getvar, interplevel, to_np, latlon_coords, get_cartopy, cartopy_xlim, cartopy_ylim
import shapefile as shp

def reduction(base, valor=5): ##Función creada para hacer una reducción de la cantidad de vectores presentes en las matrices
    aa = base[list(np.arange(0, base.shape[0], 5))]
    bb = aa[:, list(np.arange(0, base.shape[1], 5))]
    return(bb)

os.chdir('/home/edwin/Downloads/wps/descargas_20180713/1_20070131_20070205')
file_1 = pygrib.open("2007013000.grb")
lista_grib = os.listdir()
lista_grib = sorted(lista_grib)

for uu in lista_grib[8:25]:
    
    file_1 = pygrib.open(uu)
    plt.figure(figsize=(20,10))
    variable = file_1.select(name='Mean sea level pressure')[0]
    valores = variable.values/100
    lat,lon = variable.latlons()
    
    
    m=Basemap(projection='mill',lat_ts=10,llcrnrlon=260,
              urcrnrlon=350,llcrnrlat=-15,urcrnrlat=60,
              resolution='c')
    x, y = m(lon,lat)
    
    cs = m.pcolormesh(x,y,(valores),shading='flat',cmap=plt.cm.jet)
    m.drawcoastlines(color = 'w', linewidth=3.5)
    m.drawcoastlines(color = 'k', linewidth=3.0)
    levels = np.arange(900, 1100, 4)
    CS = plt.contour(x, y, (valores), colors='k', levels=levels)
    plt.clabel(CS, inline=1, fontsize=8, inline_spacing = 5)
    m.drawmapboundary()
    m.drawparallels(np.arange(-90.,120.,10.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,10.),labels=[0,0,0,1])
    
    wind_u = file_1.select(name='10 metre U wind component')[0].values
    wind_v = file_1.select(name='10 metre V wind component')[0].values

    m.barbs(reduction(x), reduction(y), reduction(wind_u), reduction(wind_v), rounding=False,
            sizes=dict(emptybarb=0.05, spacing=0.2, height=0.3)) 
    plt.title('Análisis a presión superficial (mbar) para el día '+str(uu)[6:8]+' del mes '+str(uu)[4:6]+' del año '+str(uu)[0:4]+' a las '+str(uu)[8:10]+' UTC')
    #m.streamplot(x, y, wind_u, wind_v, color='blue', density=[5, 5])
    plt.colorbar(cs,orientation='vertical')
    print(uu)
    
    plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/cartas_gfs/' + str(uu)[0:10]+'.png', figsize=(20,10) ,dpi = 199)
    plt.close()
 
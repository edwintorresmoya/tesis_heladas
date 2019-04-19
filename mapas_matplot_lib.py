#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:30:04 2018

@author: edwin
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os

#os.chdir('/home/edwin/Downloads/wps/ubicacion_zona')
#
#fh = Dataset('wrfout_d01_2007-02-04_17:00:00', mode='r')
#
#lats = fh.variables['XLAT_U'][:]
#lons = fh.variables['XLONG_U'][:]
#
#fh.close()
#
#lats.mean()
#lons.mean()
#
#lats.min()
#lats.max()
#
#lons.min()
#lons.max()
#
#a = []
#
#for i in fh.variables:
#    a = 
#
#
#################################



from netCDF4 import Dataset as NetCDFFile 
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

os.chdir('/home/edwin/Downloads/')
nc = Dataset('ECMWF_ERA-40_subset.nc', mode='r')

lat = nc.variables['latitude'][:]
lon = nc.variables['longitude'][:]
time = nc.variables['time'][:]
t2 = nc.variables['p2t'][:] # 2 meter temperature
mslp = nc.variables['msl'][:] # mean sea level pressure
u = nc.variables['p10u'][:] # 10m u-component of winds
v = nc.variables['p10v'][:] # 10m v-component of winds


map = Basemap(projection='merc',llcrnrlon=-93.,llcrnrlat=35.,urcrnrlon=-73.,urcrnrlat=45.,resolution='i') # projection, lat/lon extents and resolution of polygons to draw
# resolutions: c - crude, l - low, i - intermediate, h - high, f - full


map.drawcoastlines()
map.drawstates()
map.drawcountries()
map.drawlsmask(land_color='Linen', ocean_color='#CCFFFF') # can use HTML names or codes for colors
map.drawcounties() # you can even add counties (and other shapefiles!)


parallels = np.arange(30,50,5.) # make latitude lines ever 5 degrees from 30N-50N
meridians = np.arange(-95,-70,5.) # make longitude lines every 5 degrees from 95W to 70W
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

lons,lats= np.meshgrid(lon-180,lat) # for this dataset, longitude is 0 through 360, so you need to subtract 180 to properly display on map
x,y = map(lons,lats)


clevs = np.arange(960,1040,4)
cs = map.contour(x,y,mslp[0,:,:]/100.,clevs,colors='blue',linewidths=1.)



plt.clabel(cs, fontsize=9, inline=1) # contour labels
plt.title('Mean Sea Level Pressure')

temp = map.contourf(x,y,t2[4,:,:])
cb = map.colorbar(temp,"bottom", size="5%", pad="2%")
plt.title('2m Temperature')
cb.set_label('Temperature (K)')
plt.show()


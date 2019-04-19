#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:01:49 2018

@author: edwin
"""



def variables_nc(data):
    for ii in data.variables:
        print(ii, data.variables[ii].shape)

#map_1 = Basemap(projection='merc',llcrnrlon=-82.,llcrnrlat=-5.,urcrnrlon=-65.7,urcrnrlat=13.21,resolution='i') # Colombia en Mercator


import os
os.environ['PROJ_LIB'] = '/home/edwin/anaconda3/share/proj'
import numpy as np

from netCDF4 import Dataset
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import cartopy.crs as crs
from cartopy.feature import NaturalEarthFeature

from wrf import to_np, getvar, smooth2d, get_cartopy, cartopy_xlim, cartopy_ylim, latlon_coords

# Open the NetCDF file
ncfile = Dataset("/home/edwin/wrf_b/wrf/carpeta_alturas/wrf.nc")
#ncfile = Dataset("/home/edwin/Downloads/ecwf/salida.nc")
variables_nc(ncfile)
#HGT_M Altira del modelo


ncfile.va

slp_1 = getvar(ncfile, "z")#Forma de obtener la variable de altura
slp = slp_1[0,:,:]

slp[0,0]
slp[0,1]

base_e = pd.DataFrame({'abc':range(0,5)})



phb = ncfile.variables['PHB'][0,1]
phb_1 = ncfile.variables['PHB'][0,0]
ph = ncfile.variables['PH'][0,0]
ph_1 = ncfile.variables['PH'][0,1]
al_1 = (phb + ph)/9.81
al_2 = (0.5*(phb + ph+phb_1 + ph_1))/9.81

phb = f.variables['PHB'][0,1]
phb_1 = f.variables['PHB'][0,0]
ph = f.variables['PH'][0,0]
ph_1 = f.variables['PH'][0,1]

al_2 = (0.5*(phb + ph+phb_1 + ph_1))/9.81
al_2[0,0]


al_1[0,0]
al_2[0,0]

phb33 =getvar(ncfile, "PHB")
ph_2 =getvar(ncfile, "PH")

phb33[0,0,0]
phb33[0,1,0]


#temperatura

tmp_1 =getvar(ncfile, "T2")
tmp_1[1,1] - 273.15

tmp_1 =getvar(ncfile, "T")
tmp_1[1,1]

ncfile.variables['T2'][0, 0, 0] - 273.15

#### Viento
vien_1 =getvar(ncfile, "U10")
vien_1[0,1]
vien_1.shape
vien_1
vien_1.min()

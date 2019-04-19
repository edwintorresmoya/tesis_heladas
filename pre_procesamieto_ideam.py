#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:50:59 2018
Archivo creado para darle formato a los archivos tr5 del IDEAM
@author: edwin
"""

import numpy as np
import pandas as pd
import os

#Función

def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)

#Selección del directorio


#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
os.chdir('/home/edwin/Downloads/107512')

#ideam_1 = pd.read_csv('20179050085752.tr5', header=None)
ideam_1 = pd.read_csv('107512.tr5', header=None)

ideam_1.columns = ['a']
###Partición por numero de caracteres
ideam_1['tr'] = ideam_1.a.str[0:1]
ideam_1['cod'] = ideam_1.a.str[1:9]
ideam_1['t_info'] = ideam_1.a.str[9:11]
ideam_1['year'] = ideam_1.a.str[11:15]
ideam_1['day'] = ideam_1.a.str[15:17]
ideam_1['01'] = ideam_1.a.str[17:22]
ideam_1['01-1'] = ideam_1.a.str[22:23]
ideam_1['02'] = ideam_1.a.str[23:28]
ideam_1['02-1'] = ideam_1.a.str[28:29]
ideam_1['03'] = ideam_1.a.str[29:34]
ideam_1['03-1'] = ideam_1.a.str[34:35]
ideam_1['04'] = ideam_1.a.str[35:40]
ideam_1['04-1'] = ideam_1.a.str[40:41]
ideam_1['05'] = ideam_1.a.str[41:46]
ideam_1['05-1'] = ideam_1.a.str[46:47]
ideam_1['06'] = ideam_1.a.str[47:52]
ideam_1['06-1'] = ideam_1.a.str[52:53]
ideam_1['07'] = ideam_1.a.str[53:58]
ideam_1['07-1'] = ideam_1.a.str[58:59]
ideam_1['08'] = ideam_1.a.str[59:64]
ideam_1['08-1'] = ideam_1.a.str[64:65]
ideam_1['09'] = ideam_1.a.str[65:70]
ideam_1['09-1'] = ideam_1.a.str[70:71]
ideam_1['10'] = ideam_1.a.str[71:76]
ideam_1['10-1'] = ideam_1.a.str[76:77]
ideam_1['11'] = ideam_1.a.str[77:82]
ideam_1['11-1'] = ideam_1.a.str[82:83]
ideam_1['12'] = ideam_1.a.str[83:88]
ideam_1['12-1'] = ideam_1.a.str[88:89]
ideam_1['tipo'] = ideam_1.a.str[99:100]
##Union de las bases con la georreferenciación
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
cat_ideam = pd.read_csv('CATALOGO_ESTACIONES_IDEAM_V10_AGOSTO2017.csv')

ideam_1 = ideam_1.convert_objects(convert_numeric=True)
cat_ideam = cat_ideam.convert_objects(convert_numeric=True)

union_1 = pd.merge(left=ideam_1, right=cat_ideam, on='cod')

union_1 = union_1.iloc[:,1:]

union_1 = union_1.convert_objects(convert_numeric=True)

union_2 = union_1.replace(to_replace=99999, value=np.NaN)
union_2 = union_2.replace(to_replace=9999, value=np.NaN)

#union_2.to_csv('union_2-20180130.csv')
#union_2.to_pickle('union_2-20180130.pickle')

union_2 = pd.read_pickle('union_2-20180130.pickle')

## Ahora vamos a ponerlos en orden

union_3 = union_2.iloc[:,[1,29,44,49,2,3,4,5,7,9,11,13,15,17,19,21,23,25,27]]

union_4 = union_3.melt(id_vars=list(union_3.iloc[:,:7]))

union_4.rename(columns={'variable':'month'}, inplace=True)
#union_4.columns.values[1] = "nuevo_n"
union_5 = pd.pivot_table(union_4, index=list(union_4.iloc[:,[0,1,2,3,5,6,7]]), values='value', columns='t_info')

#union_5.to_pickle('union_5.pickle')
#union_5.to_csv('union_5.csv')

union_5 = pd.read_pickle('union_5.pickle')
union_5 = pd.read_csv('union_5.csv')
union_5['date1'] = (union_5.year*10000) + (union_5.month*100)+ (union_5.day)
union_5['date'] = pd.to_datetime(union_5.date1, format='%Y%m%d', errors='coerce')

union_6 = union_5.iloc[:,[0,1,2,3,19,7,8,9,10,11,12,13,14,15,16,17]]

union_6.to_pickle('union_6.pickle')

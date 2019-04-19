#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:31:13 2018

@author: edwin
"""

import pandas as pd
import numpy as np
import os
from statistics import mean
import matplotlib.pyplot as plt
import plotly.plotly as py

###############
def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)
#################

########
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],
                   columns=['one', 'two', 'three'])

df.iloc[]
########

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam'

os.chdir(path) # Cambia de directorio
os.getcwd() # Determina donde estoy

os.listdir() # lista de los archivos dentro de la carpeta

ideam_rs_3 = pd.read_pickle('union_6.pickle')


ideam_rs_3.shape # Dimensiones (4942764, 17)
ideam_rs_3.dtypes # colmns data type



## Extraer a Mosquera

tiba = ideam_rs_3[(ideam_rs_3.cod == 21205970)]

# =============================================================================
# Nemocón = 21205970
# Sopó = 21205990
# Tibaitatá = 21205420
# 
# =============================================================================

#tiba.to_pickle('tibaitata.pickle')
#tiba.to_csv('tibaitata.csv')
#tiba = pd.read_pickle('tibaitata.pickle')

#tiba.shape

#==============================================================================
# Según el IDEAM:
#     
#     1 Valores medios
#     2 Máximos absolutos
#     3 Mínimos absolutos
#     4 Totales
#     5 Número de dia con lluvia
#     7 Máximos medios
#     8 Mínmos medios
#     9 Máxima en 24 horas
#==============================================================================

#tiba.TS.describe() # descripción 

#tiba[(tiba.TS == -5.1)] # Este valor se encontró como tipo 8 osea que el valor tipo 8 serán los valores mínimos

#tiba[(tiba.TS == 26)] # Tipo 2
###
tiba.tipo.unique() # list of unique values
###

tiba_min = tiba[(tiba.tipo == 8)] # Valores mínimos

tiba_max = tiba[(tiba.tipo == 2)] # Valores máximos
#tiba_max = tiba[(tiba.tipo == 4)] # Valores máximos

tiba_mean = tiba[(tiba.tipo == 1)] # Valores promedio


# HIstograma para la descripción de las funciones

#gaus = np.random.randn(1000)
#plt.hist(gaus)
#gaus.dtype
tiba.TS.dtype
tiba.TS.plot.hist(bins = 20, color = 'k')
tiba_max.TS.plot.hist(bins = 20, color = 'k')
tiba_min.TS.plot.hist(bins = 20, color = 'k')

tiba_cero = tiba_min[(tiba_min.TS < 0)]
#tiba_cero.to_csv('tiba_cero.csv')


tiba_veinte = tiba_max[(tiba_max.TS > 20)]
tiba_veinte.to_csv('tiba_veinte.csv')
tiba_cero.TS.plot.hist()
tiba_veinte.TS.plot.hist()
tiba_cero.shape
tiba_cero.TS.plot()
tiba_cero.date.dt.month.plot.hist(bins=12)
tiba_cero.date.dt.year.plot.hist(bins=20)
plt.plot(tiba_cero['date'], tiba_cero['TS'])
plt.plot(tiba_veinte['date'], tiba_veinte['TS'])
tiba_veinte.date.dt.month.plot.hist(bins=12)
tiba_veinte.date.dt.year.plot.hist(bins=20)

### Importar los valores de la temperatura del pacífico

os.getcwd()
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Exploración')

sst_1 = pd.read_csv('sst_pacifico.txt')

sst_1['a'] = 0

ideam_crudo['cod'] = ideam_crudo.DATOS.str[1:9]

sst_1.columns = ['a', 'b']

sst_1['year'] = sst_1.a.str[0:4]
sst_1['month'] = sst_1.a.str[6:8]
sst_1['nino12'] = sst_1.a.str[10:16]
sst_1['anom12'] = sst_1.a.str[18:26]
sst_1['nino3'] = sst_1.a.str[27:34]
sst_1['anom3'] = sst_1.a.str[35:42]
sst_1['nino4'] = sst_1.a.str[43:49]
sst_1['anom4'] = sst_1.a.str[50:55]
sst_1['nino34'] = sst_1.a.str[56:64]
sst_1['anom34'] = sst_1.a.str[65:]


sst_2 = sst_1.iloc[0:,2:]
os.get_blocking
#From objects to float64
sst_2 = sst_2.convert_objects(convert_numeric=True)

#sst_2.to_csv('sst_82_17.csv')

sst_2.nino3.iloc[:5]
sst_2.nino3.iloc[0:6].sum()


#### Unir las máximas, mínimas y medias en una sola base.

tiba_min = tiba[(tiba.tipo == 8)] # Valores mínimos
tmin = tiba_min.rename(columns={ 'TS' : 'TS_min'})
tmin = tmin.iloc[:,[4,2,3,0,13]]#Selección de solo las variables de interés en este caso la temperatura
tmin = tmin[tmin.TS_min.notnull()]

tiba_max = tiba[(tiba.tipo == 2)] # Valores máximos
tmax = tiba_max.rename(columns={ 'TS' : 'TS_max'})
tmax = tmax.iloc[:,[4,2,3,0,13]]
tmax = tmax[tmax.TS_max.notnull()]

tiba_mean = tiba[(tiba.tipo == 1)] # Valores promedio
tmean = tiba_mean.rename(columns={ 'TS' : 'TS_mean'})
tmean = tmean.iloc[:,[4,2,3,0,13]]
tmean = tmean[tmean.TS_mean.notnull()]

#Pegar las columnas

#pd.merge(df1, df3, on = 'Year', how = 'outer')
u1 = pd.merge(left=tmin, right=tmax, how='outer', on=['date', 'LATITUD', 'LONGITUD', 'cod'])
u2 = pd.merge(left=tmean, right=u1, how='outer', on=['date', 'LATITUD', 'LONGITUD', 'cod'])

u2.to_csv('union_2.csv')

### Voy a sacar los promedios mensuales de las 3 columnas para poder hacer las correlaciones con la sst

#from datetime import datetime

u2['year'] = u2.date.dt.year
u2['month'] = u2.date.dt.month
lista_nombres(tmin)
resum = u2.groupby(['cod','LATITUD','LONGITUD','year', 'month'])['TS_mean','TS_max', 'TS_min'].mean()

resum.to_csv('t_resumen_tiba.csv')
resum = pd.read_csv('t_resumen_tiba.csv')

sst_2 = pd.read_csv('sst_82_17.csv')

sst_2 = sst_2.convert_objects(convert_numeric=True, )
resum = resum.convert_objects(convert_numeric=True)

lista_comparar = pd.merge(left=sst_2, right=resum, how='inner', on=['year', 'month'])

r2 = lista_comparar.iloc[:,[2,3,4,5,6,7,8,9,13,14,15]]
r2_2 = r2.corr()

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam'
os.chdir(path) # Cambia de directorio
os.getcwd() # Determina donde estoy
r2_2.to_csv('r2-2.csv')

#scatter plot 

# sample data
x = np.arange(10)
y = 5*x + 10 

# fit with np.polyfit
m, b = np.polyfit(x, y, 1)

plt.plot(x, y, '.')
plt.plot(x, m*x + b, '-')

x=r2.TS_mean
y=r2.nino12
m, b = np.polyfit(x, y, 1)
l = np.arange(12,16)
plt.plot(x, y, '.')
plt.plot(l, m*l + b, '-')

x=r2.TS_mean
y=r2.nino3
m, b = np.polyfit(x, y, 1)
l = np.arange(12,16)
plt.plot(x, y, '.')
plt.plot(l, m*l + b, '-')

x=r2.TS_mean
y=r2.nino4
m, b = np.polyfit(x, y, 1)
l = np.arange(12,16)
plt.plot(x, y, '.')
plt.plot(l, m*l + b, '-')

x=r2.TS_mean
y=r2.nino34
m, b = np.polyfit(x, y, 1)
l = np.arange(12,16)
plt.plot(x, y, '.')
plt.plot(l, m*l + b, '-')

#pd.DataFrame(np.corrcoef(lista_comparar.iloc[:,[3,4]]))


#####Busqueda de las fechas de interés en mínimas y máximas

tiba_cero['month'] = tiba_cero.date.dt.month
aa = tiba_cero.sort_values(['TS']).iloc[:20,:]#Fecha de la helada común en Febrero muy fuerte
a1 = tiba_cero[tiba_cero.month == 8].sort_values(['TS']).iloc[:20,:]

tiba_cero[tiba_cero.month.isin([1,2])] # conjunto de datos
tiba_cero[~tiba_cero.month.isin([1,2,12])].sort_values(['TS']).iloc[:20,:]

tiba_max['month'] = tiba_max.date.dt.month
tiba_max.sort_values(['TS'], ascending=False).iloc[:20,:] # Fecha para la selección del valor con más temperatura
tiba_max[~tiba_max.month.isin([1,2,12])].sort_values(['TS'], ascending=False).iloc[:20,:]


bb = tiba_max.sort_values(['TS'], ascending=False).iloc[:20,:]


###########Cuales estaciones presentan valores superiores a 20°C

estaciones = ideam_rs_3[ideam_rs_3.TS > 20]
estaciones_1 = estaciones.groupby(['LATITUD','LONGITUD'])['cod'].mean()

estaciones_1.to_csv('estac_sup_20.csv')

est_sup20 = [35025050,21206640,21205720,21206650,21206660,21206610,21206970,21205840,21205580,21206170,21206510,21206240,21205230,21206620,21206220,21206280,21206560,21206230,21206190,21205710,21206700,21205420,21206550,21205520,21206150,21205790,21205770,21206200,21205750,21206680,21206210,21205870,21206630,21206500,21205950,21206600,21206050,21206670,21205980,21205013,21206260,21206690,21205920,21205940,21205700,21206030,21205960,21206450,21205910,21205740]

sup20 = ideam_rs_3[ideam_rs_3.cod.isin(est_sup20)]

sup20.groupby(['cod','LATITUD','LONGITUD'])['TS'].max()

#Máxima temperatura
aa = ideam_rs_3[ideam_rs_3.cod == 21206690]
aa[aa.TS == 33]


#############################
############################# Nuevas adiciones
#############################

###

est_zon = [21206190,21206200,21206210,21206220,21206230,21206240,21206250,21206260,21206280,21206450,21206490,21206500,21206510,21206540,21206550,21206560,21206570,21206610,21206620,21206630,21206640,21206650,21206660,21206670,21206680,21206690,21206700,21206970,21200160,21200620,21201050,21201080,21201140,21201160,21201210,21201230,21201240,21201250,21201270,21201550,21201570,21201600,21201610,21201620,21201630,21201650,21202100,21202280,21205013,21205230,21205420,21205520,21205580,21205600,21205700,21205710,21205720,21205730,21205740,21205750,21205760,21205770,21205780,35020320,21205790,35020330,21205800,21205810,35025050,21205820,35025060,21205830,21205840,21205850,21205860,21205870,21205880,21205890,21205900,21205910,21205920,21205930,35027220,21205940,21205950,21205960,21205970,21205980,21205990,21206000,21206010,21206020,21206030,21206040,21206050,21206060,21206150,21206170,21205528,21205529,21206130]

est_zonas = ideam_rs_3[ideam_rs_3.cod.isin(est_zon)]
#est_zonas.to_csv('est_zonas.csv')
#est_zonas = pd.read_csv('est_zonas.csv')

marc = pd.DataFrame({'lista':(np.arange(1,len(est_zon)+1)), 
                      'cod':est_zon})

###Voy a colocar un número de 1: para poder dibujar las líneas en el tiempo

df = pd.DataFrame({'a':np.arange(0,10), 'b':np.random.uniform(0,1,10)})
df2 = pd.DataFrame({'a':[1,3,4], 'b':['a','b','c']})

nonants = 

est_zonas_2 = pd.merge(left=est_zonas[est_zonas.TS.notnull()], right=marc, how = 'inner', on='cod')

import matplotlib
matplotlib.style.use('ggplot')
import matplotlib.pyplot as plt

est_zonas_3 = est_zonas_2.iloc[:,[0,4,16]] 
est_zonas_3.columns.values[3] = 'lista_2'

plt.figure()
est_zonas_3.groupby(['date', 'lista']).sum().unstack().plot()


union_5 = pd.pivot_table(union_4, index=list(uu.iloc[:,[0,1,2,3,5,6,7]]), values='value', columns='t_info')
pd.pivot()




import pandas as pd
import matplotlib.pyplot as plt

grupos = est_zonas_3.groupby('cod')

fig, ax = plt.subplots()

for name, group in grupos:
    ax.plot(group['date'], group['lista'], label=name)
#ax.legend(loc='best')
fig.legend().set_visible(False)
fig.set_size_inches(21.69,16.27)
fig.legend(loc='upper left')
#ig.set_size_inches(5,2)
fig.savefig('gra1.png')

plt.show()

est_zonas.date.dt.year.hist() # Gráfica de la distribución de los datos a través de los años
me_1 = est_zonas[est_zonas.TS.notnull()]
me_1[me_1.tipo ==1].date.dt.year.hist()


#### Missin data



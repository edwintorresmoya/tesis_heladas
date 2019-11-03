#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 13:32:11 2018

@author: edwin
"""

# Validación de los datos de la estación con los datos manuales de CORPOICA

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import style
import pdb

def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    return(base2)

# Importación de datos
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/hydras3_2005')
lista_estaciones_2 = pd.DataFrame(list(os.listdir()))

base = pd.read_csv('21206990.csv')

#Creación de una sola columna de datos de temperatura
a = base[-base.tmp_2m.isnull()][['date','tmp_2m']]
a.columns = ['date','tmp_2m']
b = base[base.tmp_2m.isnull()& -base.tmp_2m_min.isnull()][['date','tmp_2m_min']]
b.columns = ['date', 'tmp_2m']
c = base[base.tmp_2m.isnull()& base.tmp_2m_min.isnull() & -base.tmp_2m_max.isnull()][['date','tmp_2m_max']]
c.columns = ['date','tmp_2m']

n_tmp = pd.concat([a,b,c])

base_2 = pd.merge(left=base, right=n_tmp, on='date', how='outer')

#Validación de los datos por límites extremos
base_3 = base_2[base_2.tmp_2m_y.notnull()]
base_3 = base_3[(base_3.tmp_2m_y < 50) & (base_3.tmp_2m_y > -30)].reset_index(drop=True)

###Cargar las bases del CORPOICA
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_corpoica')
corpo = pd.read_csv('union_t.csv')

corpo.dia = corpo.dia.astype(int)

corpo2 = corpo.convert_objects(convert_numeric=True)
corpo3 = corpo2.iloc[:,[0,1,2,3,4,6,7,8,9,10,11,12,14,15,16,18,20,21,22,24,26,27,28,30,34,36,38,40,41,42]]
lista_nombres(corpo3)
corpo3.head()

corpo3['date'] = corpo3.Año * 10000 + corpo3.Mes * 100 + corpo3.dia

corpo3.date = pd.to_datetime(corpo3.date, format ='%Y%m%d', errors='coerce')

corpo4 = corpo3[-corpo3.date.isnull()]

corpo4 = corpo4.sort_values(['date'])

lista_nombres(corpo4)


#Los datos máximos y mínimos de cada día no pueden sobrepasar los valores a las horas

#corpo4 = Base de Corpoica y base_3 = base de HYDRAS

inicio = '20120129'
final = '20120208'

##cambio a datetime de las fechas

base_3.date = pd.to_datetime(base_3.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

min_rang_1 = base_3[base_3.date == max(base_3[((base_3.date <= pd.to_datetime(inicio + ' 0:0:0',
                                            format ='%Y%m%d %H:%M:%S', errors='coerce')))].date)].index[0]

max_rang_1 = base_3[base_3.date == min(base_3[((base_3.date >= pd.to_datetime(final + ' 0:0:0',
                                            format ='%Y%m%d %H:%M:%S', errors='coerce')))].date)].index[0]


lista_nombres(corpo4)
lista_nombres(base_3)
#Gráfica de solo convencional

min_min = corpo4.index.get_loc(corpo4[corpo4.date == max(corpo4[corpo4.date <= pd.to_datetime(inicio + ' 0:0:0',format ='%Y%m%d %H:%M:%S', errors='coerce')].date)].index[0])
max_min = corpo4.index.get_loc(corpo4[corpo4.date == min(corpo4[corpo4.date >= pd.to_datetime(final + ' 0:0:0',format ='%Y%m%d %H:%M:%S', errors='coerce')].date)].index[0])

fig = plt.figure(1)
fig.set_size_inches(20,10)

style.use('default')

plt.plot_date(x=base_3.iloc[min_rang_1:max_rang_1,:].date, y=base_3.iloc[min_rang_1:max_rang_1,:].tmp_2m_y, linestyle='-', label = 'HYDRAS_2m')
plt.plot_date(x=base_3.iloc[min_rang_1:max_rang_1,:].date, y=base_3.iloc[min_rang_1:max_rang_1,:].tmp_10cm, linestyle='-', marker='v',label = 'HYDRAS_10cm')
#plt.plot_date(x=base_3.iloc[min_rang_1:max_rang_1,:].date, y=base_3.iloc[min_rang_1:max_rang_1,20], linestyle='--', marker='v',label = 'HYDRAS_10cm_min')
#plt.plot_date(x=base_3.iloc[min_rang_1:max_rang_1,:].date, y=base_3.iloc[min_rang_1:max_rang_1,:].tmp_10cm, linestyle='--', marker='v',label = 'HYDRAS_10cm')
plt.plot_date(x=corpo4.iloc[min_min:max_min,:].date, y=corpo4.iloc[min_min:max_min,:].max_2m, linestyle='--', marker ='o', label = 'Máxima-conv')
plt.plot_date(x=corpo4.iloc[min_min:max_min,:].date, y=corpo4.iloc[min_min:max_min,:].min_2m, linestyle='--', marker ='o', label = 'Mínima-conv')
plt.plot_date(x=corpo4.iloc[min_min:max_min,:].date, y=corpo4.iloc[min_min:max_min,:].min_1m, linestyle='--', marker ='>', label = 'Mínima-1m')
plt.plot_date(x=corpo4.iloc[min_min:max_min,:].date, y=corpo4.iloc[min_min:max_min,:].min_50cm, linestyle='--', marker ='*', label = 'Mínima-50cm')
plt.plot_date(x=corpo4.iloc[min_min:max_min,:].date, y=corpo4.iloc[min_min:max_min,:].min_10cm, linestyle='--', marker ='v', label = 'Mínima-10cm')
plt.plot_date(x=corpo4.iloc[min_min:max_min,:].date, y=corpo4.iloc[min_min:max_min,:].min_5cm, linestyle='--', marker ='^', label = 'Mínima-5cm')


plt.ylabel('Temperatura °C')
plt.xlabel('Fecha')
plt.xticks(rotation='vertical')
plt.legend()
plt.grid(True,color='lightgray')

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph'
    
os.chdir(path)
#plt.savefig('comparacion_tmp_del_suelo_2007.png', figsize=(20,10) ,dpi = 199)
#plt.savefig('comparacion_tmp_del_suelo_2012.png', figsize=(20,10) ,dpi = 199)
#plt.savefig('comparacion_tmp_del_suelo_2017.png', figsize=(20,10) ,dpi = 199)

#USar esta
#plt.savefig('comparacion_tmp_del_suelo_2007.png', figsize=(20,10) ,dpi = 199)

plt.close()

###############
#Extracción de los valores mínimos

corpo4.min_5cm.mean()
corpo4.min_10cm.mean()
corpo4.min_50cm.mean()
corpo4.min_1m.mean()
corpo4.min_2m.mean()

corpo4.min_5cm.median()
corpo4.min_10cm.median()
corpo4.min_50cm.median()
corpo4.min_1m.median()
corpo4.min_2m.median()


pdb.set_trace()

corpo4 = corpo4[corpo4['min_2m.1'] < 80]

corpo4.columns.values[24] = '5 cm'
corpo4.columns.values[25] = '10 cm'
corpo4.columns.values[26] = '50 cm'
corpo4.columns.values[27] = '100 cm'
corpo4.columns.values[29] = '200 cm'


#corpo4[['min_5cm','min_10cm','min_50cm','min_1m', 'min_2m.1']].boxplot()
corpo4[['min_2m.1','min_1m','min_50cm','min_10cm','min_5cm']].boxplot()
plt.xlabel('Altura')
plt.ylabel('Temperatura °C')
plt.title('')
plt.suptitle('')
plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Tesis_Edwin_20190226/graph/boxplot_t_min_conv.png')


pdb.set_trace()
print('hola')

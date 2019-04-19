#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:17:10 2018

@author: edwin
"""

#Manejo de la bases del Ministerio de Agricultura
#https://www.datos.gov.co/Agricultura-y-Desarrollo-Rural/Cadena-Productiva-Papa-Area-Producci-n-Y-Rendimien/pnsj-t3kh

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspect


# Función lista nombres
def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)

#Selección del directorio
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/datos')

base_c = pd.read_csv('Cadena_Productiva_Papa_-_Area__Producci_n_Y_Rendimiento.csv')

base_c['DESAGREGACIÓN REGIONAL Y/O SISTEMA PRODUCTIVO'].unique()



base_c['year'] = base_c.PERIODO.str[0:4]
base_c['month_1'] = base_c.PERIODO.str[4:5]
base_c['month_2'] = np.where(base_c.month_1 == 'A', 1, 6)
base_c = base_c.convert_objects(convert_numeric=True)
base_c['date_1'] = (base_c.year * 100) + (base_c.month_2)
base_c['PERIODO'] = pd.to_datetime(base_c.date_1, format='%Y%m', errors='coerce')


#Solo base de papa
base_p = base_c[base_c['DESAGREGACIÓN REGIONAL Y/O SISTEMA PRODUCTIVO'] == 'PAPA']

base_p['DESAGREGACIÓN REGIONAL Y/O SISTEMA PRODUCTIVO'].unique()

resum_dpto = base_p.groupby(['DEPARTAMENTO', 'PERIODO'])['Área Sembrada(ha)','Área Cosechada(ha)','Producción(t)'].sum()
resum_dpto.to_csv('resum_dpto.csv')
resum_dpto = pd.read_csv('resum_dpto.csv')

mean_dpto = base_p.groupby(['DEPARTAMENTO', 'PERIODO'])['Rendimiento(t/ha)'].mean()
mean_dpto.to_csv('mean_dpto.csv', header=True)
mean_dpto = pd.read_csv('mean_dpto.csv')

resum_mens = pd.merge(left=resum_dpto, right=mean_dpto, on=['DEPARTAMENTO', 'PERIODO'], how='outer')


## Voy a crear un archivo para mirar los cambios en los precios 

res2017 = resum_mens[resum_mens.PERIODO.isin(['2017-01-01', '2017-06-01'])]

res2017.PERIODO = pd.to_datetime(res2017.PERIODO, format ='%Y-%m-%d', errors='coerce')

res2017 = res2017.sort_values(by='Área Cosechada(ha)', ascending=False)

res2017[r"\\"] = r"\\"

aa = round(res2017, 2)

#aa.to_csv('resum2017.csv', sep='&', index=False)

res_cun = resum_mens[resum_mens.DEPARTAMENTO == 'CUNDINAMARCA']

res_cun.PERIODO = pd.to_datetime(res_cun.PERIODO, format ='%Y-%m-%d', errors='coerce')

##Gráficas

fig = plt.figure(1)
fig.set_size_inches(25,7.5)
fig.suptitle('Estadísticas de la papa en Cundinamarca')
            
            
gridspect.GridSpec(1,3)

plt.subplot2grid((1,3), (0,0), rowspan=1, colspan=1)
plt.plot_date(x=res_cun.PERIODO, y=res_cun['Área Sembrada(ha)'], linestyle='-', label ='Área Sembrada(ha)')
plt.plot_date(x=res_cun.PERIODO, y=res_cun['Área Cosechada(ha)'], linestyle='-', label ='Área Cosechada(ha)')
plt.xticks(rotation = 90)
plt.legend()

plt.subplot2grid((1,3), (0,1), rowspan=1, colspan=1)
plt.plot_date(x=res_cun.PERIODO, y=res_cun['Producción(t)'], linestyle='-')
plt.xticks(rotation = 90)
plt.legend()

plt.subplot2grid((1,3), (0,2), rowspan=1, colspan=1)
plt.plot_date(x=res_cun.PERIODO, y=res_cun['Rendimiento(t/ha)'], linestyle='-')
plt.xticks(rotation = 90)
plt.legend()

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph'

os.chdir(path)
plt.savefig('papa_cund_png', figsize=(20,10) ,dpi = 199)
plt.close()

##Crear cada una de las imagenes
########1
plt.figure(figsize=(7.5,3.75))
plt.plot_date(x=res_cun.PERIODO, y=res_cun['Área Sembrada(ha)'], linestyle='-', label ='Área Sembrada')
plt.plot_date(x=res_cun.PERIODO, y=res_cun['Área Cosechada(ha)'], linestyle='-', label ='Área Cosechada')
plt.xticks(rotation = 90)
plt.xlabel('años')
plt.ylabel('Hectáreas')
plt.legend()

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph'
os.chdir(path)
plt.savefig('papa_cund_png_1', figsize=(20,10) ,dpi = 199)
plt.close()


########2
plt.figure(figsize=(7.5,3.75))
plt.plot_date(x=res_cun.PERIODO, y=res_cun['Producción(t)'], linestyle='-')
plt.xticks(rotation = 90)
plt.xlabel('años')
plt.ylabel('Toneladas (t)')
plt.legend()

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph'
os.chdir(path)
plt.savefig('papa_cund_png_2', figsize=(20,10) ,dpi = 199)
plt.close()


########3
plt.figure(figsize=(7.5,3.75))
plt.plot_date(x=res_cun.PERIODO, y=res_cun['Rendimiento(t/ha)'], linestyle='-')
plt.xticks(rotation = 90)
plt.xlabel('años')
plt.ylabel('Toneladas/hectárea')
plt.legend()

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph'
os.chdir(path)
plt.savefig('papa_cund_png_3', figsize=(20,10) ,dpi = 199)
plt.close()


## Sacar la tabla de los rendimientos municipales
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/datos')

mean_cund_mun = base_p[base_p.DEPARTAMENTO == 'CUNDINAMARCA']
mean_cund_mun_ren = mean_cund_mun.groupby(['MUNICIPIO', 'PERIODO'])['Área Sembrada(ha)'].mean()
mean_cund_mun_ren.to_csv('mean_cund_mun_ren.csv', header=True)
mean_cund_mun_ren = pd.read_csv('mean_cund_mun_ren.csv')

tab_pivot = pd.pivot_table(mean_cund_mun_ren, values='Área Sembrada(ha)', index='PERIODO', columns='MUNICIPIO')
tab_pivot[r"\\"] = r"\\"

tab_pivot.to_csv('tab_pivot.csv', sep='&', index=False)
tab_pivot.to_csv('tab_pivot.csv', index=True)


mean_dpto = base_p.groupby(['DEPARTAMENTO', 'PERIODO'])['Rendimiento(t/ha)'].mean()
mean_dpto.to_csv('mean_dpto.csv', header=True)
mean_dpto = pd.read_csv('mean_dpto.csv')

#Tabla de precios

precios = pd.read_csv('datos_bgta.csv')
precios['date_1'] = precios.Year * 100 + precios.Mes
precios['date1'] = pd.to_datetime(precios.date_1, format='%Y%m', errors='coerce')




fig, ax1 = plt.subplots()

ax1.plot_date(x=precios.date1, y=precios['Precio (/KG)'], linestyle = '-')

ax2 = ax1.twinx()
ax2.subplot2grid((1,3), (0,0), rowspan=1, colspan=1)
ax2.plot_date(x=res_cun.PERIODO, y=res_cun['Área Sembrada(ha)'], linestyle='-', label ='Área Sembrada(ha)')
ax2.plot_date(x=res_cun.PERIODO, y=res_cun['Área Cosechada(ha)'], linestyle='-', label ='Área Cosechada(ha)')
ax2.xticks(rotation = 90)
ax2.legend()


#uNIR LAS BASES CON LAS MISMAS FECHAS PARA PODDER HACER EL PLOT

      

res_cun2 = res_cun
res_cun2 = res_cun2.rename(columns={'PERIODO':'date1'})

res_cun3 = pd.merge(left=res_cun2, right=precios, on='date1', how='outer')



res_cun3 =  res_cun3.sort_values(by='date1')

t_a= np.isfinite(res_cun3['Área Sembrada(ha)'])
t_p = np.isfinite(res_cun3['Precio (/KG)'])


#############Grafica
fig, ax1 = plt.subplots()
ax1.plot_date(x=res_cun3.date1[t_a], y=res_cun3['Área Sembrada(ha)'][t_a],
              linestyle='-', marker ='o', c='b')
ax1.set_ylabel('Área Sembrada(ha)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot_date(x=res_cun3.date1[t_p], y=res_cun3['Precio (/KG)'][t_p],
              linestyle='-', marker = 'o', c='tomato')

ax2.set_ylabel('Precio (/KG)', color='r')
ax2.tick_params('y', colors='r')

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph'
plt.savefig('papa_cund_2', figsize=(25,10) ,dpi = 199)



##############
plt.subplot2grid((1,3), (0,1), rowspan=1, colspan=1)
t_a= np.isfinite(res_cun3['Producción(t)'])
t_p = np.isfinite(res_cun3['Precio (/KG)'])


fig, ax1 = plt.subplots()
ax1.plot_date(x=res_cun3.date1[t_a], y=res_cun3['Producción(t)'][t_a],
              linestyle='-', marker ='o', c='b')
ax1.set_ylabel('Producción(t)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot_date(x=res_cun3.date1[t_p], y=res_cun3['Precio (/KG)'][t_p],
              linestyle='-', marker = 'o', c='tomato')

ax2.set_ylabel('Precio (/KG)', color='r')
ax2.tick_params('y', colors='r')

###############

t_a= np.isfinite(res_cun3['Rendimiento(t/ha)'])
t_p = np.isfinite(res_cun3['Precio (/KG)'])

plt.subplot2grid((1,3), (0,2), rowspan=1, colspan=1)
fig, ax1 = plt.subplots()
ax1.plot_date(x=res_cun3.date1[t_a], y=res_cun3['Rendimiento(t/ha)'][t_a],
              linestyle='-', marker ='o', c='b')
ax1.set_ylabel('Rendimiento(t/ha)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot_date(x=res_cun3.date1[t_p], y=res_cun3['Precio (/KG)'][t_p],
              linestyle='-', marker = 'o', c='tomato')

ax2.set_ylabel('Precio (/KG)', color='r')
ax2.tick_params('y', colors='r')

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/proyecto_colciencias/Primer_info/graph'

os.chdir(path)
plt.savefig('papa_cund_2', figsize=(20,10) ,dpi = 199)
plt.close()

# Generar tabla para poner en el documento
table = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/est_usadas_20180706.csv')
print(table.to_latex(index=False, longtable=True))

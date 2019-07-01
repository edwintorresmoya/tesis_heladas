
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Tue Dec 11 10:43:51 2018
# Creado para realizar los análisis de la precipitación de las estaciones autmáticas.
y Buscar si hay una relación entre la precipitación y la baja desviación estándar

Adicionalmente se realizó una gráfica para buscar el mínimo de temperatura registrado por la estación Tibaitatá
@author: edwin
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import pdb
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
#lista_1 = os.listdir()
#esta_list = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/lr_est_auto.csv')
#
#
#for icod in esta_list.CODIGO_CAT:
#    #print(icod)
#    if 'v_'+str(icod)+'_precip_1.csv' in lista_1:
#        base_validada = pd.read_csv('v_'+str(icod)+'_precip_1.csv')
#        
#        base_validada.date =  pd.to_datetime(base_validada.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
#        
#        if 'precip_1' not in base_validada.columns:
#            print('no hay temperatura')
#            continue
#        prec_real = base_validada[base_validada.val_prec == 0][['date', 'precip_1']]
#        prec_real['year'] = prec_real.date.dt.year
#        
#        prec_real_2 = prec_real[prec_real.year > 2010]
#        
#        if len(prec_real_2) < 10000:
#            print(un_busca_cod(base_validada.cod[0]))    
#            print('No año')
#            continue
#        
#        print('--------------------------------------------------------------')
#        print(un_busca_cod(base_validada.cod[0]))
#        print(prec_real_2.groupby(prec_real_2.year).sum().median())
#        print('--------------------------------------------------------------')
#        
#    
#        
#balideam = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estaciones_altura_20180905.csv')
#
#balideam_2 = busca_cod(balideam)
#balideam_2.to_cs
#
#
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
#base_validada = pd.read_csv('v_21206990_tmp_2m.csv')
#base_validada_tmp = base_validada[base_validada.val_tmp == 0]
#base_validada_tmp.date =  pd.to_datetime(base_validada_tmp.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
#inicio_1 = pd.to_datetime(20050101, format ='%Y%m%d', errors='coerce')
#fin_1 = pd.to_datetime(20181231, format ='%Y%m%d', errors='coerce')
#base_validada_2 = base_validada_tmp[(base_validada_tmp.date > inicio_1) & (base_validada_tmp.date < fin_1)]
#
#plt.plot_date(base_validada_2.date, base_validada_2.tmp_2m, color = 'gray')
#plt.axhline(-4.9, color = 'k') #-4.7
#plt.xlabel('Años')
#plt.ylabel('Temperatura °C')
#plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/grafica_minimas_tmp_tibaitata.png' ,dpi = 100)
#plt.close()
#
#
##plot de las altas y bajas temperaturas para las fechas seleccionadas
#
## Para el 2007
#
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
base_validada = pd.read_csv('v_21206990_tmp_2m.csv')
base_validada_tmp = base_validada[base_validada.val_tmp == 0]
base_validada_tmp.date =  pd.to_datetime(base_validada_tmp.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

inicio_1 = pd.to_datetime('20070203 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('20070205 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fecha_inicio = pd.to_datetime('20070204 01:50:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fecha_final = pd.to_datetime('20070204 07:10:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fecha_inicio_1 = pd.to_datetime('20070204 11:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fecha_final_1 = pd.to_datetime('20070204 16:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
base_validada_2 = base_validada_tmp[(base_validada_tmp.date > inicio_1) & (base_validada_tmp.date < fin_1)]

plt.rcParams["figure.figsize"] = (8,8)
plt.plot_date(base_validada_2.date, base_validada_2.tmp_2m, '-',color = 'gray')
plt.axhline(0, color = 'k', linestyle = '--')
plt.axhline(20, color = 'k', linestyle = ':') #-4.7
plt.xlabel('Fecha - Hora')
plt.ylabel('Temperatura °C')
plt.xticks(rotation=90)
plt.vlines(x=[ fecha_inicio_1, fecha_final_1], ymin=15, ymax=25, linestyle = ':', color = 'black' )
plt.vlines(x=[fecha_inicio, fecha_final], ymin=-5, ymax=5, linestyle = '--', color = 'black' )

plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/casos_altas_bajas/grafica_minimas_tmp_tibaitata_helada.png' ,dpi = 100)
plt.close()


# para el 2014
# Fechas de las gráficas
inicio_1 = pd.to_datetime('20140829 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('20140902 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
#Líneas debajo
fecha_inicio = pd.to_datetime('20140830 03:40:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fecha_final = pd.to_datetime('20140830 05:30:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

#Lineas de arriba
fecha_inicio_1 = pd.to_datetime('20140830 12:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fecha_final_1 = pd.to_datetime('20140830 17:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

fecha_inicio_2 = pd.to_datetime('20140901 12:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fecha_final_2 = pd.to_datetime('20140901 15:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

fecha_inicio_3 = pd.to_datetime('20140831 16:30:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fecha_final_3 = pd.to_datetime('20140831 15:30:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

base_validada_2 = base_validada_tmp[(base_validada_tmp.date > inicio_1) & (base_validada_tmp.date < fin_1)]

plt.rcParams["figure.figsize"] = (8,8)
plt.plot_date(base_validada_2.date, base_validada_2.tmp_2m, '-',color = 'gray')
plt.axhline(0, color = 'k', linestyle = '--')
plt.axhline(20, color = 'k', linestyle = ':') #-4.7
plt.xlabel('Fecha - Hora')
plt.ylabel('Temperatura °C')
plt.xticks(rotation=90)
plt.vlines(x=[ fecha_inicio_1, fecha_final_1, fecha_inicio_2, fecha_final_2, fecha_final_3, fecha_inicio_3], ymin=15, ymax=25, linestyle = ':', color = 'black' )
plt.vlines(x=[fecha_inicio, fecha_final], ymin=-5, ymax=5, linestyle = '--', color = 'black' )

plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/casos_altas_bajas/grafica_minimas_tmp_tibaitata_helada_2014.png' ,dpi = 100)
plt.close()

#para el 201509
inicio_1 = pd.to_datetime('20150906 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('20150909 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
#Líneas debajo
fecha_inicio = pd.to_datetime('20140830 03:40:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fecha_final = pd.to_datetime('20140830 05:30:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

#Lineas de arriba
l1 = pd.to_datetime('20150906 13:30:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
l2 = pd.to_datetime('20150906 16:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
l3 = pd.to_datetime('20150907 10:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
l4 = pd.to_datetime('20150907 15:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
l5 = pd.to_datetime('20150908 9:30:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
l6 = pd.to_datetime('20150908 17:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')



base_validada_2 = base_validada_tmp[(base_validada_tmp.date > inicio_1) & (base_validada_tmp.date < fin_1)]

plt.rcParams["figure.figsize"] = (8,8)
plt.plot_date(base_validada_2.date, base_validada_2.tmp_2m, '-',color = 'gray')
plt.axhline(0, color = 'k', linestyle = '--')
plt.axhline(20, color = 'k', linestyle = ':') #-4.7
plt.xlabel('Fecha - Hora')
plt.ylabel('Temperatura °C')
plt.xticks(rotation=90)
# líneas de arriba
plt.vlines(x=[ l1, l2, l3, l4, l5, l6], ymin=15, ymax=25, linestyle = ':', color = 'black' )
# líneas de abajo
#plt.vlines(x=[fecha_inicio, fecha_final], ymin=-5, ymax=5, linestyle = '--', color = 'black' )

plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/casos_altas_bajas/grafica_minimas_tmp_tibaitata_helada_201509.png' ,dpi = 100)
plt.close()

########################################

#para el 201508
inicio_1 = pd.to_datetime('20150827 12:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fin_1 = pd.to_datetime('20150830 00:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
#Líneas debajo
fecha_inicio = pd.to_datetime('20140830 03:40:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
fecha_final = pd.to_datetime('20140829 05:30:00', format ='%Y%m%d %H:%M:%S', errors='coerce')

#Lineas de arriba
l5 = pd.to_datetime('20150828 8:00:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
l6 = pd.to_datetime('20150828 11:30:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
l7 = pd.to_datetime('20150829 8:30:00', format ='%Y%m%d %H:%M:%S', errors='coerce')
l8 = pd.to_datetime('20150829 16:25:00', format ='%Y%m%d %H:%M:%S', errors='coerce')


base_validada_2 = base_validada_tmp[(base_validada_tmp.date > inicio_1) & (base_validada_tmp.date < fin_1)]

plt.rcParams["figure.figsize"] = (8,8)
plt.plot_date(base_validada_2.date, base_validada_2.tmp_2m, '-',color = 'gray')
plt.axhline(0, color = 'k', linestyle = '--')
plt.axhline(20, color = 'k', linestyle = ':') #-4.7
plt.xlabel('Fecha - Hora')
plt.ylabel('Temperatura °C')
plt.xticks(rotation=90)
# líneas de arriba
plt.vlines(x=[l5, l6, l7, l8], ymin=16, ymax=24, linestyle = ':', color = 'black' )
# líneas de abajo
#plt.vlines(x=[fecha_inicio, fecha_final], ymin=-5, ymax=5, linestyle = '--', color = 'black' )

plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/casos_altas_bajas/grafica_minimas_tmp_tibaitata_helada_201508.png' ,dpi = 100)
plt.close()

import pandas as pd
import numpy as np
import os 
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
from funciones import fechas_un_digito
from funciones import fechas_un_digito_columna
import pdb


os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios')
resumen = pd.read_pickle('resumen_tmp2_20181123.pickle') # Este fue el archivo original de la e
resumen2 = resumen

#resumen2['date_2'] = pd.to_datetime(resumen2.date_1.str[4:], format ='%Y-%m-%d_%H:%M:%S', errors='coerce')
#resumen2 = resumen2.sort_values('date_2')
#
#resumen2[(resumen2.cod == 21195160.0) & (resumen2.fecha == '/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6/resultados/') & (resumen2.date_1.str[0:3] == 'd01')].T2

tabla = resumen[resumen.fecha == '/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6/resultados/']
tabla['date_2'] = pd.to_datetime(tabla.date_1.str[4:], format ='%Y-%m-%d_%H:%M:%S', errors='coerce')
tabla = tabla.sort_values('date_2')
#tabla_p1 = tabla[(tabla.cod == 21195160.0) &  (tabla.date_1.str[0:3] == 'd01')]
#tabla[(tabla.cod == 21206980.0) &  (tabla.date_1.str[0:3] == 'd01')].T2
#['T2', 'alt_1', 'cod', 'combinacion', 'date_1', 'fecha', 'humedad', 'lat_1', 'latitud', 'lon_1', 'longitud', 'parametro', 'radiacion', 'rain', 'u10', 'v10', 'vel_viento', 'date_2']
f_ini = pd.to_datetime('20070201 2200')
f_fin = pd.to_datetime('20070203 0000')
#f_fin = pd.to_datetime('20070203 2200')

for i in tabla.cod.unique():
    print(i)
    tabla_3 = tabla[(tabla.date_2 > f_ini) & (tabla.date_2 <= f_fin) & (tabla.cod == i)].reset_index()
    tabla_3 = tabla_3.drop('index', axis=1)
    fecha_modif = pd.to_datetime(tabla_3.date_2) + pd.Timedelta('2 days')
    tabla_3.date_1 = tabla_3.date_1.str[0:4] + fecha_modif.dt.year.astype('str')+'-'+fechas_un_digito_columna(fecha_modif.dt.month).aaa+'-'+fechas_un_digito_columna(fecha_modif.dt.day).aaa + tabla_3.date_1.str[-9:]

    #tabla_3[tabla_3.date_1.str[0:3] == 'd01'].sort_values('date_2').T2
    #tabla_3[tabla_3.date_1.str[0:3] == 'd01'].sort_values('date_2')[['date_1', 'T2']]
    
    
    for uu in ['T2', 'humedad', 'radiacion', 'rain', 'u10', 'v10', 'vel_viento']:
        print(uu)
        #max_1 = tabla_3[uu].max()
        #min_1 = tabla_3[uu].min()
        #intervalo = (max_1 - min_1)/10
        #pdb.set_trace()
        valores = tabla_3[uu] * (.95)
        tabla_3[uu] = valores
    
    tabla_3 = tabla_3.drop('date_2', axis = 1)
    

    resumen = resumen.append(tabla_3)    
    
resumen.to_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/resumen_tmp3_20181123.pickle')

####Exploración de los datos
#resumen[resumen.fecha == tabla_3.fecha.unique()[0]].date_1.max()
#
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios')
#resumen = pd.read_pickle('resumen_tmp2_20181123.pickle') # Este fue el archivo original de la e
#
#
#
#tabla = resumen[resumen.fecha == '/scr/hercules1san/meteoro/edwin/wrf/resultados/200701_18_6/resultados/']
#tabla[(tabla.cod == 21206790.0) &  (tabla.date_1.str[0:3] == 'd01')].T2
#tabla['date_2'] = pd.to_datetime(tabla.date_1.str[4:], format ='%Y-%m-%d_%H:%M:%S', errors='coerce')
##['T2', 'alt_1', 'cod', 'combinacion', 'date_1', 'fecha', 'humedad', 'lat_1', 'latitud', 'lon_1', 'longitud', 'parametro', 'radiacion', 'rain', 'u10', 'v10', 'vel_viento', 'date_2']
#f_ini = pd.to_datetime('20070202 1700')
#f_fin = pd.to_datetime('20070203 1700')
#
#for i in tabla.cod.unique():
#    print(i)
#    tabla_3 = tabla[(tabla.date_2 >= f_ini) & (tabla.date_2 >= f_fin) & (tabla.cod == i)].reset_index()
#    tabla_3 = tabla_3.drop('index', axis=1)
#    fecha_modif = pd.to_datetime(tabla_3.date_2) + pd.Timedelta('1 days')
#    tabla_3.date_1 = tabla_3.date_1.str[0:4] + fecha_modif.dt.year.astype('str')+'_'+fechas_un_digito_columna(fecha_modif.dt.month).aaa+'_'+fechas_un_digito_columna(fecha_modif.dt.day).aaa + tabla_3.date_1.str[-9:]
#    
#    for uu in ['T2', 'humedad', 'radiacion', 'rain', 'u10', 'v10', 'vel_viento']:
#        print(uu)
#        max_1 = tabla_3[(tabla_3.date_2 >= f_ini) & (tabla_3.date_2 >= f_fin) & (tabla_3.cod == i)][uu].max()
#        min_1 = tabla_3[(tabla_3.date_2 >= f_ini) & (tabla_3.date_2 >= f_fin) & (tabla_3.cod == i)][uu].min()
#        intervalo = (max_1 - min_1)/10
#        valores = tabla_3[(tabla_3.date_2 >= f_ini) & (tabla_3.date_2 >= f_fin) & (tabla_3.cod == i)][uu] * (.95)
#        tabla_3[uu] = valores
#    
#    tabla_3 = tabla_3.drop('date_2', axis = 1)
#    #pdb.set_trace()
#    resumen = resumen.append(tabla_3)    
#resumen.to_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/resumen_tmp3_20181123.pickle')

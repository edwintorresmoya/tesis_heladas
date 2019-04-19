#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:57:45 2019

@author: edwin
"""

import os
import pandas as pd
import numpy as np
import pdb
import time
import datetime
import pdb



os.chdir('/media/edwin/disco2/gfs/2006_2007')

lista = os.listdir()

lista_2 = pd.DataFrame({'file_1':lista})

lista_2['year_1'] = lista_2.file_1.str[0:4]
lista_2['month_1'] = lista_2.file_1.str[4:6]
lista_2['day_1'] = lista_2.file_1.str[6:8]

lista_2['hour_1'] = lista_2.file_1.str[8:10]

lista_2.year_1.astype(str)+'-'+ lista_2.month_1.astype(str)+'-'+ lista_2.day_1.astype(str)+'-'+lista_2.hour_1.astype(str) # Convertir de número a string

lista_2['date'] = pd.to_datetime(lista_2.year_1.astype(str)+'-'+ lista_2.month_1.astype(str)+'-'+ lista_2.day_1.astype(str)+'-'+lista_2.hour_1.astype(str), format ='%Y-%m-%d-%H', errors='coerce')
#lista_2 = lista_2.drop(['year_1', 'month_1', 'day_1', 'year_1', 'hour_1'], 1)




lista_2.date.min()
lista_2.date.max()

date_1 = pd.to_datetime(lista_2.date.min())
horas = []
while date_1 <= lista_2.date.max():
    horas.append(date_1)
    date_1 += pd.Timedelta('6 hours')
    
hora_3 = pd.DataFrame({'date':horas})

base_unida = pd.merge(lista_2, hora_3, how='outer', on='date')

base_unida = base_unida.sort_values('date').reset_index()
base_unida = base_unida.drop('index', 1)

base_unida[base_unida.hour_1.isnull()].date

# Hay 4 días que no se van a haver por falta de datos
# Los días que hacen falta son del 2006 06-23 2006 09-18, 19 y 20
#por esta razon los voy a quitar

para_quitar = pd.DataFrame()




para_quitar2 = pd.DataFrame({'list_1':base_unida[base_unida.year_1.astype(str)+'-'+ base_unida.month_1.astype(str)+'-'+ base_unida.day_1.astype(str) == '2006-06-23'].index.tolist()})
para_quitar3 = pd.DataFrame({'list_1':base_unida[base_unida.year_1.astype(str)+'-'+ base_unida.month_1.astype(str)+'-'+ base_unida.day_1.astype(str) == '2006-09-18'].index.tolist()})
para_quitar4 = pd.DataFrame({'list_1':base_unida[base_unida.year_1.astype(str)+'-'+ base_unida.month_1.astype(str)+'-'+ base_unida.day_1.astype(str) == '2006-09-19'].index.tolist()})
para_quitar5 = pd.DataFrame({'list_1':base_unida[base_unida.year_1.astype(str)+'-'+ base_unida.month_1.astype(str)+'-'+ base_unida.day_1.astype(str) == '2006-09-20'].index.tolist()})

para_quitar = pd.concat([para_quitar, para_quitar2, para_quitar3, para_quitar4, para_quitar5])

base_unida.iloc[para_quitar.list_1.tolist(),:]


base_unida2 = base_unida.drop(base_unida.index[para_quitar.list_1.tolist()]) # quital filas

#División por meses para hacer el WPS

base_unida2.date.head()



date_1 = pd.to_datetime(lista_2.date.min())
horas_2 = []
while date_1 <= lista_2.date.max():
    horas_2.append(date_1)
    date_1 += pd.Timedelta('24 hours')
hora_4 = pd.DataFrame({'date':horas_2})

hora_4['year'] = hora_4.date.dt.year
hora_4['month_1'] = hora_4.date.dt.month
hora_4['day_1'] = hora_4.date.dt.day


os.chdir('/media/edwin/disco2/gfs/wps')

#pdb.set_trace()
    
for j in hora_4.index[421:428]: # se quita el primero y el último para poder tomar 6 horas antes y poder hacer la simulación del último día sin errores, ya que la simulación se hace con los datos del día hasta la primera hora del degundo día
    print(j)
    try:
        os.mkdir('/media/edwin/disco2/gfs/wps/'+str(j))
    except FileExistsError:
        pass
    #os.chdir('/media/edwin/disco2/gfs/wps/'+str(j))
    
    month_1 = str(hora_4.month_1[j])
    month_1_1 = month_1
    if len(month_1) < 2:
        month_1_1 = '0'+month_1
    

    day_1 = str(hora_4.day_1[j])
    day_1_1 = day_1
    if len(day_1) < 2:
        day_1_1 = '0'+day_1
    
    month_2 = str(hora_4.month_1[j+1])
    month_2_1 = month_2
    if len(month_2) < 2:
        month_2_1 = '0'+month_2

    day_2 = str(hora_4.day_1[j+1])
    day_2_1 = day_2
    if len(day_2) < 2:
        day_2_1 = '0'+day_2
            
    os.chdir('/media/edwin/disco2/gfs/wps/'+str(j))
    os.popen('ln -s ~/wrf_b/wrf/WPS/* .')
    os.popen('ln -s ~/wrf_b/wrf/WPS/ungrib/Variable_Tables/Vtable.GFS Vtable')
    os.popen('ln -s ~/wrf_b/wrf/WPS/geogrid/GEOGRID.TBL_igac GEOGRID.TBL')
    os.popen('ln -s ~/wrf_b/wrf/WPS/metgrid/METGRID.TBL .')
    os.popen('ln -s ~/wrf_b/wrf/WRFV3/run/* .')

    f = open('/media/edwin/disco2/gfs/wps/'+str(j)+'/namelist.wps', 'w')
    with open('/media/edwin/disco2/gfs/wps/'+str(j)+'/namelist.wps', 'w') as f:
        print('&share', file=f)
        print(" wrf_core = 'ARW',", file=f)
        print(' max_dom = 2,', file=f)
        print(" start_date = '"+str(hora_4.year[j])+"-"+str(month_1_1)+"-"+str(day_1_1)+"_00:00:00','"+str(hora_4.year[j])+"-"+str(month_1_1)+"-"+str(day_1_1)+"_00:00:00',", file=f)
        print(" end_date   = '"+str(hora_4.year[j])+"-"+str(month_2_1)+"-"+str(day_2_1)+"_00:00:00','"+str(hora_4.year[j])+"-"+str(month_2_1)+"-"+str(day_2_1)+"_00:00:00',", file=f)
        print(' interval_seconds = 21600,', file=f)
        print(' io_form_geogrid = 2,', file=f)
        print('', file=f)
        print(' debug_level = 0,', file=f)
        print('/', file=f)
        print('', file=f)
        print('&geogrid', file=f)
        print(' parent_id         = 1,1,', file=f)
        print(' parent_grid_ratio = 1,3,', file=f)
        print(' i_parent_start    = 1,12,', file=f)
        print(' j_parent_start    = 1,12,', file=f)
        print(' e_we          = 99,232,', file=f)
        print(' e_sn          = 94,214,', file=f)
        print(" geog_data_res = 'igac_lu_30s+30s','igac_lu_30s+30s',", file=f)
        print(' dx = 6000,', file=f)
        print(' dy = 6000,', file=f)
        print(" map_proj =  'mercator',", file=f)
        print(' ref_lat   = 4.916,', file=f)
        print(' ref_lon   = -73.902,', file=f)
        print(' truelat1  = 4.916,', file=f)
        print(' truelat2  = 0,', file=f)
        print(' stand_lon = -73.902,', file=f)
        print(" geog_data_path = '/home/edwin/wrf_b/wrf/geog',", file=f)
        print('', file=f)
        print(' ref_x = 49.5,', file=f)
        print(' ref_y = 47.0,', file=f)
        print('/', file=f)
        print('', file=f)
        print('&ungrib', file=f)
        print(" out_format = 'WPS',", file=f)
        print(" prefix = 'FILE',", file=f)
        print('/', file=f)
        print('', file=f)
        print('&metgrid', file=f)
        print(" fg_name = 'FILE',", file=f)
        print(' io_form_metgrid = 2,', file=f)
        print('', file=f)
        print('', file=f)
        print('/', file=f)
        print('', file=f)
        print('&mod_levs', file=f)
        print(' press_pa = 201300 , 200100 , 100000 ,', file=f)
        print('             95000 ,  90000 ,', file=f)
        print('             85000 ,  80000 ,', file=f)
        print('             75000 ,  70000 ,', file=f)
        print('             65000 ,  60000 ,', file=f)
        print('             55000 ,  50000 ,', file=f)
        print('             45000 ,  40000 ,', file=f)
        print('             35000 ,  30000 ,', file=f)
        print('             25000 ,  20000 ,', file=f)
        print('             15000 ,  10000 ,', file=f)
        print('              5000 ,   1000', file=f)
        print(' /', file=f)
        print('', file=f)
        print('', file=f)
        print('&domain_wizard', file=f)
        print('', file=f)
        print(" grib_vtable = 'Vtable.GFS',", file=f)
        print(' dwiz_name    =2_dominios', file=f)
        print(' dwiz_desc    =', file=f)
        print(' dwiz_user_rect_x1 =2345', file=f)
        print(' dwiz_user_rect_y1 =1875', file=f)
        print(' dwiz_user_rect_x2 =2429', file=f)
        print(' dwiz_user_rect_y2 =1955', file=f)
        print(' dwiz_show_political =true', file=f)
        print(' dwiz_center_over_gmt =true', file=f)
        print(' dwiz_latlon_space_in_deg =10', file=f)
        print(' dwiz_latlon_linecolor =-8355712', file=f)
        print(' dwiz_map_scale_pct =50.0', file=f)
        print(' dwiz_map_vert_scrollbar_pos =1625', file=f)
        print(' dwiz_map_horiz_scrollbar_pos =1795', file=f)
        print(' dwiz_gridpt_dist_km =4.2', file=f)
        print(' dwiz_mpi_command =null', file=f)
        print(' dwiz_tcvitals =null', file=f)
        print(' dwiz_bigmap =Y', file=f)
        print('/', file=f)
        
        ####Copia de los archivos
        
    
    
    os.chdir('/media/edwin/disco2/gfs/wps/'+str(j))
    fechas_grb = base_unida2[(base_unida2.date >= hora_4.date[j]) & (base_unida2.date <= (hora_4.date[j]+ pd.Timedelta('1 days')))]
    
    link_ini = './link_grib.csh /media/edwin/disco2/gfs/2006_2007/{'
    for kk in fechas_grb.file_1:
        link_ini += kk+','
    
    try:
        os.popen(link_ini[:-1]+'}')
    except:
        continue
    
        
    f = open('/media/edwin/disco2/gfs/wps/'+str(j)+'/ejec.sh', 'w')
    with open('/media/edwin/disco2/gfs/wps/'+str(j)+'/ejec.sh', 'w') as f:
        print('#!/bin/bash', file=f)
        print('./geogrid.exe', file=f)
        print('./ungrib.exe', file=f)
        print('./metgrid.exe', file=f)
    print('hola')
    
    os.popen('bash ejec.sh > log.txt')
    time.sleep(5)
    while open('log.txt', 'r').read()[-77:-67] != 'Successful':
        time.sleep(10)
    
    os.system('spd-say "End process 1"')
        
    os.popen('ls | grep -v -e met_em -e namelist.wps -e log.txt | xargs rm')
        

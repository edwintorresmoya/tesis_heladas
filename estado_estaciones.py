#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:11:08 2019
verificación del estado de las estaciones
@author: edwin
"""


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)
        
#os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col1/')

lista_est_1 = pd.DataFrame({'todo':os.listdir()})
lista_cod = lista_est_1.todo.str[2:10].unique()[1:]

###Estas son las estaciones que no tienen valores de temperatura
# Dado que no tienen temperatura no están dentro de las estacinoes que se validaron dentro de la carpeta validados_col_col
lista_1 = [21201580,21202270,21202271,21206710,21209920,26127010,35025100,35027001,35027002]

for i in (lista_cod):
    for j in lista_1:
        if int(i) == j:
            print(i, j)
            
for k in [1,2,3, 4]:
    print(k)
    
    if k == 1:
        year = str(201509)
        fecha_inicio = pd.to_datetime(20150907, format ='%Y%m%d', errors='coerce')
        fecha_fin = pd.to_datetime(20150910, format ='%Y%m%d', errors='coerce')
                
    if k == 2:
        year = str(201408)
        fecha_inicio = pd.to_datetime(20140829, format ='%Y%m%d', errors='coerce')
        fecha_fin = pd.to_datetime(20140901, format ='%Y%m%d', errors='coerce')
    
    if k == 3:
        year = str(200702)
        fecha_inicio = pd.to_datetime(20070201, format ='%Y%m%d', errors='coerce')
        fecha_fin = pd.to_datetime(20070205, format ='%Y%m%d', errors='coerce')
        
    if k == 4:
        year = str(201508)
        fecha_inicio = pd.to_datetime(20150827, format ='%Y%m%d', errors='coerce')
        fecha_fin = pd.to_datetime(20150830, format ='%Y%m%d', errors='coerce')
    
    #Extracción de los datos horarios
    step = datetime.timedelta(hours=1)
    inicio_date = fecha_inicio
    fin_date = fecha_fin
    result = []
    while inicio_date <= fin_date:
        result.append(inicio_date)
        inicio_date += step
    
    fechas = pd.DataFrame({'date':result})
    
    validos = []
    validos_valores = []
    for ii in lista_est_1[lista_est_1.todo.str.contains('tmp_2m')].todo:
        print(ii)
        base_validada = pd.read_csv(ii)
        base_validada.date =  pd.to_datetime(base_validada.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
        base_val = base_validada[(base_validada.date > fecha_inicio) & (base_validada.date < fecha_fin) & (base_validada.val_tmp == 0)]
        validos_valores.append(len(base_val))
        if (len(base_val) > 10):
            validos.append(True)
        else:
            validos.append(False)
        
        if len(base_val) < 1:
            print(ii[2:10]+'-'+year, 'No hay datos')
            continue
        
        base_val_1 = pd.merge(fechas, base_val, on = 'date', how='inner')
        
        plt.plot_date(base_val_1.date, base_val_1.tmp_2m)
        plt.xlabel('Fecha - Hora')
        plt.ylabel('Temperatura °C')
        plt.xticks(rotation=90)
        plt.vlines(x=[ fecha_inicio, fecha_fin], ymin=base_val.tmp_2m.min(), ymax=base_val.tmp_2m.max(), linestyle = ':', color = 'black' )
        plt.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_temp_simulaciones/'+year+'-'+ii[2:10]+'.png' ,dpi = 100)
        plt.close()
        #plt.show()
    
#resumen_1 = pd.DataFrame({'cod':lista_est_1[lista_est_1.todo.str.contains('tmp_2m')].todo, 'valor':validos_valores,
#                                'cond':validos})    
#        
#resumen_1[resumen_1.cond == True].shape
#resumen_1
    
import datetime

dt = datetime.datetime(2010, 12, 1)
end = datetime.datetime(2010, 12, 30, 23, 59, 59)
step = datetime.timedelta(seconds=5)

result = []

while dt < end:
    result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
    dt += step      


    

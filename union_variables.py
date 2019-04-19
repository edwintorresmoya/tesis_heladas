#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:56:11 2018

@author: edwin
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:07:58 2018

@author: edwin
"""




############### Caracterización de la variable deseada

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspect
from datetime import datetime  
from datetime import timedelta
import matplotlib.dates as mdates
import pdb



def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)




os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col1')
file_list = pd.DataFrame({'list_1':os.listdir()})
file_list['cod'] = file_list.list_1.str[2:10]
file_list['var_1'] = file_list.list_1.str[11:-4]
estacion_var = []
estacion_1 = pd.DataFrame({'date':[]})

#def caracterizacion():
for co in file_list.cod.unique():
    for va in file_list.var_1.unique():
        if 'v_'+str(co) + '_'+str(va)+'.csv' in list(file_list.list_1):
            print('v_'+str(co) + '_'+str(va)+'.csv')
            base_2 = pd.read_csv('v_'+str(co) + '_'+str(va)+'.csv')
            estacion_1 = pd.merge(estacion_1, base_2, on='date', how='outer')
            #Corrección de las fechas
    estacion_1.date = pd.to_datetime(estacion_1.date, format ='%Y%m%d %H:%M:%S', errors='coerce')
    estacion_1 = estacion_1.sort_values('date')
     
    
    
    estacion_1['date_2'] = (estacion_1.date.dt.year * 10000) + (estacion_1.date.dt.month * 100) + (estacion_1.date.dt.day)
    estacion_1['date_ant'] = estacion_1.date - timedelta(days=1)
    estacion_1['date_ant'] = ((estacion_1.date_ant.dt.year) * 10000) + ((estacion_1.date_ant.dt.month ) * 100) + ((estacion_1.date_ant.dt.day))
    
    ###Busqueda de las heladas
    estacion_1[(estacion_1.val_tmp == 0) & (estacion_1.tmp_2m < 0)]
    np.where(((estacion_1.val_tmp == 0) & (estacion_1.tmp_2m < 0)), 1, 0) # 1 = Helada. Si se cumple que la temperatura está bajo cero y es un dato válido entonces se coloca 1
    
    union_1 = estacion_1[['date_2', 'date_ant']]
    union_1['heladas'] = np.where(((estacion_1.val_tmp == 0) & (estacion_1.tmp_2m < 0)), 1, 0)
    
    union_2 = pd.DataFrame(union_1.groupby(['date_2'])['heladas'].max())
    union_2['date_2'] = union_2.index
    ###Unión con los valores de helada del mismo día
    estacion_2 = pd.merge(estacion_1, union_2, on='date_2', how='outer')
    ###unión con los valores de las heladas del día anterior
    union_3 = pd.DataFrame(union_1.groupby(['date_ant'])['heladas'].max())
    union_3['date_2'] = union_3.index
    union_3.columns.values[0] = 'heladas_antes'
    
    estacion_3_1 = pd.merge(estacion_2, union_3, on='date_2', how='outer')
    
    
    # búsqueda de las altas temperaturas
    
    #Extracción de los valores superiores a 25
    union_1_1 = estacion_1[['date_2', 'date_ant']]
    union_1_1['altas'] = np.where(((estacion_1.val_tmp == 0) & (estacion_1.tmp_2m > 25)), 1, 0)
    #agrupación de los valores por presencia de las altas temperaturas
    union_2_1 = pd.DataFrame(union_1_1.groupby(['date_2'])['altas'].max())
    union_2_1['date_2'] = union_2_1.index
    estacion_3_1 = pd.merge(estacion_3_1, union_2_1, on='date_2', how='outer')
    union_3_1 = pd.DataFrame(union_1_1.groupby(['date_ant'])['altas'].max())
    union_3_1['date_2'] = union_3_1.index
    union_3_1.columns.values[0] = 'altas_antes'
    
    #Unión de las bases con las heladas y las altas temperaturas
    estacion_3 = pd.merge(estacion_3_1, union_3_1, on='date_2', how='outer')
    
    ## 
    # Modificación usada par la ectracción de las horas
    estacion_3['hora'] = 10000+ (estacion_3.date.dt.hour * 100) + (estacion_3.date.dt.minute)
    estacion_3['hora_n'] = (estacion_3.date.dt.hour * 100) + (estacion_3.date.dt.minute/ 60)
    estacion_3['hora'] = estacion_3.hora.astype('str')
    qqq = estacion_3.hora.str[1:]
    www = qqq.str[:-2]
    estacion_3['hora'] = pd.to_datetime(www, format ='%H%M', errors='coerce')
    
    estacion_3.to_pickle('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/bases_unidas/'+str(co)+'.pickle')
    estacion_var = []
    estacion_3 = []
    estacion_1 = pd.DataFrame({'date':[]})
    ###################
    ## Comienzan los plots
    ###################

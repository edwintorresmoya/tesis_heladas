#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:07:45 2018

@author: edwin
"""


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspect
from datetime import datetime  
from datetime import timedelta
import matplotlib.dates as mdates



###############
def lista_nombres(base):
    base2 = pd.DataFrame(list(base))
    print(base2)
    return(base2)
#################


os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col1')
file_list = os.listdir()

estacion_1 = pd.DataFrame({'date':[]})
for uu in file_list:
    if 'tmp_2m' in uu:
        print(uu)
        base_2 = pd.read_csv(uu)
        base_2.date = pd.to_datetime(base_2.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

        base_2['hora'] = 10000+ (base_2.date.dt.hour * 100) + (base_2.date.dt.minute)
        base_2['hora_n'] = (base_2.date.dt.hour * 100) + (base_2.date.dt.minute/ 60)
        base_2['hora'] = base_2.hora.astype('str')
        qqq = base_2.hora.str[1:]
        www = qqq
        base_2['hora'] = pd.to_datetime(www, format ='%H%M', errors='coerce')
        
        plt.plot_date(base_2[base_2.val_tmp ==0].hora, base_2[base_2.val_tmp ==0].tmp_2m)
        plt.plot_date(base_2[(base_2.val_tmp ==0)&((base_2.tmp_2m > 0.4)|(base_2.tmp_2m < 0.0))].hora, base_2[(base_2.val_tmp ==0)&((base_2.tmp_2m > 0.4)|(base_2.tmp_2m < 0.0))].tmp_2m)
        plt.xticks(rotation=90)
        plt.show()
        plt.close()
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:04:28 2018
Usado para buscar las fechas en las que la temperatura estuvo debajo de 0°C y sobre 20
@author: edwin
"""


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.gridspec as gridspect

def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)

#  importación de los datos de las estaciones convencionales

path = '/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam'
os.chdir(path)

cod_conv = pd.read_csv('codigo_est_aut_zon.csv')
ideam_rs_3_nona = pd.read_csv('ideam_zona_nonan.csv')
ideam_rs_3_nona.date = pd.to_datetime(ideam_rs_3_nona.date, format ='%Y%m%d %H:%M:%S', errors='coerce')

#estaciones de la Zona 

conv_tiba = ideam_rs_3_nona[ideam_rs_3_nona.cod.isin(cod_conv.cod)]

conv_tiba.date = pd.to_datetime(conv_tiba.date, format ='%Y%m%d %H:%M:%S', errors='coerce')


convenc_f =  conv_tiba[(conv_tiba.TS > 20) | (conv_tiba.TS < 0)][['cod','date', 'TS']]

convenc_f = convenc_f.sort_values(by=['TS'])

convenc_f1 = busca_cod(convenc_f)

convenc_f1.to_csv('~/Downloads/convencionales.csv')


conv_tiba = pd.read_csv('conv_tiba.csv')        


## Búsqueda de las estaciones automáticas


os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/validados_col_col/')
lista1 = os.listdir()

colec = pd.DataFrame({'date':[], 'tmp_2m':[], 'cod':[]})

for ii in lista1:
    if 'tmp_2m.csv' in ii:
        base = pd.read_csv(ii)
        base1 = base[base.val_tmp == 0]
        base2 = base1[(base1.tmp_2m > 25) | (base1.tmp_2m < 0)][['date', 'tmp_2m']]
        base2['cod'] = ii[2:10]
        colec = colec.append(base2)
        
colec_1 = busca_cod(colec)
colec_1 = colec_1.sort_values(by=['tmp_2m'])
colec_1.to_csv('~/Downloads/automaticas.csv')



    
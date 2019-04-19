#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 16:55:50 2018

@author: edwin
"""

import pandas as pd
import os
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_validados_20180620')
lista_1 = os.listdir()
summary_1 = pd.DataFrame(columns = ['cod', 'count_1'])
summary_3 =  pd.DataFrame(columns = ['cod', 'count_1'])
summary_4 = pd.DataFrame({'cod':[], 'count_1':[]})
lista_9 = pd.DataFrame({'aa':['cod;tipo;median']})
for i in lista_1:
    print(i)
    base = pd.read_csv(i)
    summary_2 = summary_1.append(pd.DataFrame({'cod':base.cod.unique(), 'count_1':len(base) })) # Adicion del código único de la estación
    para_unir = pd.DataFrame(base[[col for col in base if col.startswith('val')]].sum()).transpose() # Se están sumando los valores que no cumplen
    para_unir['cod'] = base.cod.unique()
    para_unir['cod'] = base.cod.unique()
    summary_3 = pd.DataFrame(summary_2.merge(para_unir, on='cod'))
    
    summary_4 =pd.concat([summary_3, summary_4])
    
summary_5 = summary_4
summary_5.val_dir = summary_5.val_dir *100 / summary_4.count_1
summary_5.val_hum = summary_5.val_hum *100 / summary_4.count_1
summary_5.val_prec = summary_5.val_prec *100 / summary_4.count_1
summary_5.val_rad = summary_5.val_rad *100 / summary_4.count_1
summary_5.val_tmp = summary_5.val_tmp *100 / summary_4.count_1
summary_5.val_vv = summary_5.val_vv *100 / summary_4.count_1

summary_4.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/conteo_numero.csv')    
summary_5.to_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/conteo.csv')

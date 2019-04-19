#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:53:57 2019
Código creado para realizar los diagramas de Taylor de las diferentes variables
@author: edwin
"""


import pandas as pd
import os
os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam')
import numpy as np
import matplotlib.pyplot as plt
from taylor_diagram import diagrama_taylor
import matplotlib.pyplot as PLT
#anno_1 = '200702'
#pp = '_hum_2m.csv'
#pp = '_val_rad.csv'
#i = 21206930.0


for anno_1 in ['200702', '201408', '201508', '201509']:
    print(anno_1)
    
    for pp, pp_col, pp_val, pp_col_wrf in zip(['_hum_2m.csv','_val_rad.csv', '_precip_1.csv'],
                                  ['hum_2m', 'rad_1', 'precip_1'],
                                  ['val_hum','val_rad', 'val_prec'],
                                  ['humedad','radiacion','rain']):#,'_precip_1.csv']





        # Ojo ejecutar el comando taylor_diagrama.py
        #'/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion.csv'
        #recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/Extraccion_dominios/ta_rasumen_ejem_20181124_con_correccion.csv')
        recep_t = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/otras_variables/taylormejores_var_'+anno_1+pp)        
        #print(recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())])
        #
        ##Se usa para hacer el remplazo de los nombres
        #recep_t.tipo_1 = recep_t.tipo_1.replace('36-12-4', 'Caso 1')
        #recep_t.tipo_1 = recep_t.tipo_1.replace('18-6-2', 'Caso 2')
        #recep_t.tipo_1 = recep_t.tipo_1.replace('6-2', 'Caso 3')
        #recep_t.tipo_1 = recep_t.tipo_1.replace('solo2', 'Caso 4')
        #recep_t.tipo_1 = recep_t.tipo_1.replace('10-3', 'Caso 5')
        #21206980
        for i in recep_t.cod_1.unique():
            print(i)
            para_t = recep_t[(recep_t.cod_1 == i) & (-recep_t.r2.isnull())][['std_estandar', 'r2', 'tipo_1', 'dom_1', 'std_pura']]
            para_t['orden'] = para_t.tipo_1.str[-2:]
            para_t = para_t.sort_values(['orden', 'tipo_1'])
            para_t['name'] = para_t.tipo_1 +'-'+ para_t.dom_1
            if len(para_t) < 1:
                continue
            PLT.rcParams["figure.figsize"] = (8,5)
            diagrama_taylor(para_t[['std_estandar','r2','name']].reset_index().iloc[:,[1,2,3]], #Tabla usada para ingresar los valores
                            para_t.std_pura.iloc[0], # se toma la desviación estándar real
                            '  ')# Se toma el código
            
            
            PLT.savefig('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/graficas_taylor_otras_variables/taylor_'+ str(i)[:-2]+'_'+anno_1+pp+'.png', dpi = 100)
            PLT.close()

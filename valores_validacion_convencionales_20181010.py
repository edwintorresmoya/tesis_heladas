#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:31:57 2018
# Creado para hacer una tabla para poder contar los no valores y spikes de las 
estaciones convencionales
@author: edwin
"""

import os
import pandas as pd

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/datos_ideam/convencionales_validados/datos')
lista_1 = os.listdir()

recolec = pd.DataFrame({'Código':[],
                        'Tipo':[],
                        'No datos (%)':[],
                        'P. Saltos (%)':[],
                        'Total de datos':[]})

for o in lista_1:
    #o = '21205013_Máximos_absolutos_val.csv'
    #print(o)
    base = pd.read_csv(o)
    cod = o[0:8]
    tipo_1 = o[9:-8]
    total = len(base)
    missing_1 = base.missin_data.sum()
    missing_por = missing_1 * 100 / total
    
    spikes_1 = base.spikes.sum()
    spikes_por = spikes_1 *100 / total
    
    recolec_1 = pd.DataFrame({'Código':[cod],
                              'Tipo':[tipo_1],
                            'No datos (%)':[missing_por],
                            'P. Saltos (%)':[spikes_por],
                            'Total de datos':[total]})
    recolec = pd.concat([recolec, recolec_1])    

recolec = recolec.iloc[:,[0,3,1,2,4]]

    
    
print(recolec.round(4).to_latex(index=False, longtable = True))

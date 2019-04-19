#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 09:37:21 2018

@author: edwin
"""

import pandas as pd
import numpy as np
import os


def lista_nombres(base):
        base2 = pd.DataFrame(list(base))
        return(base2)

os.chdir('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis')

balwrf1 = pd.read_csv('resumen_tmp_altura.csv')
balwrf2 = pd.read_csv('resumen_tmp_altura10_37.csv')
balwrf3 = pd.read_csv('resumen_tmp_alturas_20181022.csv')
#balwrf3 = pd.read_csv('resumen_tmp_4dom_20181014.csv') # Esto son los anteriores dominios usados



balwrf0 = balwrf1.append(balwrf2)
balwrf = balwrf0.append(balwrf3)

balwrf = balwrf[-balwrf.cod.isnull()].reset_index()

balwrf = balwrf.iloc[1:,]
balideam = pd.read_csv('/media/edwin/6F71AD994355D30E/Edwin/Maestría Meteorologia/Tesis/estaciones_altura_20180905.csv')
balwrf.cod
balwrf.cod = balwrf['cod'].astype(np.int64)

balideam.cod

union_b = pd.merge(balwrf, balideam, how='outer', on='cod')

union_b['correc_1'] = (union_b.msnm - union_b.al_alos) * 0.0065



union_b.to_csv('union_b_20180905.csv')
union_b = pd.read_csv('union_b_20180905.csv')

union_b.fecha.unique()
